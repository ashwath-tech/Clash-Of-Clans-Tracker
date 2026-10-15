# all things about rag
from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_text(text, chunk_size=500):
  """
  Splits the input text into chunks of specified size.
  """
  text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=0)
  texts = text_splitter.split_text(text)
  return texts

if __name__ == "__main__":
    document = "This is a sample text that will be split into chunks. " * 20
    chunk_text(document, chunk_size=100)
