from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(
    file_path="./data/pdf2.pdf",
    mode="single",  # 默认page，按页存document， single模式则不管多少页，只生成一个document对象
    password="itheima",
)

count = 0
for document in loader.lazy_load():
    print(document)
    count += 1
    print("=" * 20, count, "=" * 20)
