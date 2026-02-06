from langchain_community.embeddings import DashScopeEmbeddings

# 创建模型对象不传model默认用的是text-embeddings-v1
model = DashScopeEmbeddings()

# 不用invoke stream

print(model.embed_query("你好"))
print(model.embed_documents(["你好", "吃什么", "吃面条"]))


# from langchain_ollama import OllamaEmbeddings
#
# # 创建模型对象不传model默认用的是text-embeddings-v1
# model = OllamaEmbeddings(model="qwen3-embedding:4b")  # ollama模型，需要下载到本地
#
# # 不用invoke stream
# print(model.embed_query("你好"))
# print(model.embed_documents(["你好", "吃什么", "吃面条"]))
