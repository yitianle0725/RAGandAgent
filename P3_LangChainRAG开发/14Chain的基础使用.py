from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_models.tongyi import ChatTongyi

chat_prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个把酒言欢的诗人"),
        MessagesPlaceholder("history"),  # 注入历史消息
        ("human", "请再写一首唐诗"),
        # ("ai", "锄禾日当午，汗滴禾下土，谁知盘中餐，粒粒皆辛苦"),
        # ("human", "按照上个回复的格式，再写一首唐诗"),
    ]
)

history_data = [
    # ("system", "你是一个把酒言欢的诗人"),
    ("human", "写一首唐诗"),
    ("ai", "床前明月光，疑似地上霜，举头望明月，低头思故乡"),
    # ("human", "按照上个回复的格式，再写一首唐诗"),
    ("human", "再来一个"),
    ("ai", "锄禾日当午，汗滴禾下土，谁知盘中餐，粒粒皆辛苦"),
]

model = ChatTongyi(model="qwen3-max")

# 形成链，要求每一个组件都是Runnable接口的子类
# 一个组建的输出，为下一个组件的输入
# chain是RunnableSequence类型
chain = chat_prompt_template | model

# res = chain.invoke({"history": history_data})
# print(res.content)

res = chain.stream({"history": history_data})
for chunk in res:
    print(chunk.content, end="", flush=True)
