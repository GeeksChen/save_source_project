#### 前沿
>能够流程化的业务尽量自动化。提高效率，最大程度的商业化才是首要。


>本人的业务逻辑是这样：
第一步：首先抓包，获取需要的接口；
第二步：开启爬虫，保存爬取的资源；
第三步：根据本地的资源，生成json，入库；
第四步：把本地资源上传S3；
第五步：通过服务端API请求数据。

##### 流程图：
![流程图.png](https://upload-images.jianshu.io/upload_images/1745735-b689bc6b8998a2da.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

>本片文章主要介绍第二步，第三步，第四步

#### 第二步：对文件重命名&生成json
```
rename_json.py
```
>批量修改文件名

![批量修改文件名.png](https://upload-images.jianshu.io/upload_images/1745735-581ea925e3be1648.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

>生成json

![生成json.png](https://upload-images.jianshu.io/upload_images/1745735-f71aaa972e74a6cd.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


#### 第三步：连接数据库&建表&入库
```
json_to_mysql.py
```
>连接数据库

![连接数据库.png](https://upload-images.jianshu.io/upload_images/1745735-08517f2d1c000de7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

>建表

![建表.png](https://upload-images.jianshu.io/upload_images/1745735-c755ba4933d416aa.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

>入库

![入库.png](https://upload-images.jianshu.io/upload_images/1745735-c2005d94bdf77057.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


##### 第四步：连接S3&创建目录&批量上传资源
```
file_to_s3.py
```
>连接S3

![连接S3.png](https://upload-images.jianshu.io/upload_images/1745735-84fac92db57f3b69.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

>创建目录

![创建目录.png](https://upload-images.jianshu.io/upload_images/1745735-fe34e2f586c161ad.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

>批量上传资源

![批量上传资源.png](https://upload-images.jianshu.io/upload_images/1745735-d26386b6b5933a9c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

#### 最后

不管大佬们关不关注公众号，我都会放上本章的[Demo](https://github.com/GeeksChen/autoDataProcessing)


个人作品1：（匿名聊天）
[http://im.meetyy.cn/](http://im.meetyy.cn/)

个人作品2：（单身交友）
![公众号Meetyy](https://upload-images.jianshu.io/upload_images/1745735-9ba29c862a0268be.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


