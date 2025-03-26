#Bilibili Video Downloader#
Introduction
This script is designed to download videos and their corresponding audio from Bilibili and then merge them into a complete video file.

Features
Download video and audio separately from Bilibili
Merge the downloaded video and audio into a complete video file
Simple and straightforward implementation

Requirements
Python 3.8
requests
moviepy

Installation
Ensure you have Python 3.6+ installed
Install the required dependencies:
bash
pip install requests moviepy
Usage
Save the script as bilibili_downloader.py
Run the script:
bash
python bilibili_downloader.py
The downloaded video will be saved as 完整.mp4

Notes
Ensure you have a stable internet connection
Be aware of Bilibili's terms of service and download responsibly
If you encounter issues with downloading videos, check the script for any error messages



#Douyin Video Crawler#
Introduction
This script is designed to crawl and download videos from Douyin (TikTok). It extracts video URLs from a given page and downloads them.

Features
Extract video URLs from Douyin pages
Validate and download multiple videos
Comprehensive logging for tracking

Requirements
Python 3.8
requests
Installation
Ensure you have Python 3.6+ installed
Install the required dependencies:

bash
pip install requests

Usage
Save the script as douyin_crawler.py
Run the script:
bash
python douyin_crawler.py
Check the generated crawler.log file for download status
Downloaded videos will be saved as douyin_video_1.mp4, douyin_video_2.mp4, etc.

Notes
Ensure you have a stable internet connection
Be aware of Douyin's terms of service and crawl responsibly
If you encounter issues with downloading videos, check the log file for details


# 抖音和Bilibili视频爬取脚本使用指南
## 总说明
这两个爬取脚本都需要通过浏览器开发者工具获取视频的URL。以下是详细的操作步骤：
### 对于抖音爬取脚本：

1. 打开抖音网页版，找到你想要下载的视频页面。
2. 打开浏览器的开发者工具（通常可以通过右键点击页面，选择“检查”或按F12键）。
3. 切换到“网络”选项卡，这里会显示页面加载的所有资源。
4. 播放视频，这时网络选项卡会显示新的请求。
5. 查找包含视频文件的请求，通常可以通过筛选.mp4扩展名来快速定位。
6. 找到视频的请求后，右键点击该请求并选择“复制”->“请求链接”。
7. 将复制的链接替换到抖音爬取脚本中的相应位置。

### 对于Bilibili爬取脚本：

1. 打开Bilibili网站，找到你想要下载的视频页面。
2. 打开浏览器的开发者工具（通常可以通过右键点击页面，选择“检查”或按F12键）。
3. 切换到“网络”选项卡，这里会显示页面加载的所有资源。
4. 播放视频，这时网络选项卡会显示新的请求。
5. 查找包含视频和音频文件的请求，通常可以通过筛选.m4s扩展名来快速定位。
6. 找到视频和音频的请求后，右键点击每个请求并选择“复制”->“请求链接”。
7. 将复制的链接分别替换到Bilibili爬取脚本中的相应位置。

### 注意事项：

- 确保你复制的URL是正确的，并且可以直接访问。
- 如果视频加载较慢，可能需要等待一段时间，让网络请求完全加载。
- 如果遇到反爬虫机制，可能需要添加请求头（如User-Agent和Referer）来模拟正常浏览器请求。
- 如果视频有加密或需要登录才能访问，直接复制URL可能无法下载，需要进一步处理。

## 获取URL的过程总结

1. 打开目标视频页面。
2. 使用浏览器开发者工具查看网络请求。
3. 找到并复制视频（和音频）的URL。
4. 将URL替换到爬取脚本中。
5. 运行脚本下载视频。

通过以上步骤，你可以成功获取抖音和Bilibili视频的URL，并使用爬取脚本下载视频。