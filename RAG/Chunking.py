from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """ Credit risk is the possibility of a borrower defaulting .It includes default risk , concentration risk , and counterparty risk .
Liquidity risk refers to the inability to meet short - term obligations ."""


splitter = RecursiveCharacterTextSplitter(
    chunk_size= 120,
    chunk_overlap = 50
)

chunks = splitter.split_text(text)
for i,c in enumerate(chunks):
    print(f"Chunk {i}: {c[:100]}...")
