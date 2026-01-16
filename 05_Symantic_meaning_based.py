from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai import OpenAIEmbeddings

# Initialize embeddings
embeddings = OpenAIEmbeddings()

#we break in to chunks, we remove the embedding for the entire embedding, we take semantic meaning based chunks,
#find the standard deviation or percentile of the distances between embeddings of chunks,
#and we break the text at those points where the distance between embeddings is higher than the threshold
# Create semantic chunker
text_splitter = SemanticChunker(
    embeddings=embeddings,
    breakpoint_threshold_type="percentile",  # or "standard_deviation"
    breakpoint_threshold_amount=1 #
)

text = """
Farmers were working hard in the fields, preparing the soil and planting seeds.
The Indian Premier League (IPL) is the biggest cricket league in the world.

Terrorism is a big danger to peace and safety.
"""

# Split text
chunks = text_splitter.split_text(text)

for i, chunk in enumerate(chunks, start=1):
    print(f"Chunk {i}:\n{chunk}\n")
