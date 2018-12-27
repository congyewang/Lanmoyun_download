import requests
from lxml import etree
import re
import difflib
from fake_useragent import UserAgent


class Toolbox:

    def __init__(self, username: str, password: str, url: str, cookies=None):
        self.login_url = 'https://www.mosoteach.cn/web/index.php?c=passport&m=account_login'
        self.url = url
        self.username = username
        self.password = password
        self.s = requests.Session()
        self.headers = {
            'Host': 'www.mosoteach.cn',
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': UserAgent().random,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9'
        }
        self.cookies = cookies

    def login(self):
        data = {
            "account_name": self.username,
            "user_pwd":  self.password,
            "remember_me": "N"
        }
        sess = self.s.post(url=self.login_url, data=data,
                           headers=self.headers, timeout=500)
        return dict(sess.cookies)

    def get_url(self, path: str, title: str) ->list:
        clazz_course_id = re.search('(clazz_course_id=).+', self.url).group().replace(
            'clazz_course_id=', '')
        r = requests.get(
            self.url,
            headers=self.headers,
            cookies=self.cookies,
            timeout=500)
        html = etree.HTML(r.text)
        data_id = html.xpath(path)
        tit = html.xpath(title)
        links = [f'https://www.mosoteach.cn/web/index.php?c=interaction_quiz&m=person_quiz_result&clazz_course_id={clazz_course_id}&id={i}&order_item=group&user_id=F3E8D24D-A848-11E7-AA22-7CD30AD36C02'
                 for i in data_id]

        return links, tit

    def get_data(self, url: str, path: str) ->list:
        r = requests.get(
            url,
            headers=self.headers,
            cookies=self.cookies,
            timeout=500)
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
        r = requests.get(
            url,
            headers=self.headers,
            cookies=self.cookies,
            timeout=500)
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

    def check_diff(n1: str, n2: str, choose='txt') -> str:
        with open(n1, 'r') as f1:
            s1 = f1.read()
        with open(n2, 'r') as f2:
            s2 = f2.read()
        text1_line = s1.splitlines()
        text2_line = s2.splitlines()
        if choose == 'txt':
            d = difflib.Differ()
            a = d.compare(text1_line, text2_line)
            a = list(a)
            with open(f"diff.txt", "w+") as f:
                f.write('\n'.join(list(a)))
        elif choose == 'html':
            d = difflib.HtmlDiff()
            with open('diff.html', 'w+') as f:
                f.write(d.make_file(text1_line, text2_line))
        else:
            print('choose value error, input "txt" or "html"')
