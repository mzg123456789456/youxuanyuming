import requests
from bs4 import BeautifulSoup
import re
import logging

# 设置日志记录
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 目标URL列表
urls = [
     'https://ip.164746.xyz',
    'https://api.uouin.com/cloudflare.html',
    'https://ip.164746.xyz/ipTop.html',
    'https://ip.164746.xyz/ipTop10.html',
    'https://raw.githubusercontent.com/tianshipapa/cfipcaiji/refs/heads/main/ip.txt',
    'https://addressesapi.090227.xyz/CloudFlareYes',
    'https://addressesapi.090227.xyz/ip.164746.xyz',
    'https://ipdb.api.030101.xyz/?type=bestcf&country=true',
    'https://ipdb.030101.xyz/api/bestcf.txt'
]    # 'https://cf.090227.xyz',

# 预编译正则表达式匹配IP地址
ip_pattern = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')

# 提取IP地址
def extract_ips_from_url(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # 直接从网页中匹配IP地址
        ip_matches = set()
        elements = soup.find_all(text=ip_pattern)
        for element in elements:
            ip_matches.update(ip_pattern.findall(element))

        if ip_matches:
            logging.info(f"从 {url} 提取到 {len(ip_matches)} 个唯一IP")
            return ip_matches
        else:
            logging.info(f"未找到IP地址：{url}")
            return set()
    except requests.exceptions.RequestException as e:
        logging.error(f"请求失败 {url}: {e}")
        return set()

# 主程序
def main():
    ip_addresses = set()
    for url in urls:
        ip_addresses.update(extract_ips_from_url(url))

    if ip_addresses:
        with open('ip.txt', 'w') as file:
            for ip in ip_addresses:
                country = get_ip_country(ip)
                file.write(f"{ip}#{country}\n")
        logging.info("IP地址已保存到 ip.txt 文件中。")
    else:
        logging.info("没有提取到任何IP地址。")

if __name__ == "__main__":
    main()
