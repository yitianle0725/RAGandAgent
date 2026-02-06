import json

d = {
    "name": "周杰伦",
    "age": 22,
    "gender": "男",
}

# print(str(d)) # str和json还是不一样的，一个单引号，一个双引号
s = json.dumps(d, ensure_ascii=False)  # ensure_ascii 用于确保中文正常显示
print(s)  # 返回值json字符串

l = [
    {
        "name": "周杰伦",
        "age": 22,
        "gender": "男",
    },
    {
        "name": "张杰",
        "age": 12,
        "gender": "男",
    },
    {
        "name": "邓紫棋",
        "age": 22,
        "gender": "女",
    },
]
# json.dumps() : python字典或列表->json字符串
print(json.dumps(l, ensure_ascii=False))

# json.loads() : json字符串->python字典或列表
json_str = '{"name": "周杰伦", "age": 22, "gender": "男"}'
json_array_str = '[{"name": "周杰伦", "age": 22, "gender": "男"}, {"name": "张杰", "age": 12, "gender": "男"}, {"name": "邓紫棋", "age": 22, "gender": "女"}]'

res_dict = json.loads(json_str)
print(res_dict, type(res_dict))

res_list = json.loads(json_array_str)
print(res_list, type(res_list))
