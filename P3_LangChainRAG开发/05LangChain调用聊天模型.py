from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

model = ChatTongyi(model="qwen3-max")  # 因为qwen3-max是聊天模型，qwen-max是大语言模型。api-key已经保护在环境变量中

messages = [
    # SystemMessage(content="你是一个把酒言欢的诗人"),
    # HumanMessage(content="写一首唐诗"),
    # AIMessage(content="锄禾日当午，汗滴禾下土，谁知盘中餐，粒粒皆辛苦"),
    # HumanMessage(content="按照上个回复的格式，再写一首唐诗"),
    ("system", "你是一个把酒言欢的诗人"),
    ("human", "写一首唐诗"),
    ("ai", "锄禾日当午，汗滴禾下土，谁知盘中餐，粒粒皆辛苦"),
    ("human", "按照上个回复的格式，再写一首唐诗"),
    # 使用类对象的方式是 静态 的，一步到位
    # 直接得到Messaage类的类对象
    # 使用简写形式，则是 动态 的，在运行时，由langchain内部机制，转换为Messaage类对象
]

res = model.stream(input=messages)
for chunk in res:
    print(chunk.content, end="", flush=True)  # 聊天模型和llms不完全一致，此处需要加上.content
