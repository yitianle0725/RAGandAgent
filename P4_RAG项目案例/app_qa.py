# streamlit run app_qa.py
import time
from rag import RagService
import config_data as config

import streamlit as st

# title
st.title("智能客服")
st.divider()

if "message" not in st.session_state:
    st.session_state["message"] = [{"role": "assistant", "content": "你好，有什么可以帮你？"}]

if "rag" not in st.session_state:
    st.session_state["rag"] = RagService()

for message in st.session_state["message"]:
    st.chat_message(message["role"]).write(message["content"])

# 输入栏
prompt = st.chat_input()

if prompt:
    st.chat_message("user").write(prompt)
    st.session_state["message"].append({"role": "user", "content": prompt})

    with st.spinner("载入知识库中..."):
        time.sleep(1)
        answer_stream = st.session_state["rag"].chain.stream({"input": prompt}, config.session_config)

        answer_list = []


        # yield
        def capture(generator, list):
            # 捕获流式输出，并存入list，再原样返还
            for item in generator:
                list.append(item)
                yield item


        st.chat_message("assistant").write(capture(answer_stream, answer_list))
        st.session_state["message"].append({"role": "assistant", "content": "".join(answer_list)})
        # 用"".join()将碎片str连起来
