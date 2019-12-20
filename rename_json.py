import os
import re
import sys
import json


# 批量修改文件名字
def rename():

    # 目录名字
    dir_name = 'Abstract'
    # 待修改文件夹
    file_list = os.listdir(r"/Users/mjdev/Desktop/save_source_project/" + dir_name)
    # 输出文件夹中包含的文件
    print("修改前：" + str(file_list))
    # 得到进程当前工作目录
    current_dir_path = os.getcwd()
    # 将当前工作目录修改为待修改文件夹的位置
    os.chdir(r"/Users/mjdev/Desktop/save_source_project/" + dir_name)

    num = 1  # 名称变量
    for fileName in file_list:  # 遍历文件夹中所有文件

        pat = ".+\.(jpg|png|pgm|JPG|jpeg|PNG)"   # 匹配文件名正则表达式
        pattern = re.findall(pat, fileName)  # 进行匹配

        str1 = dir_name + '_' + str(num)
        # hl = hashlib.md5()
        # hl.update(str1.encode(encoding='utf-8'))
        os.rename(fileName, str1 + '.' + pattern[0])  # 文件重新命名
        num = num + 1  # 改变编号，继续下一项
    print("---------------------------------------------------")
    os.chdir(current_dir_path)  # 改回程序运行前的工作目录
    sys.stdin.flush()  # 刷新
    print("修改后：" + json.dumps(os.listdir(r"/Users/mjdev/Desktop/save_source_project/" + dir_name)))  # 输出修改后文件夹中包含的文件

    to_json(dir_name)


# 生成目标json
def to_json(dir_name):

    # 生成最外层字典
    resDic = {}
    list2 = os.listdir(r"/Users/mjdev/Desktop/save_source_project/" + dir_name)
    resDic["data"] = list2
    resDic["msg"] = "获取数据成功"
    with open("/Users/mjdev/Desktop/save_source_project/" + dir_name + ".json", "w") as f:
        json.dump(resDic, f)
        print("加载入文件完成...")


if __name__ == "__main__":  # 起到一个初始化或者调用函数的作用
    rename()
