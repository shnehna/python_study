# list 列表 是专门存储一串信息
# 用 [] 定义,索引从0开始
name_list = ["zhangsan", "lisi", "lisi", "wangwu"]
# 1.取值
print(name_list[2])
print(name_list.index("lisi"))
# 2.修改
name_list[2] = "wangermazi"
# 3.增加
name_list.append("123")
name_list.insert(1, "123")
name_list.extend(["insert", "extend"])
# 4.删除
# name_list.remove(123)
# name_list.pop()
# name_list.remove(123)
# name_list.clear()
del name_list[1]
# 5.统计
len(name_list)
name_list.count("123")
# 6.排序
print(name_list)
name_list.sort()
print(name_list)
name_list.sort(reverse=True)
print(name_list)
name_list.reverse()
print(name_list)

# 7.迭代循环遍历
# for name in name_list:
#     print(name)
for index in range(0, 7):
    print(name_list[index])
