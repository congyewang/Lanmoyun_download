import os
import requests
from lxml import etree
import re
import difflib
import time


class RunSpiders:
    def RunCommand(self, spider):
        os.system(f"scrapy crawl {spider}")


class Toolbox:
    def __init__(self, url: str, headers: dict, cookies: dict):
        self.url = url
        self.headers = headers
        self.cookies = cookies

    def get_url(self, path: str) ->list:
        clazz_course_id = re.search(
            '(clazz_course_id=).+', self.url).group().replace('clazz_course_id=', '')
        proxies = {"http": "http://127.0.0.1:1080",
                   "https": "https://127.0.0.1:1080",
                   }
        r = requests.get(
            self.url,
            headers=self.headers,
            cookies=self.cookies,
            proxies=proxies,
            timeout=500)
        html = etree.HTML(r.text)
        data_id = html.xpath(path)
        links = [f'https://www.mosoteach.cn/web/index.php?c=interaction_quiz&m=person_quiz_result&clazz_course_id={clazz_course_id}&id={i}&order_item=group&user_id=F3E8D24D-A848-11E7-AA22-7CD30AD36C02'
                 for i in data_id]

        return links

    def get_data(self, url: str, path: str) ->list:
        proxies = {"http": "http://127.0.0.1:1080",
                   "https": "https://127.0.0.1:1080",
                   }
        r = requests.get(
            url,
            headers=self.headers,
            cookies=self.cookies,
            proxies=proxies,
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
        proxies = {"http": "http://127.0.0.1:1080",
                   "https": "https://127.0.0.1:1080",
                   }
        r = requests.get(
            url,
            headers=self.headers,
            cookies=self.cookies,
            proxies=proxies,
            timeout=500)
        html = etree.HTML(r.text)
        title = []
        ans_sum = []
        curr = []
        try:
            for i in range(
                    len(html.xpath('/html/body/div[3]/div[2]/div[4]/div'))):
                title.append(html.xpath(
                    f'/html/body/div[3]/div[2]/div[4]/div[{i + 1}]/div[1]/div/div[1]/div/div[3]/pre/text()'))
                ans = []
                for j in range(len(html.xpath(
                        f'/html/body/div[3]/div[2]/div[4]/div[{i + 1}]/div[1]/div/div[3]/div'))):
                    ans.append(html.xpath(
                        f'/html/body/div[3]/div[2]/div[4]/div[{i + 1}]/div[1]/div/div[3]/div[{j + 1}]/span[3]/text()'))
                ans_sum.append(ans)
                curr.append(html.xpath(
                    f'/html/body/div[3]/div[2]/div[4]/div[{i + 1}]/div[2]/div[1]/div[1]/span/text()'))
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


if __name__ == '__main__':
    tic = time.time()
    url = 'https://www.mosoteach.cn/web/index.php?c=interaction&m=index&clazz_course_id=0D5BF5CA-EBF3-11E8-832A-EC0D9ACEE976'
    headers = {
        'Host': 'www.mosoteach.cn',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9'}

    cookies = {
        '_uab_collina': '154280184098098822088961',
        'UM_distinctid': '165ea9955f7140-072e1f8bdbdb38-1130685c-fa000-165ea9955f8496',
        '_ga': 'GA1.2.432290112.1544065307',
        'CNZZDATA1253495893': '230301430-1537237385-https%253A%252F%252Fwww.google.com%252F%7C1545308245',
        'aliyungf_tc': 'AQAAADcdTxq9eQgAv7Mpb39/px3ta5gu',
        'mosoteach2': '118142e8d352a546e4baec54935aa2b58c1e99f9',
        'login_token': '7bdb40fd83f6e411295f2e58767b510788c1668992456f5a3bcf026dbfdbe5e1',
        'SERVERID': '85f2f94ec6c34af49bb881648f0847ac|1545308870|1545308839'}
    path = '//*[@class="interaction-row"]/@data-id'
    todo_urls = Toolbox(url, headers, cookies)
    urls = todo_urls.get_url(path)
    with open('todo_urls.txt', 'w+') as f:
        f.write('\n'.join(urls))

    _run = RunSpiders()
    _run.RunCommand('Lanmoyun_scrapy')
    toc = time.time()
    print(f'time: {toc - tic}s')
