from langchain.text_splitter import CharacterTextSplitter  
from langchain.text_splitter import RecursiveCharacterTextSplitter, Language



def split_text_into_chunks(long_string, num_tokens):

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=num_tokens, chunk_overlap=20)  

    documents = text_splitter.create_documents([long_string])

    chunks = [doc.page_content for doc in documents]

    # Print out the number of tokens in each chunk
    for i, chunk in enumerate(chunks, 1):
        print(f"Chunk {i} has {len(chunk)} tokens.")

    return chunks
