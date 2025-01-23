import os

def setup_proxy():
    # Указываем прокси для HTTP и HTTPS
    os.environ['http_proxy'] = 'http://user:password@proxy_ip:port'
    os.environ['https_proxy'] = 'http://user:password@proxy_ip:port'

if __name__ == '__main__':
    setup_proxy()