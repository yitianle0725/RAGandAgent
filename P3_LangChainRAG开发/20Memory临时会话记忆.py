from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory

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

store = {}  # key是session，value是InMemoryChatMessageHistory类对象


# 通过会话ID获取InMemoryChatMessageHistory类对象
# InMemoryChatMessageHistory可以实现在内存中存储会话历史，但是临时的，程序结束就没有了
def get_history(session_id):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()

    return store[session_id]


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
    res = conversation_chain.invoke({"input": "小明有2个猫"}, session_config)
    print("回复1:", res)
    res = conversation_chain.invoke({"input": "小红有3只狗"}, session_config)
    print("回复2:", res)
    res = conversation_chain.invoke({"input": "总共有几个宠物"}, session_config)
    print("回复3:", res)
