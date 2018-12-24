from toolbox import *
import time

if __name__ == '__main__':

    username = input('Please input your username:')
    password = input('Please input your password:')
    url = input('Please input the url:')
    tim = input('How long would you like to make the request sleep:')
    path = '//*[@class="interaction-row"]/@data-id'
    tit = '//*[@class="interaction-row"]//@title'

    fin_man = Toolbox(username=username, password=password, url=url)
    fin_man.cookies = fin_man.login()
    urls, tit = fin_man.get_url(path, tit)

    s = 0
    for k in range(len(urls)):
        title, ans_sum, curr = fin_man.get_txt(urls[k])
        time.sleep(int(tit))
        print(f'{k / len(urls) * 100:.2f}%')
        try:
            with open(f'data.txt', 'a+') as f:
                for i in range(len(title)):
                    s = s + 1
                    f.write(f'{s}、{title[i][0]}\n')
                    for j in range(len(ans_sum[i])):
                        f.write(f'{chr(65 + j)}、{ans_sum[i][j][0]}\n')
                    f.write(f'{"".join(curr[i])}\n\n')
        except Exception:
            pass
