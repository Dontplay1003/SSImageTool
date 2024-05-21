# <center>SSImageTool
<center> [English](README.md) | [简体中文](README_ZH.md) </center>

SSImageTool是一个简单的工具，用于处理图片使其可以被上传到steam的创意工坊展柜和艺术作品展柜。

## 它会做什么？
1. 如果图片的宽度小于630，将会调整图片的大小使其可以完全填充steam展柜
2. 如果要将图片放在steam的**创意工坊**展柜中，将会自动把图片切割成5个部分
3. 编辑图片的二进制文件结尾，使其可以被上传到steam

## 如何使用？
1. 下载最新的release
2. 解压文件
3. 将要处理的图片拖到`SSImageTool.exe`上并选择展柜的类型或者在命令行中输入`SSImageTool.exe [--output OUTPUT] [-a | -w] input
`

可选参数:
- `-o` 或 `--output` 指定输出目录
- `-h` 或 `--help` 显示帮助信息
- `-w` 或 `--workshop` 处理图片以适应steam创意工坊展柜
- `-a` 或 `--artwork` 处理图片以适应steam艺术作品展柜

## 许可证
MIT License