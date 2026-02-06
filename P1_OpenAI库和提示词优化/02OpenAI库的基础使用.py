from openai import OpenAI

# 1.获取client对象，OpenAI对象
client = OpenAI(
    # api_key="sk-a167bbd8d76f479aba51a744a62bed6e",# 在环境变量里配置API_KEY用于保护
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

# 2.调用模型
response = client.chat.completions.create(
    model="qwen-flash",
    messages=[
        {"role": "system", "content": "你是一个Python编程专家，并且不说废话，简单回答"},
        {"role": "assistant", "content": "好的，我是编程专家，并且话不多，你要问什么？"},
        {"role": "user", "content": "输出1-10的数字使用python代码"},
    ],
    # message消息列表中，是可以组织历史消息，提供给模型的
    stream=True  # 开启流式输出，效果为字一个一个输出
)

# 3.处理结果
# print(response.choices[0].message.content)
for chunk in response:
    print(
        chunk.choices[0].delta.content,
        end="  ",       # 每一段之间以空格分隔
        flush=True,     # 立刻刷新缓冲区
    )

