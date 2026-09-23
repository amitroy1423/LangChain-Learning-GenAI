from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('9.Document Loaders/Artificial Intelligence.pdf')

docs = loader.load()

print(len(docs))

print(docs[0].page_content)
print(docs[1].metadata)