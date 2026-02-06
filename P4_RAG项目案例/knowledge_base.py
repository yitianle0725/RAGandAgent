"""
知识库
"""

import os
import config_data as config
import hashlib
from langchain_chroma import Chroma
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from datetime import datetime


def check_md5(md5_str: str):
    # 检查是否经过md5处理
    if not os.path.exists(config.md5_path):
        # 未处理过
        open(config.md5_path, 'w', encoding='utf-8').close()
        return False
    else:
        for line in open(config.md5_path, 'r', encoding='utf-8').readlines():
            line = line.strip()  # 去掉str前后的空格和回车
            if line == md5_str:
                return True  # 已处理过
        return False


def save_md5(md5_str: str):
    # 将传入的文件的md5值保存，以防重复
    with open(config.md5_path, 'a', encoding='utf-8') as f:
        f.write(md5_str + '\n')


def get_string2md5(input_str: str, encoding='utf-8'):
    # str->bytes
    str2bytes = input_str.encode(encoding=encoding)
    return hashlib.md5(str2bytes).hexdigest()


class KnowledgeBaseService(object):
    def __init__(self):
        os.makedirs(config.persist_directory, exist_ok=True)

        self.chroma = Chroma(
            collection_name=config.collection_name,  # 数据库的表名
            embedding_function=DashScopeEmbeddings(model="text-embedding-v4"),
            persist_directory=config.persist_directory,  # 数据库本地存储文件
        )  # 向量数据库实例

        self.spliter = RecursiveCharacterTextSplitter(
            chunk_size=config.chunk_size,  # 分割后的文本段落最大值
            chunk_overlap=config.chunk_overlap,  # 分割文本段之间的字符值重复数量
            separators=config.separators,  # 自然段落划分符号
            length_function=len,
        )  # 文本分割器的对象

    def upload_by_str(self, data: str, filename):
        # 将字符串向量化，并存入向量数据库
        md5_hex = get_string2md5(data)
        if check_md5(md5_hex):
            return "[跳过]内容已存在知识库中"

        # 超过阈值才分割
        if len(data) > config.max_split_char_number:
            knowledge_chunks: list[str] = self.spliter.split_text(data)
        else:
            knowledge_chunks = [data]

        metadata = {
            "source": filename,
            "create_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "operator": "ytl"
        }
        self.chroma.add_texts(
            knowledge_chunks,
            metadatas=[metadata for _ in knowledge_chunks],
        )

        save_md5(md5_hex)

        return "[成功]内容已经成功载入向量库"


if __name__ == '__main__':
    service = KnowledgeBaseService()
    r = service.upload_by_str("黑马", "testfile")
    print(r)
