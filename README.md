# <center>SSImageTool
<center> [English](README.md) | [简体中文](README_ZH.md) </center>

SSImageTool is a simple tool to process the image to fit steam showcase.

## what will it do?
1. Resize the image if its width can't completely fill the steam showcase (width<=630)
2. Cut the image into 5 parts if to use it in steam **workshop** showcase
3. Edit the binary file of the image to make it can be uploaded to steam

## How to use?
1. Download the latest release
2. Unzip the file
3. Drag the image you want to process to the exe file and choose the type of the showcase or input `SSImageTool.exe [--output OUTPUT] [-a | -w] input` in the command line

Optional arguments:
- `-o` or `--output` to specify the output directory
- `-h` or `--help` to show the help message
- `-w` or `--workshop` to process the image for steam workshop showcase
- `-a` or `--artwork` to process the image for steam artwork showcase

## Other
I'm a little busy recently, so this tools may not that perfect. If you have any problem, please open an issue.

## License
MIT License