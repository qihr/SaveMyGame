# 概述

因为昨天完了二十几个小时的FallOut2存档被steam云覆盖，恼羞成怒，决定写一个备份存档的工具。

需要写的内容如下：

- 抓取一份持续维护的游戏存档信息集合（可能要我自己写然后维护，因为我没有找到哪个网站保留了所有游戏的存档目录，steam云如何找到存档目录的并不清楚）
- 在游戏运行结束后自动备份。
- 定时备份游戏存档。
- 对游戏存档进行归档，压缩zip。
- 反向输出存档到游戏目录
- 图形界面？

其实我希望有人能帮帮我这个菜逼。

思考了一下，我决定在用户配置好保存路径后，如果是有效的，就上传至服务器。
- 抓取一份持续维护的游戏存档信息集合（可能要我自己写然后维护，因为我没有找到哪个网站保留了所有游戏的存档目录，steam云如何找到存档目录的并不清楚）

# 日志

​	这块是日志内容，每次写的东西会在这做个总结。



## 2020-03-17 20:13:35 

​	简单了解了一下python，写了读取本地游戏信息csv然后保存到指定目录的模块。保存路径是测试用写死了。
