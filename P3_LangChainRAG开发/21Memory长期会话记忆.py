import os, json
from typing import Sequence

from langchain_community.chat_models import ChatTongyi
from langchain_core.messages import messages_from_dict, message_to_dict, BaseMessage
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableWithMessageHistory


# messages_from_dict:[字典,字典...]->[消息,消息...]
# message_to_dict:单个消息对象(BaseMessage实例)->字典
# AIMessage,HumanMessage,SystemMessage都是BaseMessage的子类

# 实现长期记忆的类
class FileChatMessageHistory(BaseChatMessageHistory):
    def __init__(self, session_id, storage_path):
        self.session_id = session_id  # 会话id
        self.storage_path = storage_path  # 不同会话id的存储文件，所在文件夹路径
        # 完整文件夹的名称
        self.file_path = os.path.join(self.storage_path, self.session_id)
        # 确保文件夹是存在的
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)

    def add_messages(self, messages: Sequence[BaseMessage]) -> None:
        all_messages = list(self.messages)  # 已有的消息列表
        all_messages.extend(messages)  # 把新的消息加入到已有的消息列表

        new_messages = [message_to_dict(messages) for messages in all_messages]
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(new_messages, f)

    @property  # @property装饰器将messages方法变为属性使用
    def messages(self) -> list[BaseMessage]:
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                messages_data = json.load(f)
                return messages_from_dict(messages_data)
        except FileNotFoundError:
            return []

    def clear(self):
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump([], f)


model = ChatTongyi(model="qwen3-max")
# prompt = PromptTemplate.from_template(
#     "你需要根据对话历史回应用户问题。对话历史：{chat_history}。用户当前输入：{input}，请回答"
# )

chat_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "你需要根据对话历史回应用户问题。对话历史："),
        MessagesPlaceholder("chat_history"),
        ("human", "请回答：{input}")
    ]
)
str_parser = StrOutputParser()


# 查看每次的prompt
def print_prompt(full_prompt):
    print("=" * 20, "\n", full_prompt.to_string(), "\n", "=" * 20)  # 打印这部分内容
    return full_prompt


base_chain = chat_prompt | print_prompt | model | str_parser


# 读取SessionID对应的长期会话历史文件
def get_history(session_id):
    return FileChatMessageHistory(session_id, "./chat_history")


# 创建一个新链，对基链增强：自动附加历史消息
conversation_chain = RunnableWithMessageHistory(
    base_chain,  # 基链
    get_history,  # 通过会话ID获取InMemoryChatMessageHistory类对象
    input_messages_key="input",
    history_messages_key="chat_history",
)

if __name__ == "__main__":
    # 固定格式，添加LangChain的配置，为当前程序配置所属的session_id
    session_config = {
        "configurable": {
            "session_id": "user_001"
        }
    }
    # res = conversation_chain.invoke({"input": "小明有2个猫"}, session_config)
    # print("回复1:", res)
    #
    # res = conversation_chain.invoke({"input": "小红有3只狗"}, session_config)
    # print("回复2:", res)

    res = conversation_chain.invoke({"input": "总共有几个宠物"}, session_config)
    print("回复3:", res)
