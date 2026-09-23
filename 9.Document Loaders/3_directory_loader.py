from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='9.Document Loaders/Directory',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

# docs = loader.load()
# print("Total documents/pages:", len(docs))
# print(docs[7].page_content)
# print(docs[7].metadata)

docs = loader.lazy_load()

for document in docs:
    print(document.metadata)


# Directory
#    ↓
# Find all PDFs
#    ↓
# PyPDFLoader processes each PDF
#    ↓
# Each PDF is split into page Documents
#    ↓
# All Documents go into one list