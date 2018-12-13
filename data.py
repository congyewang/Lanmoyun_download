from toolbox import *
import time
import tqdm


if __name__ == '__main__':

    # 爬取根网页的url及题目数量

    url = r'https://www.mosoteach.cn/web/index.php?c=interaction&m=index&clazz_course_id=01529E8B-A300-11E8-AA22-7CD30AD36C02'
    headers = {
        'Host': 'www.mosoteach.cn',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9'}
    cookies = {'_uab_collina': '154460537297751233510614',
               'aliyungf_tc': 'AQAAABBvoXgpDg4AQrMpb9GZSayPZ0u6',
               'CNZZDATA1253495893': '1065823389-1544604378-https%3A%2F%2Fwww.baidu.com%2F|1544705080',
               'login_token': '32430788bb9661a458010be79e58f530451e362c44d18e2e9221e07819169427',
               'mosoteach2': '39dfe58758d13cf1dade40288fd0885e88564009',
               'SERVERID': 'd497d74f17ca4f67d620e473cb67dd68|1544717996|1544717879',
               'UM_distinctid': '167a1a77569449-0551ed561d506e-4a506d-fa000-167a1a7756b538'}
    path = '//*[@class="interaction-row"]/@data-id'
    tit = '//*[@class="interaction-row"]//@title'

    intab = '/'
    outtab = '_'
    trantab = ''.maketrans(intab, outtab)

    fin_man = Toolbox(url, headers, cookies)
    urls, tit = fin_man.get_url(path, tit)
    # for k in tqdm.trange(len(urls)):
    #     title, ans_sum, curr = fin_man.get_txt(url=urls[k])
    #     try:
    #         with open(f'data/{tit[k].translate(trantab)}.txt', 'w+') as f:
    #             for i in range(len(title)):
    #                 f.write(f'{i + 1}、{title[i][0]}\n')
    #                 for j in range(len(ans_sum[i])):
    #                     f.write(f'{chr(65 + j)}、{ans_sum[i][j][0]}\n')
    #                 f.write(f'{"".join(curr[i])}\n\n')
    #     except Exception:
    #         pass
    s = 0
    for k in tqdm.trange(len(urls)):
        title, ans_sum, curr = fin_man.get_txt(urls[k])
        try:
            with open(f'Sum.txt', 'a+') as f:
                for i in range(len(title)):
                    s = s + 1
                    f.write(f'{s}、{title[i][0]}\n')
                    for j in range(len(ans_sum[i])):
                        f.write(f'{chr(65 + j)}、{ans_sum[i][j][0]}\n')
                    f.write(f'{"".join(curr[i])}\n\n')
        except Exception:
            pass
