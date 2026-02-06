from openai import OpenAI
import os

client = OpenAI(
    # base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    # 注意一个是https一个是http
    # 本地部署的模型则不需要api-key
    base_url="http://localhost:11434/v1",
)

messages = [{"role": "user", "content": "你是谁，能做什么？"}]
completion = client.chat.completions.create(
    model="qwen3:4b",  # 您可以按需更换为其它深度思考模型
    messages=messages,
    # extra_body={"enable_thinking": True},
    stream=True
)
# is_answering = False  # 是否进入回复阶段
# print("\n" + "=" * 20 + "思考过程" + "=" * 20)
for chunk in completion:
    print(chunk.choices[0].delta.content, end="", flush=True)
