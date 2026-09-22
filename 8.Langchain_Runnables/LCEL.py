from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence

from dotenv import load_dotenv

load_dotenv()

# Model
model = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")

# Prompt
prompt = PromptTemplate(
    template="What is {topic}?",
    input_variables=["topic"]
)

# Parser
parser = StrOutputParser()


# =====================================================
# 1. RunnableSequence - Explicit Way
# =====================================================

chain = RunnableSequence(prompt, model, parser)

result = chain.invoke({"topic": "Python"})
print("By Runnable Sequence:\n")
print(result)


# =====================================================
# 2. LCEL - Using Pipe Operator
# =====================================================

chain = prompt | model | parser
print("\nBy LCEL:\n")
result = chain.invoke({"topic": "Python"})

print(result)