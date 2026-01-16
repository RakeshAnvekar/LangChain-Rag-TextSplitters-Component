from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter

loader = PyPDFLoader("text_splitter_explanation.pdf")
documents = loader.load()


splitter=CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20,
    separator='')

result=splitter.split_documents(documents)

print(result)

