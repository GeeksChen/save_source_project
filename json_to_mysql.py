import json
import pymysql

# 建表
def create_table(db):

    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")
    data = cursor.fetchone()
    print("Database version : %s " % data)  # 结果表明已经连接成功
    cursor.execute("DROP TABLE IF EXISTS api_items")  # 习惯性
    sql = """CREATE TABLE `api_items` (
              `lid` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键id,分类id',
              `pid` int(11) NOT NULL DEFAULT 0 COMMENT '父id',
              `title` varchar(32) NOT NULL DEFAULT '' COMMENT '分类名称',
              `imgpath` varchar(256) NOT NULL DEFAULT '' COMMENT '分类图片路径',
              `color` varchar(32) NOT NULL DEFAULT '' COMMENT '背景色',
              `isfree` tinyint(4) NOT NULL DEFAULT '1' COMMENT '是否免费 1收费 0免费',  
              `status` tinyint(4) NOT NULL DEFAULT '1' COMMENT '状态 1显示 0隐藏',
              PRIMARY KEY (`lid`)
            ) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4"""
    cursor.execute(sql)  # 根据需要创建一个表格

# json数据入库
def insert_data_to_table(db):

    # 目录名
    dir_name = 'Animals'
    with open('/Users/mjdev/Desktop/save_source_project/'+dir_name+'.json', encoding='utf-8') as f:
        i = 0
        lines = f.readline()  # 使用逐行读取的方法
        review_text = json.loads(lines)  # 解析每一行数据
        print(review_text['data'])
        for imgpath in review_text['data']:
            i += 1
            result = []
            result.append((2, dir_name, imgpath, "000000", 0, 1))
            print(result)

            inesrt_re = "insert into api_items(pid, title, imgpath, color, isfree, status) values (%s, %s, %s,%s, %s,%s)"
            cursor = db.cursor()
            cursor.executemany(inesrt_re, result)
            db.commit()


if __name__ == "__main__":  # 起到一个初始化或者调用函数的作用

    db = pymysql.connect("localhost", "root", "", "api", charset='utf8')
    cursor = db.cursor()
    create_table(db) #建表
    insert_data_to_table(db) #插入数据
    cursor.close()