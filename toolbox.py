import requests
from lxml import etree


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
        links = [f'https://www.mosoteach.cn/web/index.php?c=interaction_quiz&m=person_quiz_result&clazz_course_id=0D5BF5CA-EBF3-11E8-832A-EC0D9ACEE976&id={i}&order_item=group&user_id=F3E8D24D-A848-11E7-AA22-7CD30AD36C02'
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
