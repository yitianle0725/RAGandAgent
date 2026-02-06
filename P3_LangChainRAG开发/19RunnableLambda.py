from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.runnables import RunnableLambda

# 创建模型
model = ChatTongyi(model="qwen3-max")

# StrOutputParser可以将AIMessage类型转为str
str_parser = StrOutputParser()

# 提示词模板
first_prompt = PromptTemplate.from_template(
    "我的邻居姓{lastname},刚生了一个孩子，性别为{gender},请你帮忙起一个名字，仅告知我名字，不要额外信息"
)

second_prompt = PromptTemplate.from_template(
    "姓名:{name},请帮我解析含义,简单回答即可"
)

# AIMessage -> dict({"name":"xxx"})
my_func = RunnableLambda(lambda ai_msg: {"name": ai_msg.content})

# 加入解析器parser
chain = first_prompt | model | my_func | second_prompt | model | str_parser
res = chain.stream(input={"lastname": "曹", "gender": "女"})
for chunk in res:
    print(chunk, end="", flush=True)
