from langchain_ollama import OllamaLLM

model = OllamaLLM(model="qwen3:4b")  # 调用本地模型，故不需要api-key

# # 调用invoke向模型提问
# res = model.invoke(input="你是谁？能做什么？") #invoke方法：一次性返回结果
# print(res)


# 调用stream向模型提问
res = model.stream(input="你是谁？能做什么？")  # stream方法：流式输出结果
for chunk in res:
    print(chunk, end="", flush=True) #end=“”是为了去掉回车符，flush是立刻刷新缓冲区
