import requests
from lxml import etree
import re


class Toolbox:

    def __init__(self, username: str, password: str, url: str):
        self.url = url
        self.username = username
        self.password = password
        self.s = requests.Session()
        self.headers = {
            'Host': 'www.mosoteach.cn',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1500.55 Safari/537.36'
        }

    def login(self) -> dict:
        '''
        To login and save the session before the next step which is to get urls.
        return: To show the Status Code of this url. See details "https://www.restapitutorial.com/httpstatuscodes.html"
        '''
        login_url = "https://www.mosoteach.cn/web/index.php?c=passport&m=account_login"
        data = {
            "account_name": self.username,
            "user_pwd":  self.password,
            "remember_me": "N"
        }
        sess = self.s.post(url=login_url, data=data,
                           headers=self.headers, timeout=500)
        return sess.json()

    def get_url(self) -> list:
        path = '//*[@class="interaction-row"]/@data-id'
        title = '//*[@class="interaction-row"]//@title'
        clazz_course_id = re.search('(clazz_course_id=).+', self.url).group().replace(
            'clazz_course_id=', '')
        r = self.s.get(
            self.url,
            headers=self.headers,
            timeout=500)
        html = etree.HTML(r.text)
        data_id = html.xpath(path)
        tit = html.xpath(title)
        links = [f'https://www.mosoteach.cn/web/index.php?c=interaction_quiz&m=person_quiz_result&clazz_course_id={clazz_course_id}&id={i}&order_item=group&user_id=F3E8D24D-A848-11E7-AA22-7CD30AD36C02'
                 for i in data_id]

        return links, tit

    def get_data(self, url: str) -> list:
        r = self.s.get(
            url,
            headers=self.headers,
            timeout=500)
        html = etree.HTML(r.text)
        title = []
        ans_sum = []
        curr = []
        try:
            for i in range(len(html.xpath('/html/body/div[3]/div[2]/div[4]/div'))):
                title.append(html.xpath(
                    f'/html/body/div[3]/div[2]/div[4]/div[{i + 1}]/div[1]/div/div[1]/div/div[3]/pre/text()'))
                ans = []
                for j in range(len(html.xpath(f'/html/body/div[3]/div[2]/div[4]/div[{i + 1}]/div[1]/div/div[3]/div'))):
                    ans.append(html.xpath(
                        f'/html/body/div[3]/div[2]/div[4]/div[{i + 1}]/div[1]/div/div[3]/div[{j + 1}]/span[3]/text()'))
                ans_sum.append(ans)
                curr.append(html.xpath(
                    f'/html/body/div[3]/div[2]/div[4]/div[{i + 1}]/div[2]/div[1]/div[1]/span/text()'))
        except Exception:
            pass
        return title, ans_sum, curr
