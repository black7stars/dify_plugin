# QQ邮箱爬虫插件

## 项目介绍

这是一个Dify平台的QQ邮箱爬虫插件，可以爬取指定文件夹中的当日邮件并合并为文档输出。

## 项目结构

```
src/
├── dify_plugin/           # Dify插件主目录
│   ├── provider/          # Provider配置和实现
│   ├── tools/             # Tool配置和实现
│   ├── _assets/           # 插件资源文件
│   ├── manifest.yaml      # 插件元信息
│   ├── PRIVACY.md         # 隐私政策
│   ├── README.md          # 插件说明
│   ├── USAGE.md           # 使用说明
│   ├── __init__.py        # Python包初始化文件
│   ├── main.py            # 插件主入口
│   └── build_plugin.py    # 插件打包脚本
├── crawler.py             # 原始爬虫文件（空）
└── test_crawler.py        # 测试脚本
```

## 功能特性

- 爬取QQ邮箱指定文件夹中的当日邮件
- 支持多种输出格式（Markdown、HTML、TXT）
- 安全的凭证管理
- 符合Dify插件规范

## 安装依赖

```bash
pip install -r requirements.txt
```

## 打包插件

```bash
python src/dify_plugin/build_plugin.py
```

打包后的插件文件位于：`src/dify_plugin/build/qq_email_crawler.difypkg`

## 使用说明

1. 获取QQ邮箱IMAP授权码
2. 在Dify平台中安装插件包
3. 配置邮箱凭证
4. 在工作流中使用"Crawl QQ Emails"工具

详细使用说明请查看 [USAGE.md](src/dify_plugin/USAGE.md)

## 安全说明

- 插件通过Dify平台的安全机制管理凭证
- 所有数据处理均在本地环境中进行
- 不会存储或传输您的邮箱数据

## 开发说明

- Provider实现：`src/dify_plugin/provider/qq_email.py`
- Tool实现：`src/dify_plugin/tools/crawl_emails.py`
- 配置文件：对应的YAML文件
