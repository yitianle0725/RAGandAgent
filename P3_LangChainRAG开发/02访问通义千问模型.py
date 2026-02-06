from langchain_community.llms.tongyi import Tongyi

# 不用qwen3-max,因为qwen3-max是聊天模型，qwen-max是大语言模型
model = Tongyi(model="qwen-max")  # 参数内含有API-KEY，因为已经保护在本地环境变量中，故此处省略填写

# 调用invoke向模型提问
res = model.invoke(input="你是谁？能做什么？")

print(res)
