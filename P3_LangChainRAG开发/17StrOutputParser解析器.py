from langchain_community.llms.tongyi import Tongyi
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models.tongyi import ChatTongyi

# StrOutputParser可以将AIMessage类型转为str
parser = StrOutputParser()
model = ChatTongyi(model="qwen3-max")
prompt = PromptTemplate.from_template(
    "我的邻居姓{lastname},刚生了一个孩子，性别为{gender},请你帮忙起个名字，简单回答"
)

# 未加入解析器
# chain = prompt | model | model
#
# res = chain.invoke(input={"lastname": "张", "gender": "女"})
# print(res.content)
# # ValueError: Invalid input type <class 'langchain_core.messages.ai.AIMessage'>. Must be a PromptValue, str, or list of BaseMessages.


# 加入解析器parser
chain = prompt | model | parser | model | parser
res = chain.invoke(input={"lastname": "张", "gender": "女"})
print(res)
print(type(res))
