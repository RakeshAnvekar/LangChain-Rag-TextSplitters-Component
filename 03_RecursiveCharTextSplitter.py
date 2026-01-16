from langchain_text_splitters import RecursiveCharacterTextSplitter

text="""LangChain's RecursiveCharacterTextSplitter is an advanced tool for splitting text using a hierarchical approach. It allows you to define multiple levels of separators, chunk sizes, and overlaps, making it suitable for complex documents that require nuanced splitting strategies."""

splitter= RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20
)

result=splitter.split_text(text)
print(result)
print(len(result))