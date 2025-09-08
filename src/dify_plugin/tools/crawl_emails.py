import email
import imaplib
from collections.abc import Generator
from datetime import date
from email.header import decode_header
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage


class CrawlEmailsTool(Tool):
    def _invoke(
        self, tool_parameters: dict[str, Any]
    ) -> Generator[ToolInvokeMessage, None, None]:
        """
        爬取指定文件夹中的当日邮件并合并为文档

        Args:
            tool_parameters: 包含工具参数的字典
                - folder_name (str): 邮件文件夹名称
                - output_format (str): 输出格式 (markdown, html, txt)

        Yields:
            ToolInvokeMessage: 包含合并后邮件内容的消息
        """
        # 1. 获取凭证
        try:
            email_address = self.runtime.credentials["email_address"]
            auth_code = self.runtime.credentials["authorization_code"]
        except KeyError:
            raise Exception("邮箱凭证未配置或无效，请在插件设置中提供邮箱地址和授权码")

        # 2. 获取工具参数
        folder_name = tool_parameters.get("folder_name", "INBOX")
        output_format = tool_parameters.get("output_format", "markdown")

        # 3. 连接邮箱并爬取邮件
        try:
            # 连接到QQ邮箱IMAP服务器
            mail = imaplib.IMAP4_SSL("imap.qq.com", 993)
            mail.login(email_address, auth_code)

            # 选择文件夹
            mail.select(folder_name)

            # 搜索今天的邮件
            today = date.today().strftime("%d-%b-%Y")
            search_criteria = f'(ON "{today}")'
            status, messages = mail.search(None, search_criteria)

            # 解析邮件ID
            email_ids = messages[0].split()

            # 收集邮件内容
            emails_content = []
            for email_id in email_ids:
                # 获取邮件
                status, msg_data = mail.fetch(email_id, "(RFC822)")

                # 解析邮件
                msg = email.message_from_bytes(msg_data[0][1])

                # 解析邮件信息
                subject = self._decode_header(msg["Subject"])
                sender = self._decode_header(msg["From"])
                date_received = msg["Date"]

                # 获取邮件正文
                body = self._get_email_body(msg)

                # 格式化邮件内容
                formatted_email = self._format_email_content(
                    subject, sender, date_received, body, output_format
                )
                emails_content.append(formatted_email)

            # 关闭连接
            mail.close()
            mail.logout()

            # 4. 合并邮件内容
            merged_content = self._merge_emails(emails_content, output_format)

            # 5. 返回结果
            yield self.create_text_message(merged_content)

        except Exception as e:
            raise Exception(f"爬取邮件失败: {e}")

    def _decode_header(self, header):
        """解码头部信息"""
        if header is None:
            return ""
        decoded_parts = decode_header(header)
        decoded_string = ""
        for part, encoding in decoded_parts:
            if isinstance(part, bytes):
                decoded_string += part.decode(encoding or "utf-8")
            else:
                decoded_string += part
        return decoded_string

    def _get_email_body(self, msg):
        """获取邮件正文"""
        if msg.is_multipart():
            for part in msg.walk():
                content_type = part.get_content_type()
                content_disposition = str(part.get("Content-Disposition"))

                if "attachment" not in content_disposition:
                    if content_type == "text/plain":
                        return part.get_payload(decode=True).decode("utf-8")
                    elif content_type == "text/html":
                        return part.get_payload(decode=True).decode("utf-8")
        else:
            return msg.get_payload(decode=True).decode("utf-8")
        return ""

    def _format_email_content(self, subject, sender, date, body, format_type):
        """根据指定格式格式化邮件内容"""
        if format_type == "markdown":
            return (
                f"## {subject}\n\n**发件人: ** {sender}\n\n"
                f"**日期: ** {date}\n\n{body}\n\n---\n"
            )
        elif format_type == "html":
            return (
                f"<h2>{subject}</h2><p><strong>发件人: </strong> {sender}</p>"
                f"<p><strong>日期: </strong> {date}</p><div>{body}</div><hr>"
            )
        else:  # txt
            return (
                f"主题: {subject}\n发件人: {sender}\n日期: {date}\n\n" f"{body}\n\n{'-'*50}\n"
            )

    def _merge_emails(self, emails_content, format_type):
        """合并所有邮件内容"""
        if format_type == "markdown":
            return f"# QQ邮箱邮件汇总 ({date.today().strftime('%Y-%m-%d')})\n\n" + "\n".join(
                emails_content
            )
        elif format_type == "html":
            return f"<h1>QQ邮箱邮件汇总 ({date.today().strftime('%Y-%m-%d')})</h1>" + "".join(
                emails_content
            )
        else:  # txt
            return f"QQ邮箱邮件汇总 ({date.today().strftime('%Y-%m-%d')})\n\n" + "\n".join(
                emails_content
            )
