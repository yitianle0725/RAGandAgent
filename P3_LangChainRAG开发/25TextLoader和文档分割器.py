from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = TextLoader(
    file_path="./data/Python基础语法.txt",
    encoding="utf-8",
)
docs = loader.load()

# print(docs)
# print(len(docs))

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,  # 分段的最大字符数
    chunk_overlap=50,  # 分段之间允许重叠字符数
    # 自然段的分割依据
    separators=["\n\n", "\n", "。", "！", "？", ".", "!", "?", " ", ""],
    length_function=len,
)

split_docs = splitter.split_documents(docs)

print(len(split_docs))
for doc in split_docs:
    print(doc)
    print("=" * 40)
    print("=" * 40)
