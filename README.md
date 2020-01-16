# Lanmoyun-download

批量爬取蓝墨云班课中的习题

----

本程序使用Python3.7.2编写

请使用Python3.6及以上版本，若使用低版本请删去toolbox.py下Toolbox类中变量注释，并查看格式化`{}`方法是否适用于您的Python版本

e.g. 

将:

```python
def get_data(self, url: str) -> list:
```

修改为:

```python
def get_data(self, url):
```

将:

```python
title.append(html.xpath(f'/html/body/div[3]/div[2]/div[4]/div[{i + 1}]/div[1]/div/div[1]/div/div[3]/pre/text()'))
```

修改为:

```python
title.append(html.xpath('/html/body/div[3]/div[2]/div[4]/div[%]/div[1]/div/div[1]/div/div[3]/pre/text()' % str(i + 1))
```

----

## 安装依赖：

`pip install requests`

`pip install lxml`

`pip install tqdm`

----

## 注意事项

- 本程序默认自动重连次数为10次(`for r in range(10):`)，重连等待时间为5秒(`time.sleep(5)`)，爬取网页等待时间为2秒(`time.sleep(2)`)，文件为程序所在目录下的**Sum.txt**(`with open('Sum.txt', 'a+') as f:`)。如需修改请在**data.py**文件中添加您需要的数值

- 本程序已构建可执行.exe文件，Windows平台可直接下载运行

- **Lanmoyun_scrapy**框架已完善, 请先修改**start.py**中的`url`及`cookie`, 然后修改**Lanmoyun_scrapy**中的**settings.py**中的`DEFAULT_REQUEST_HEADERS`, 最后运行**start.py**文件

- 刷答案方面，不建议用Python，因为对网页进行Javascript注入没有原生程序便捷。以多选题为例，下附Javascript代码:

  ```javascript
  # 选取多选题选项框
  answer_list = document.getElementsByTagName("i")
  # 判断总个数，并逐一选取
  for(i=0;i<answer_list.length;i++) {answer_list[i].click()}
  ```

  若出现单选，则判断个数后用总数除以选项分组。为确保刷题的真实性，可添加随机选取，修改i++，用random()函数结合自身页面进行调整

  用法:

  以Chrome浏览器为例:

  1. 单击右上角3个点

  2. 单击更多工具

  3. 单击**开发者工具**(注: 每个浏览器的开发者工具位置大体一致)

  4. 单击Console后输入javascript代码(注: Firefox浏览器为**控制台**)

----

## 已解决问题：

1. 批量爬取蓝墨云班课活动

2. 题目统一编号整理后写入统一文档--v2.0

3. Session会话管理--v2.1

6. tqdm加入进度条

7. 完善Lanmoyun_scrapy

----

## 待解决问题：

1.将题目以首字母拼音升序排列(拟用pypinyin库构建)

2.改用asyncio + aiohttp + ThreadPoolExecutor进行高并发多线程爬取

## 运行程序

`python main.py`

按照终端提示依次输入用户名、密码及网址

注: 网址为您课程下题目集合的网址

![demo](pic/demo.png)
