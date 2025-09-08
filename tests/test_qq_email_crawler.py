#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
QQ邮箱爬虫插件测试
"""

import os
import unittest


class TestQQEmailCrawler(unittest.TestCase):
    """QQ邮箱爬虫插件测试类"""

    def test_plugin_structure(self):
        """测试插件目录结构"""
        # 检查必要的目录和文件是否存在
        plugin_dir = os.path.join(os.path.dirname(__file__), "..", "src", "dify_plugin")

        # 检查provider目录
        provider_dir = os.path.join(plugin_dir, "provider")
        self.assertTrue(os.path.exists(provider_dir))

        # 检查tools目录
        tools_dir = os.path.join(plugin_dir, "tools")
        self.assertTrue(os.path.exists(tools_dir))

        # 检查必要的配置文件
        manifest_file = os.path.join(plugin_dir, "manifest.yaml")
        self.assertTrue(os.path.exists(manifest_file))

        privacy_file = os.path.join(plugin_dir, "PRIVACY.md")
        self.assertTrue(os.path.exists(privacy_file))

        readme_file = os.path.join(plugin_dir, "README.md")
        self.assertTrue(os.path.exists(readme_file))

        # 检查Provider配置文件
        provider_yaml = os.path.join(provider_dir, "qq_email.yaml")
        self.assertTrue(os.path.exists(provider_yaml))

        # 检查Provider实现文件
        provider_py = os.path.join(provider_dir, "qq_email.py")
        self.assertTrue(os.path.exists(provider_py))

        # 检查Tool配置文件
        tool_yaml = os.path.join(tools_dir, "crawl_emails.yaml")
        self.assertTrue(os.path.exists(tool_yaml))

        # 检查Tool实现文件
        tool_py = os.path.join(tools_dir, "crawl_emails.py")
        self.assertTrue(os.path.exists(tool_py))


if __name__ == "__main__":
    unittest.main()
