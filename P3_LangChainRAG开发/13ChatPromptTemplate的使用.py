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

prompt_text = chat_prompt_template.invoke({"history": history_data}).to_string()
# print(prompt_text)
# prompt_text = chat_prompt_template.invoke({"history": history_data})

model = ChatTongyi(model="qwen3-max")
res = model.invoke(input=prompt_text)
print(res.content)

# 哈哈，且听我新酿一壶诗——
#
# **《江楼夜饮》**
# 孤舟系柳月如钩，
# 浊酒倾杯笑客愁。
# 醉拍阑干呼雁字，
# 半江星火载诗流。
#
# （掷杯大笑）此诗可配三百杯！你看那江心星子落进酒盏，雁声驮着诗稿飞过云楼——这人间痛快，原不在金樽玉馔，而在肝胆相照时啊！
