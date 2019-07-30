'''
实现具体的爬虫类
'''
# import time
# import random
import requests
import sys

sys.path.append('../')
# import re
# import js2py
from IPProxyPool.proxy_spider.base_spider import BaseSpider


class XiciSpider(BaseSpider):
    '''西刺代理爬虫	'''
    urls = ['http://www.xicidaili.com/nn/{}'.format(i) for i in range(1, 21)]

    group_xpath = '//*[@id="ip_list"]//tr[position()>1]'
    detail_xpath = {
        'ip': './td[2]/text()',
        'port': './td[3]/text()',
        'area': './td[4]/a/text()',
    }


class Ip3366Spider(BaseSpider):
    '''
    ip3366代理爬虫
    '''

    urls = ['http://www.ip3366.net/free/?stype={}&page={}'.format(i, j) for i in range(1, 4, 2) for j in range(1, 8)]

    group_xpath = '//*[@id="list"]/table/tbody/tr'
    detail_xpath = {
        'ip': './td[1]/text()',
        'port': './td[2]/text()',
        'area': './td[5]/text()',
    }


class kuaiSpider(BaseSpider):
    '''
    快代理爬虫
    '''

    urls = ['http://www.kuaidaili.com/free/in{}/{}'.format(i, j) for i in ['ha', 'tr'] for j in range(1, 21)]

    group_xpath = '//*[@id="list"]/table/tbody/tr'
    detail_xpath = {
        'ip': './td[1]/text()',
        'port': './td[2]/text()',
        'area': './td[5]/a/text()',
    }

    '''
    def get_page(self,url):
        #随机等待时间
        time.sleep(random.uniform(1,2))
        return super().get_page(url)
    '''


class Free89ipSpider(BaseSpider):
    '''
    89ip代理爬虫
    '''
    urls = ['http://www.89ip.cn/index{}.html'.format(i) for i in range(1, 17)]

    group_xpath = '//div[3]//table/tbody/tr'
    detail_xpath = {
        'ip': './td[1]/text()',
        'port': './td[2]/text()',
        'area': './td[3]/text()',
    }

    def get_page(self, url):
        return super().get_page(url).decode()

    def get_proxies(self):
        proxies = super().get_proxies()
        for item in proxies:
            item.ip = str(item.ip).replace("\n", "").replace("\t", "")
            item.area = str(item.area).replace("\n", "").replace("\t", "")
            item.port = str(item.port).replace("\n", "").replace("\t", "")
            # 返回Proxy对象
            yield item


if __name__ == '__main__':
    spider = Free89ipSpider()
    count = 0
    for proxy in spider.get_proxies():
        count += 1
        print(proxy)