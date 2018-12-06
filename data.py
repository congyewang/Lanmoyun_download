from toolbox import *
import time
import tqdm


if __name__ == '__main__':

    # 爬取根网页的url及题目数量

    url = r'https://www.mosoteach.cn/web/index.php?c=interaction&m=index&clazz_course_id=0D5BF5CA-EBF3-11E8-832A-EC0D9ACEE976'
    headers = {
        'Host': 'www.mosoteach.cn',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9'}
    cookies = {'_uab_collina': '154280184098098822088961',
               'UM_distinctid': '165ea9955f7140-072e1f8bdbdb38-1130685c-fa000-165ea9955f8496',
               '_ga': 'GA1.2.432290112.1544065307',
               '_gid': 'GA1.2.1771914764.1544065307',
               'login_token': 'afe24a33894baf331bf42b6e5f7aad597072260c6d3da353ba975b4e20116e2c',
               'CNZZDATA1253495893': '230301430-1537237385-https%253A%252F%252Fwww.google.com%252F%7C1544091625',
               'aliyungf_tc': 'AQAAANJrvBWghAQAykk6AZ+ihx+bqppZ',
               'mosoteach2': '3e86b3888f45b312601175cf413a86acd0854843',
               'SERVERID': '68f66c39de4d86bde6b178dda9174eb6|1544092697|1544092689'}
    path = '//*[@class="interaction-row"]/@data-id'
    tit = '//*[@class="interaction-row"]//@title'
    que_path = '//*[@class="row-center"]//text()'
    ans_path = '//*[@class="true-rate"]//text()'

    # 爬取根网页的url及测试名称
    fin_man = Toolbox(url, headers, cookies)
    urls, title = fin_man.get_url(path, tit)
    # 爬取题目并保存在data文件夹下
    for i in tqdm.trange(len(urls)):
        que = fin_man.get_data(urls[i], que_path)
        que_str = ''.join(que).replace(' ', '').replace('\n\n', '')
        ans = fin_man.get_data(urls[i], ans_path)
        ans_str = ''.join(ans).replace(' ', '').replace('\n\n', '')
        with open(f'data/{title[i]}.txt', 'w+') as f:
            f.write(que_str)
        with open(f'data/{title[i]}_answer.txt', 'w+') as f:
            f.write(ans_str)
        # time.sleep(2)
