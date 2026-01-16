from langchain_text_splitters import RecursiveCharacterTextSplitter,Language

pythoon_code = """class AskRequest(BaseModel):
    url: str
    content: str
    question: str


# -------- Normalize follow-up / fragment questions --------
def normalize_question(question: str, conversation: list) -> str:   
   
    words = question.strip().split()

    if len(words) < 6 and conversation:
        last_user_question = None

        for msg in reversed(conversation):
            if msg["role"] == "user":
                last_user_question = msg["content"]
                break

        if last_user_question:
            return (
                f"Based on the previous question: '{last_user_question}', "
                f"answer the following follow-up question: {question}"
            )

    return question
"""

splitter= RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=200,
    chunk_overlap=0,
)
result=splitter.split_text(pythoon_code)
print(result)
print(len(result))