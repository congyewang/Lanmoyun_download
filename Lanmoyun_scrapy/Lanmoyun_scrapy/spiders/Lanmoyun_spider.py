from scrapy.spiders import Spider
from Lanmoyun_scrapy.items import LanmoyunScrapyItem
# from lanmoyun_scra.spiders.toolbox import *


class LanmoyunSpider(Spider):

    name = 'Lanmoyun_scrapy'
    headers = {
            'Host': 'www.mosoteach.cn',
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9'
    }

    cookies = {'_uab_collina': '154280184098098822088961',
               'UM_distinctid': '165ea9955f7140-072e1f8bdbdb38-1130685c-fa000-165ea9955f8496',
               '_ga': 'GA1.2.432290112.1544065307',
               'CNZZDATA1253495893': '230301430-1537237385-https%253A%252F%252Fwww.google.com%252F%7C1545308245',
               'aliyungf_tc': 'AQAAADcdTxq9eQgAv7Mpb39/px3ta5gu',
               'mosoteach2': '118142e8d352a546e4baec54935aa2b58c1e99f9',
               'login_token': '7bdb40fd83f6e411295f2e58767b510788c1668992456f5a3bcf026dbfdbe5e1',
               'SERVERID': '85f2f94ec6c34af49bb881648f0847ac|1545308870|1545308839'
    }

    start_urls = [i.strip() for i in
                  open('todo_urls.txt').readlines()]



    def parse(self, response):
        item = LanmoyunScrapyItem()
        totels = response.xpath(r'/html/body/div[3]/div[2]/div[4]/div')
        try:
            for totel in totels:
                item['title'] = totel.xpath('./div[1]/div/div[1]/div/div[3]/pre/text()').extract()[0]
                item['curr'] = totel.xpath('./div[2]/div[1]/div[1]/span/text()').extract()[0]
                divs = totel.xpath('./div[1]/div/div[3]/div')
                for div in divs:
                    item['ans_sum'] = div.xpath('./span[3]/text()').extract()[0]
        except Exception:
            pass
        yield item
