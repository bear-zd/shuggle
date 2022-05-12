# shuggle
shu数据库大作业——shuggle科学竞赛平台
# user表

| First_name    | 用户姓         |
| ------------- | -------------- |
| Last_name     | 用户名         |
| Email         | 邮箱           |
| register_date | 注册日期       |
| user_id       | 用户id（主键） |
| Password      | 用户密码       |



# BBSsection表

BBS中的某个板块

| Sid         | 板块号     |
| ----------- | ---------- |
| Sname       | 板块名     |
| Sclickcount | 板块点击数 |

目前假设只有一个板块

# BBStopic表

某个板块下的某个topic

| Tid            | topic号（主键）             |
| -------------- | --------------------------- |
| Tsid           | 该话题所属的板块号（topic） |
| Tuid           | 话题发起者的用户id          |
| Treplycount    | 该话题的回复次数            |
| Temotioin      | 发起话题时的emoji           |
| Ttopic         | 该话题的标题                |
| Tcontents      | 该话题的内容                |
| Ttime          | 话题发起时间                |
| Tclickcount    | 话题点击量                  |
| Tlastclicktime | 话题上次的点击时间          |



# BBSreply表

用户回复话题的连接表


| Tid       | Topic id （主键）         |
| --------- | ------------------------- |
| Replytime | 回复时间                  |
| content   | 回复内容                  |
| replied   | 该reply的号码（主键）     |

# available 表

相较于之前添加了availabel_topic_id