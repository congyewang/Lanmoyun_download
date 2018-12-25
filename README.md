# Lanmoyun-download

批量爬取蓝墨云班课中的习题

----

本程序使用Python3.7.0编写

请使用Python3.6及以上版本，若使用低版本请修改toolbox.py下Toolbox类中变量注释

----

#安装依赖：

`pip install requests`
  
`pip install lxml`

`pip install fake-useragent`

`pip install tqdm`

----

输入账号和密码及待爬取的课程网页即可使用, sleep参数没有默认值, 建议为2

**请务必查看环境是否需要使用代理！！！视情况更改requests.get的proxy参数！！！**

本程序已构建可执行exe文件

----

#已解决问题：

1.批量爬取蓝墨云班课活动

2.题目统一编号整理后写入统一文档--v2.0

3.Session会话管理--v2.1

4.加入difflib便于比较文件版本差异--v2.1.1

5.fake-useragent随机生成浏览器头

6.tqdm加入进度条

----

#待解决问题：

1.将题目以首字母拼音升序排列(拟用pypinyin库构建)

2.改用asyncio + aiohttp + ThreadPoolExecutor进行高并发多线程爬取
