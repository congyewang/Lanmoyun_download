from scrapy.spiders import Spider
from Lanmoyun_scrapy.items import LanmoyunScrapyItem


class LanmoyunSpider(Spider):

    name = 'Lanmoyun_scrapy'
    # headers = {
    #     'Host': 'www.mosoteach.cn',
    #     'Connection': 'keep-alive',
    #     'Cache-Control': 'max-age=0',
    #     'Upgrade-Insecure-Requests': '1',
    #     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
    #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    #     'Accept-Encoding': 'gzip, deflate, br',
    #     'Accept-Language': 'zh-CN,zh;q=0.9'}
    #
    # cookies = {
    #     '_uab_collina': '154280184098098822088961',
    #     'UM_distinctid': '165ea9955f7140-072e1f8bdbdb38-1130685c-fa000-165ea9955f8496',
    #     '_ga': 'GA1.2.432290112.1544065307',
    #     'CNZZDATA1253495893': '230301430-1537237385-https%253A%252F%252Fwww.google.com%252F%7C1546938426',
    #     'aliyungf_tc': 'AQAAAFkerBm/sggA9oGmezpKlyuZgbV4',
    #     'teachweb': '104e4f1fdc632ca2e959ea671cb622f2b6ad759f',
    #     'login_token': 'd4d07c7df1bfe49a1505aeca1907f8d73e36b5f3d7c69c671e5e97d9f2371d71',
    #     'SERVERID': '98b6fea346cee1806c7dd0d9feae3405|1550991439|1550991405'}

    start_urls = [i.strip() for i in
                  open('todo_urls.txt').readlines()]

    def parse(self, response):
        # 控制台调试
        # from scrapy.shell import inspect_response
        # inspect_response(response, self)
        # 实例化容器
        item = LanmoyunScrapyItem()
        # 获取总数
        txt = response.xpath('//div[@class="view-quiz-row"]')
        # 读取每题位置
        for i in range(len(txt)):
            title = txt[i].xpath(
                './/pre[@class="color-33 topic-subject"]/text()').extract()

            curr = txt[i].xpath(
                './/div[@class="true-rate"]//span[@style="color:#07AC6C;"]/text()'
            ).extract()
            # 读取各选项
            ans_sum = txt[i].xpath('.//span[@class="person-result-answer"]/text()').extract()
            item['title'] = title
            item['ans_sum'] = ans_sum
            item['curr'] = curr
            yield item
