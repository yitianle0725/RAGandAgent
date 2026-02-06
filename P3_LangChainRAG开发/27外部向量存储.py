from langchain_chroma import Chroma
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.document_loaders import CSVLoader

# pip install langchain-chroma chromadb -i https://pypi.tuna.tsinghua.edu.cn/simple

vector_store = Chroma(
    collection_name="test",  # 为当前向量存储起名
    embedding_function=DashScopeEmbeddings(),
    persist_directory="./chroma_db"  # 指定存放位置
)

# loader = CSVLoader(
#     file_path="./data/info.csv",
#     # csv_args={
#     #     "delimiter": ",",  # 指定分隔符，方便正确识别
#     #     "quotechar": '"',  # 指定带有分隔符文本的引号包围是 单引号or双引号
#     #     # "fieldnames": ['name', 'age', 'gender', 'hobby']  # 若数据原本无表头，则需要带上该参数
#     # },
#     encoding="utf-8",
#     source_column="source",  # 指定本条数据的来源为 ”xxx“
# )
#
# documents = loader.load()
# # for document in documents:
# #     print("=" * 40)
# #     print(document)
# #     print("=" * 40)
#
#
# # 向量存储的 新增、删除、相似检索
# vector_store.add_documents(
#     documents=documents,
#     ids=[f"id{i}" for i in range(1, 1 + len(documents))],
# )
#
# vector_store.delete(["id1", "id2"])

res = vector_store.similarity_search(
    query="明天晚上吃啥子呀",
    k=3,  # 检索的结果数量
    filter={"source": "黑马程序员"},
)
print(res)
