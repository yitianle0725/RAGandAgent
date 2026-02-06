from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(
    file_path="./data/stu.csv",
    csv_args={
        "delimiter": ",",  # 指定分隔符，方便正确识别
        "quotechar": '"',  # 指定带有分隔符文本的引号包围是 单引号or双引号
        # "fieldnames": ['name', 'age', 'gender', 'hobby']  # 若数据原本无表头，则需要带上该参数
    },
    encoding="utf-8",
)

# # 批量加载 .load()->[Document,Document,...]
# documents = loader.load()
#
# for document in documents:
#     print(type(document))
#     print(document)
#     print("=" * 40)

# 懒加载 .load() 迭代器[Document]
# 内存不够而数据量较大的时候，使用懒加载
documents = loader.lazy_load()
for document in documents:
    print(type(document))
    print(document)
    print("=" * 40)
