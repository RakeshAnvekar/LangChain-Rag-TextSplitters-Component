from langchain_text_splitters import  CharacterTextSplitter

text="""LangChain's CharacterTextSplitter is a versatile tool for splitting text based on character count. It allows you to define chunk sizes and overlaps, making it ideal for processing large documents or preparing text for NLP tasks.""""""LangChain's CharacterTextSplitter is a versatile tool for splitting text based on character count. It allows you to define chunk sizes and overlaps, making it ideal for processing large documents or preparing text for NLP tasks."""

splitter= CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20,
    separator=''
)

result=splitter.split_text(text)
print(result)
print(len(result))
# ['LangChain\'s CharacterTextSplitter is a versatile tool for splitting text based on character