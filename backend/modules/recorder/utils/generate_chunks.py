from langchain.text_splitter import CharacterTextSplitter

def generate_chunks(text:str) -> list[str]:
  text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
  return text_splitter.split_text(text)
