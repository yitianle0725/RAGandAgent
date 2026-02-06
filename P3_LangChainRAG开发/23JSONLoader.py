from langchain_community.document_loaders import JSONLoader

loader = JSONLoader(
    file_path="./data/stu_json_lines.json",
    jq_schema=".name",
    text_content=False,  # 告知JSONLoader抽取内容非字符串
    json_lines=True,  # 告知JSONLoader,这是一个json_lines文件，每一行是一个正确的json数据
)

documents = loader.load()
print(documents)
