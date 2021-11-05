import csv
from kyb_testproject.baseView.log import Logger


# 读取csv文件
def get_scv_data(csv_file, line):
    with open(csv_file, "r", encoding="utf-8-sig") as file:
        reader = csv.reader(file)
        for index, row in enumerate(reader, 1):
            if index == line:
                return row


csv_file = '../data/account.csv'
data = get_scv_data(csv_file, 1)  # 需要获取到第几行的数据就改为几行
# 通过下标获取单个数据


# for方法 循环读取列表中的数据，索引和索引志向数据
list = ["这", "是", "一个", "测试数据"]
for i in range(len(list)):
    print(i, list[i])

# enumerate方法 循环读取列表中的数据，索引和索引志向数据
list1 = ["这", "是", "一个", "测试数据"]
for index, item in enumerate(list1):
    print(index, item)
