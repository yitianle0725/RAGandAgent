from openai import OpenAI
import os

client = OpenAI(
    # 如果没有配置环境变量，请用阿里云百炼API Key替换：api_key="sk-xxx"
    # api_key=os.getenv("DASHSCOPE_API_KEY"),
    # api_key="sk-a167bbd8d76f479aba51a744a62bed6e",//在环境变量里配置API_KEY用于保护
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

messages = [{"role": "user", "content": "你是谁，能做什么？"}]
completion = client.chat.completions.create(
    model="qwen-flash",  # 您可以按需更换为其它深度思考模型
    messages=messages,
    # extra_body={"enable_thinking": True},
    stream=True
)
# is_answering = False  # 是否进入回复阶段
# print("\n" + "=" * 20 + "思考过程" + "=" * 20)
for chunk in completion:
    print(chunk.choices[0].delta.content,end="",flush=True)