# Lanmoyun-download
批量爬取蓝墨云班课中的习题
----
本程序使用Python3.7.0编写

请使用Python3.6及以上版本，若使用低版本请修改toolbox.py下Toolbox类中变量注释
----

安装依赖：


`pip install requests`
  
`pip install lxml`
  
`pip install tqdm`

----
若无法安装tqdm请修改`tqdm.trange(len(urls))`为`range(len(urls))`

请检查代码根目录下是否有data文件夹

修改url及cookies参数后运行data.py进行爬取，得到txt文件即为班课中题目及答案

请自行调整格式

----

待解决问题：

1.与PostgreSQL进行连接并筛选

2.将输出文本进行格式清洗
