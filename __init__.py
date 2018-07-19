import requests
from lxml import etree
from links import *
import time
import tqdm
import random
'''
@author=Congye.Wang
07/10/2018
爬取蓝墨云文档以txt存储，links类用来获取爬取网址及题目数量
links，headers，cookies填写根网页信息
请自行替换links，cookies等信息
若超时请及时替换cookies
'''

# 爬取根网页的url及题目数量
links = r'https://www.mosoteach.cn/web/index.php?c=interaction&m=index&clazz_course_id=D654668D-8B2C-11E7-8560-7CD30ABC9F86'
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'referer': 'https://www.mosoteach.cn/web/index.php?c=interaction&m=index&clazz_course_id=D654668D-8B2C-11E7-8560-7CD30ABC9F86',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
cookies = {
    'UM_distinctid': '16446ac2f881ea-01fc111e7df84-16386952-fa000-16446ac2f8996a',
    'login_token': 'ea55988e89318a5f5daa921c694b694c16055087663d5f488e76390e27cc4aae',
    'CNZZDATA1253495893': '977897281-1514085120-https%253A%252F%252Fwww.baidu.com%252F%7C1531996710',
    'mosoteach2': '69bfd7a8eb0c9284c817c3531d98b402e76c3f73',
    'SERVERID': '68f66c39de4d86bde6b178dda9174eb6|1531997878|1531997769'}
lanmo_id_num = Links(links, headers, cookies)
totol_urls = lanmo_id_num.get_url()
urls = []
exam_num = []
for i in tqdm.trange(len(totol_urls[0])):
    id = totol_urls[0][i][0]
    urls.append(
        'https://www.mosoteach.cn/web/index.php?c=interaction_quiz&m=person_quiz_result&clazz_course_id=D654668D-8B2C-11E7-8560-7CD30ABC9F86&id=' +
        id +
        '&order_item=group&user_id=F3E8D24D-A848-11E7-AA22-7CD30AD36C02')
    exam_num.append(totol_urls[1][i][0])

# 爬取题目并存为list，存在报错信息为讨论或头脑风暴等页面，用pass跳过
for j in tqdm.trange(len(urls)):
    url = urls[j]
    r = requests.get(url, headers=headers, cookies=cookies, timeout=5000)
    html = etree.HTML(r.text)
    title_list = []
    A = []
    B = []
    C = []
    D = []
    D = []
    E = []
    Currect = []
    time.sleep(random.randint(2, 5))
    try:
        for i in range(1, int(exam_num[j]) + 1):
            title_list.append(
                html.xpath(
                    r'//*[@id="cc-main"]/div[2]/div[4]/div[' +
                    str(i) +
                    ']/div[1]/div/div[1]/div/div[3]/pre/text()'))
            A.append(
                html.xpath(
                    r'//*[@id="cc-main"]/div[2]/div[4]/div[' +
                    str(i) +
                    ']/div[1]/div/div[3]/div[1]/span[3]/text()'))
            B.append(
                html.xpath(
                    r'//*[@id="cc-main"]/div[2]/div[4]/div[' +
                    str(i) +
                    ']/div[1]/div/div[3]/div[2]/span[3]/text()'))
            C.append(
                html.xpath(
                    r'//*[@id="cc-main"]/div[2]/div[4]/div[' +
                    str(i) +
                    ']/div[1]/div/div[3]/div[3]/span[3]/text()'))
            D.append(
                html.xpath(
                    r'//*[@id="cc-main"]/div[2]/div[4]/div[' +
                    str(i) +
                    ']/div[1]/div/div[3]/div[4]/span[3]/text()'))
            E.append(
                html.xpath(
                    r'//*[@id="cc-main"]/div[2]/div[4]/div[' +
                    str(i) +
                    ']/div[1]/div/div[3]/div[5]/span[3]/text()'))
            Currect.append(
                html.xpath(
                    '//*[@id="cc-main"]/div[2]/div[4]/div[' +
                    str(i) +
                    ']/div[2]/div[1]/div[1]/span/text()'))
    except Exception:
        pass


# 从list中按顺序取出题目、选项和答案，存在报错信息为讨论或头脑风暴等页面，用pass跳过
with open('Exam.txt', 'a+', encoding='utf-8') as f:
    try:
        for k in tqdm.trange(int(exam_num[j])):
            f.write(str(k +
                        1) +
                    '\n' +
                    title_list[k][0] +
                    '\n' +
                    'A.' +
                    str(A[k]) +
                    '\n' +
                    'B.' +
                    str(B[k]) +
                    '\n' +
                    'C.' +
                    str(C[k]) +
                    '\n' +
                    'D.' +
                    str(D[k]) +
                    '\n' +
                    'E.' +
                    str(E[k]) +
                    '\n' +
                    str(Currect[k]) +
                    '\n\n')
            f.close()
    except Exception:
        pass
