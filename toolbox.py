import requests
from lxml import etree
import re


class Toolbox:

    def __init__(self, url: str, headers: dict, cookies: dict):
        self.url = url
        self.headers = headers
        self.cookies = cookies

    def get_url(self, path: str, title: str) ->list:
        proxies = {"http": "http://127.0.0.1:1087",
                   "https": "https://127.0.0.1:1087",
                   }
        r = requests.get(
            self.url,
            headers=self.headers,
            cookies=self.cookies,
            proxies=proxies,
            timeout=200)
        html = etree.HTML(r.text)
        data_id = html.xpath(path)
        tit = html.xpath(title)
        links = [f'https://www.mosoteach.cn/web/index.php?c=interaction_quiz&m=person_quiz_result&clazz_course_id=01529E8B-A300-11E8-AA22-7CD30AD36C02&id={i}&order_item=group&user_id=F3E8D24D-A848-11E7-AA22-7CD30AD36C02'
                 for i in data_id]

        return links, tit

    def get_data(self, url: str, path: str) ->list:
        proxies = {"http": "http://127.0.0.1:1087",
                   "https": "https://127.0.0.1:1087",
                   }
        r = requests.get(
            url,
            headers=self.headers,
            cookies=self.cookies,
            proxies=proxies,
            timeout=200)
        html = etree.HTML(r.text)
        try:
            result = html.xpath(path)
        except Exception:
            result = None
        return result

    def sort_que(s: str, mat: str) ->str:
        pattern = re.compile(mat)
        m = pattern.finditer(s)
        old = []
        new = []
        for i in m:
            old.append(i.group())
            new.append('\n' + i.group())
        for j in range(len(old)):
            s = s.replace(old[j], new[j])
        return s

    def sort_ans(s: str, mat: str) ->str:
        pattern = re.compile(mat)
        m = pattern.finditer(s)
        old = []
        new = []
        for i in m:
            old.append(i.group())
            new.append(i.group() + '\n')
        for j in range(len(old)):
            s = s.replace(old[j], new[j])
        return s

    def get_txt(self, url: str) ->list:
        proxies = {"http": "http://127.0.0.1:1087",
                   "https": "https://127.0.0.1:1087",
                   }
        r = requests.get(
            url,
            headers=self.headers,
            cookies=self.cookies,
            proxies=proxies,
            timeout=200)
        html = etree.HTML(r.text)
        title = []
        ans_sum = []
        curr = []
        try:
            for i in range(len(html.xpath('/html/body/div[3]/div[2]/div[4]/div'))):
                title.append(html.xpath(f'/html/body/div[3]/div[2]/div[4]/div[{i + 1}]/div[1]/div/div[1]/div/div[3]/pre/text()'))
                ans = []
                for j in range(len(html.xpath(f'/html/body/div[3]/div[2]/div[4]/div[{i + 1}]/div[1]/div/div[3]/div'))):
                    ans.append(html.xpath(f'/html/body/div[3]/div[2]/div[4]/div[{i + 1}]/div[1]/div/div[3]/div[{j + 1}]/span[3]/text()'))
                ans_sum.append(ans)
                curr.append(html.xpath(f'/html/body/div[3]/div[2]/div[4]/div[{i + 1}]/div[2]/div[1]/div[1]/span/text()'))
        except Exception:
            pass
        return title, ans_sum, curr
