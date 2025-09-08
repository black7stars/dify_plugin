# QQ邮箱爬虫插件

## 插件介绍

QQ邮箱爬虫插件是一个Dify工具插件，可以帮助您从QQ邮箱中爬取指定文件夹的当日邮件，并将它们合并为一个文档输出。支持多种输出格式，包括Markdown、HTML和纯文本。

## 功能特性

- 爬取QQ邮箱指定文件夹中的当日邮件
- 支持多种输出格式（Markdown、HTML、TXT）
- 安全的凭证管理
- 符合Dify插件规范

## 安装与配置

1. 在Dify平台中安装此插件
2. 配置QQ邮箱凭证：
   - 邮箱地址：您的QQ邮箱地址
   - 授权码：QQ邮箱的IMAP授权码（非密码）
3. 在工作流中使用"Crawl QQ Emails"工具

## 使用说明

在Dify工作流中添加"Crawl QQ Emails"工具节点，配置以下参数：

- Folder Name：要爬取的邮件文件夹名称（如INBOX表示收件箱）
- Output Format：输出文档格式（可选，支持markdown、html、txt，默认为markdown）

## 安全说明

- 插件通过Dify平台的安全机制管理凭证
- 所有数据处理均在本地环境中进行
- 不会存储或传输您的邮箱数据

## 获取QQ邮箱授权码

1. 登录QQ邮箱
2. 进入"设置"->"账户"
3. 找到"POP3/SMTP服务"和"IMAP/SMTP服务"
4. 开启IMAP/SMTP服务
5. 按提示发送短信获取授权码
