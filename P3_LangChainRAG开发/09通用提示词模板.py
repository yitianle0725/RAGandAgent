from langchain_core.prompts import PromptTemplate
from langchain_community.llms.tongyi import Tongyi

prompt_template = PromptTemplate.from_template(
    "我的邻居姓{lastname},刚生了一个孩子，性别为{gender},请你帮忙起个名字，简单回答"
)

# # 调用.format方法注入信息
# prompt_text = prompt_template.format(lastname="张", gender="女")
# # print(prompt_text)
#
# model = Tongyi(model="qwen-max")
# res = model.stream(input=prompt_text)
# for chunk in res:
#     print(chunk, end="", flush=True)

model = Tongyi(model="qwen-max")
chain = prompt_template | model # 封装到链条中

res = chain.invoke(input={"lastname": "张", "gender": "女"})
print(res)
