import requests
from lxml import etree
import re
'''
@author=CongyeWang
07/10/2018
爬取蓝墨云文档以txt存储，links类用来获取爬取网址及题目数量
links，headers，cookies填写根网页信息

此类库依赖requests库、xpath解析及正则表达式爬取url，类似于url管理器
'''
class Links:

    def __init__(self, links, headers, cookies):
        self.links = links
        self.headers = headers
        self.cookies = cookies

    def get_url(self):
        r = requests.get(
            self.links,
            headers=self.headers,
            cookies=self.cookies,
            timeout=5000)
        html = etree.HTML(r.text)
        id_num = str(
            html.xpath('//*[@id="interaction-list-box"]/div[1]/div[1]/span[2]/text()')[0])
        num = int(re.search(r'\d+', id_num).group()) + 1
        data_id = [
            html.xpath(
                '//*[@id="interaction-list-box"]/div[1]/div[2]/div[' +
                str(i) +
                ']/@data-id') for i in range(
                1,
                num)]
        que_number = [
            html.xpath(
                '//*[@id="interaction-list-box"]/div[1]/div[2]/div[' +
                str(j) +
                ']/div/div[3]/div[1]/span[2]/text()') for j in range(
                1,
                num)]
        return data_id, que_number
