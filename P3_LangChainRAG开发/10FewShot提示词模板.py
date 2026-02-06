from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate
from langchain_community.llms.tongyi import Tongyi

# 示例的模板
example_template = PromptTemplate.from_template("单词：{word},反义词：{antonym}")

# 示例的动态数据注入，要求是list内部套字典
example_data = [
    {"word": "大", "antonym": "小"},
    {"word": "上", "antonym": "下"},
]

few_shot_template = FewShotPromptTemplate(
    # 该对象的构建需要5个核心参数
    example_prompt=example_template,
    examples=example_data,
    prefix="告知我单词的反义词，示例如下：",
    suffix="基于前面的示例告诉我，{input_word}的反义词是？",
    input_variables=["input_word"],
    # output_variables=[],
)

prompt_text = few_shot_template.invoke(input={"input_word": "左"}).to_string()
# print(prompt_text)
# .format()得到的是字符串
# .invoke()得到的是一个prompt类

model = Tongyi(model="qwen-max")
print(model.invoke(input=prompt_text))
