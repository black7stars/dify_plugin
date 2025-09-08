#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
QQ邮箱爬虫插件打包脚本
"""

import os
import shutil
import zipfile
from pathlib import Path


def build_plugin():
    """打包插件"""
    print("开始打包QQ邮箱爬虫插件...")

    # 定义插件目录
    plugin_dir = Path(__file__).parent
    build_dir = plugin_dir / "build"

    # 创建build目录
    if build_dir.exists():
        shutil.rmtree(build_dir)
    build_dir.mkdir()

    # 创建插件包目录结构
    plugin_package_dir = build_dir / "qq_email_crawler"
    plugin_package_dir.mkdir()

    # 复制必要的文件和目录
    directories_to_copy = ["provider", "tools", "_assets"]
    files_to_copy = [
        "manifest.yaml",
        "PRIVACY.md",
        "README.md",
        "USAGE.md",
        "__init__.py",
        "main.py",
    ]

    for directory in directories_to_copy:
        src_dir = plugin_dir / directory
        dst_dir = plugin_package_dir / directory
        if src_dir.exists():
            shutil.copytree(src_dir, dst_dir)

    for file in files_to_copy:
        src_file = plugin_dir / file
        dst_file = plugin_package_dir / file
        if src_file.exists():
            shutil.copy2(src_file, dst_file)

    # 创建requirements.txt文件
    requirements_content = "dify_plugin\n"
    with open(plugin_package_dir / "requirements.txt", "w") as f:
        f.write(requirements_content)

    # 创建插件包
    plugin_zip = build_dir / "qq_email_crawler.difypkg"
    with zipfile.ZipFile(plugin_zip, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(plugin_package_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arc_path = os.path.relpath(file_path, build_dir)
                zipf.write(file_path, arc_path)

    print(f"插件打包完成: {plugin_zip}")
    print("插件已成功打包为.difypkg文件，可以在Dify平台中安装使用。")


if __name__ == "__main__":
    build_plugin()
