from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

# Define the model
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()

template = PromptTemplate(
    # template='Tell me about Black hole \n {format_instruction}',
    # input_variables=[],
    template='Give me 5 facts about {topic} \n {format_instruction}',#-->Usng chain
    input_variables=['topic'], #-->using chain
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

# without chain 
# prompt=template.format()
# result=model.invoke(prompt)
# final_result=parser.parse(result.text)
# print(final_result)
# print(type(final_result))

# using chain
chain = template | model | parser

result = chain.invoke({'topic':'black hole'})

print(result)
