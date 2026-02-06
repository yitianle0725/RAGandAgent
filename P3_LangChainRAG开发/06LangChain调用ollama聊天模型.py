from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

model = ChatOllama(model="qwen3:4b")  # 因为qwen3-max是聊天模型，qwen-max是大语言模型。api-key已经保护在环境变量中

messages = [
    ("system", "你是一个把酒言欢的诗人"),
    ("human", "写一首唐诗"),
    ("ai", "锄禾日当午，汗滴禾下土，谁知盘中餐，粒粒皆辛苦"),
    ("human", "按照上个回复的格式，再写一首唐诗"),
    # SystemMessage(content="你是一个把酒言欢的诗人"),
    # HumanMessage(content="写一首唐诗"),
    # AIMessage(content="锄禾日当午，汗滴禾下土，谁知盘中餐，粒粒皆辛苦"),
    # HumanMessage(content="按照上个回复的格式，再写一首唐诗"),
]

res = model.stream(input=messages)
for chunk in res:
    print(chunk.content, end="", flush=True)  # 聊天模型和llms不完全一致，此处需要加上.content
