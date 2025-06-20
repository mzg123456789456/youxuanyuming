import socket
import os
import logging

# 设置日志记录
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 目标域名列表
domains = [
    'proxyip.fxxk.dedyn.io',
    'proxyip.us.fxxk.dedyn.io',
    'proxyip.sg.fxxk.dedyn.io',
    'proxyip.jp.fxxk.dedyn.io',
    'proxyip.hk.fxxk.dedyn.io',
    'proxyip.aliyun.fxxk.dedyn.io',
    'proxyip.oracle.fxxk.dedyn.io',
    'proxyip.digitalocean.fxxk.dedyn.io',
    'proxyip.oracle.cmliussss.net'
]

# 删除旧文件（如果存在）
if os.path.exists('proxyip.txt'):
    os.remove('proxyip.txt')

# 解析域名并保存IP
with open('proxyip.txt', 'w') as file:
    for domain in domains:
        try:
            # 获取域名对应的IP
            ip_address = socket.gethostbyname(domain)
            file.write(f'{ip_address}\n')  # 只写入IP
            logging.info(f'成功解析 {domain} -> {ip_address}')
        except socket.gaierror as e:
            logging.error(f'域名解析失败: {domain} - {str(e)}')

logging.info('所有域名解析完成，结果已保存到 proxyip.txt')
