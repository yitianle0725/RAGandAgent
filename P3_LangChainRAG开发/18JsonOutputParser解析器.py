from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models.tongyi import ChatTongyi

# 创建所需的解析器
json_parser = JsonOutputParser()
str_parser = StrOutputParser()

# 创建模型
model = ChatTongyi(model="qwen3-max")

# 提示词模板
first_prompt = PromptTemplate.from_template(
    "我的邻居姓{lastname},刚生了一个孩子，性别为{gender},请你帮忙起个名字，并封装为JSON格式给我。"
    "要求key是name，value是你起的名字，请严格遵守格式要求"
)

second_prompt = PromptTemplate.from_template(
    "姓名:{name},请帮我解析含义,简单回答即可"
)

# chain1 = first_prompt | model | json_parser
# res1 = chain1.invoke(input={"lastname": "张", "gender": "女"})
# print(res1)
# print(type(res1))

# chain2 = chain1 | second_prompt | model | str_parser
# res2 = chain2.invoke(input={"lastname": "张", "gender": "女"})
# print(res2)
# print(type(res2))

chain = first_prompt | model | json_parser | second_prompt | model | str_parser
for chunk in chain.stream(input={"lastname": "张", "gender": "女"}):
    print(chunk, end="", flush=True)


# 在构建链的时候要注意整体兼容性，注意前后组件的输入和输出要求。
# ·模型输入：PromptValue或字符串或序列(BaseMessage、list、tuple、 str、 dict)。
# ·模型输出：AIMessage
# ·提示词模板输入：要求是字典
# ·提示词模板输出：PromptValue对象
# ·StrOutputparser:AIMessage输入、str输出
# ·JsonOutputparser:AIMessage输入、dict输出