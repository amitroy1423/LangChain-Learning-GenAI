from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader



# text = """
# Text Splitter in LangChain
# Working with large documents or unstructured text often creates challenges for language models, as they can only process limited text within their context window. To address this, LangChain provides Text Splitters which are components that segment long documents into manageable chunks while preserving semantic meaning and contextual continuity.
# Purpose: Manage long-form text efficiently by splitting it into meaningful parts.
# Functionality: Helps maintain context, improves semantic retrieval and prevents truncation errors.
# Integration: Works seamlessly with document loaders, vector stores and retrieval pipelines in LangChain.
# Flexibility: Supports various splitting strategies depending on data type — plain text, markdown or token-based text.
# """
loader = PyPDFLoader('10.Text Splitters/Artificial Intelligence.pdf')



docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=0,
    separator=''
)

#result = splitter.split_text(text)
result = splitter.split_documents(docs)

print(result[1].page_content)