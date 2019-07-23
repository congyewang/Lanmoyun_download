from toolbox import Toolbox
import tqdm
import time


def main():
    usr = input("Please input your user name:")
    pwd = input("Please input your password name:")
    url = input("Please input the url:")

    # 判断用户名是否为字符串
    if isinstance(usr, str):
        pass
    elif isinstance(usr, int):
        usr = str(usr)
    else:
        raise Exception("Type error")

    # 判断密码是否为字符串
    if isinstance(pwd, str):
        pass
    elif isinstance(pwd, int):
        usr = str(pwd)
    else:
        raise Exception("Type error")

    # 判断网址是否为字符串
    if isinstance(url, str):
        pass
    else:
        raise Exception("Type error")

    scrapy = Toolbox(usr, pwd, url)

    check = scrapy.login()
    if check["result_code"] == 0:
        pass
    else:
        raise Exception(
            f'error code: {check["result_code"]}\n error message: {check["result_msg"]}\n Please try again')

    urls, _ = scrapy.get_url()

    s = 0
    if urls:
        for k in tqdm.trange(len(urls)):
            for r in range(10):
                try:
                    title, ans_sum, curr = scrapy.get_data(urls[k])
                    break
                except Exception as e:
                    time.sleep(5)
                    print("\n" + e + "\n" + "#" * 20 +
                          f" Retry {r + 1} " + "#" * 20 + "\n")
            try:
                with open('Sum.txt', 'a+') as f:
                    for i in range(len(title)):
                        s += 1
                        f.write(f'{s}、{title[i][0]}\n')
                        for j in range(len(ans_sum[i])):
                            f.write(f'{chr(65 + j)}、{ans_sum[i][j][0]}\n')
                        f.write(f'{"".join(curr[i])}\n\n')
            except Exception:
                pass
            time.sleep(2)


if __name__ == "__main__":
    main()
