import requests
import re
import logging
from typing import List

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('crawler.log'), logging.StreamHandler()]
)


class DouyinCrawler:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0',
            'Referer': 'https://www.douyin.com/',
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)

    def extract_video_urls(self, html: str) -> List[str]:
        """改进后的链接提取方法"""
        # 匹配抖音新版视频URL模式
        patterns = [
            r'"playAddr":\s*"([^"]+)"',  # JSON格式
            r'src="(https://[^"]+\.mp4(?=\?))',  # 直接链接
            r'https://v3-web\.douyinvod\.com/[^\s]+'  # 兜底匹配
        ]

        urls = []
        for pattern in patterns:
            found = re.findall(pattern, html)
            urls.extend([url.replace('\\u002F', '/') for url in found])

        # 去重处理
        return list(set(urls))

    def get_real_video_url(self, page_url: str) -> List[str]:
        """获取真实视频地址"""
        try:
            # 第一步：获取页面内容
            response = self.session.get(page_url)
            response.raise_for_status()

            # 第二步：提取潜在视频链接
            provisional_urls = self.extract_video_urls(response.text)

            # 第三步：验证链接有效性
            valid_urls = []
            for url in provisional_urls:
                if self.validate_url(url):
                    valid_urls.append(url)
                    logging.info(f"验证通过: {url}")

            return valid_urls

        except requests.RequestException as e:
            logging.error(f"请求异常: {str(e)}")
            return []

    def validate_url(self, url: str) -> bool:
        """验证URL有效性"""
        try:
            head = self.session.head(url, timeout=5)
            if head.status_code == 200:
                content_type = head.headers.get('Content-Type', '')
                return 'video' in content_type
            return False
        except Exception:
            return False

    def download_video(self, url: str, filename: str = "video.mp4") -> bool:
        """增强型下载方法"""
        try:
            with self.session.get(url, stream=True, timeout=10) as res:
                res.raise_for_status()
                with open(filename, 'wb') as f:
                    for chunk in res.iter_content(chunk_size=1024 * 1024):  # 1MB chunks
                        if chunk:
                            f.write(chunk)
                logging.info(f"视频下载完成: {filename}")
                return True
        except Exception as e:
            logging.error(f"下载失败: {str(e)}")
            return False


if __name__ == "__main__":
    # 使用示例
    crawler = DouyinCrawler()

    # 测试你提供的URL列表
    test_urls = [""
    ""
    ""
      ]

    # 批量处理URL
    for idx, url in enumerate(test_urls):
        if crawler.validate_url(url):
            filename = f"douyin_video_{idx + 1}.mp4"
            if crawler.download_video(url, filename):
                logging.info(f"成功下载第 {idx + 1} 个视频")
            else:
                logging.warning(f"第 {idx + 1} 个视频下载失败")
        else:
            logging.warning(f"无效URL: {url}")