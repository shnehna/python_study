info_dictionary = {"name": "小名", "age": 18, 88: "father", ("monther",): 19.0}
print(type(info_dictionary))
print(info_dictionary.items())
print(type(info_dictionary.items()))
print(info_dictionary.keys())
print(type(info_dictionary.keys()))
print(info_dictionary.values())
print(type(info_dictionary.values()))
print(info_dictionary["name"])

info_dictionary["what"] = "name"
print(info_dictionary)
info_dictionary["name"] = "小明"
print(info_dictionary)

print("  %d " % len(info_dictionary))

# 合并字典
temp_dict = {"name": "小红", "age": 199}
info_dictionary.update(temp_dict)
print(info_dictionary)

# 循环遍历
for dictt in info_dictionary:  # 直接得到keys
    print(info_dictionary[dictt])

# 列表和字典的组合

dict_list = [{"name": "shenhan"},
             {"name": "liushaung"}
             ]
