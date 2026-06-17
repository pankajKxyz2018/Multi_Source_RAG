# MULTI SOURCE RAG APPLICATION

# ========================================================================================
# STEP 1: IMPORTING OF FILES OR DOCUMENTS by using langchain_community.documents_loaders
# =======================================================================================

from langchain_community.document_loaders import (
    PyPDFLoader,
    Docx2txtLoader,
    CSVLoader
)
from langchain_google_genai import (
    GoogleGenerativeAIEmbeddings,
    ChatGoogleGenerativeAI)
from langchain_chroma import Chroma


# ========================================================================================
# STEP 2: LOADING OF ALL THE DOCUMENTS
# =======================================================================================

pdf_loader = PyPDFLoader("company_policy.pdf")
pdf_docs = pdf_loader.load()

docx_loader = Docx2txtLoader("employee_handbook.docx")
docx_docs = docx_loader.load()

csv_loader = CSVLoader("employee.csv")
csv_docs = csv_loader.load()

# =========================================================================================
# STEP 3: COMBINING ALL DOCUMENTS
# =========================================================================================

all_documents = pdf_docs + docx_docs + csv_docs

# ========================================================================================
# STEP 4: PRINT EACH DOUMENTS WITH ITS LEN() & ALSO PRINT all_documents with its len()
# =======================================================================================

print("PDF DOCUMENTS:", len(pdf_docs))
print("DOCX DOCUMENTs:", len(docx_docs))
print("CSV DOCUMENTS:", len(csv_docs))
print("TOTAL DOCUMENTS:", len(all_documents))

# ============================================================================================
# STEP 5: VERIFICATION OF ALL DOCUMENTS CONTENT
# ============================================================================================

print(type(all_documents))
print(type(all_documents[0]))
print("\nFIRST DOCUMENT:\n")
print(all_documents[0].page_content[:300])

# ==============================================================================================
# STEP 6: CREATING CHUNKS
# =============================================================================================

from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 500,
    chunk_overlap = 100
)

chunks = splitter.split_documents(all_documents)

print("TOTAL CHUNKS:", len(chunks))
print(type(chunks))
print(type(chunks[0]))

print("\nFIRST CHUNK:\n")
print(chunks[0].page_content[:300])

# ==========================================================================
# STEP 7: VERIFYING THE ABOVE STEPS IN TERMS OF DOCUMENTS 
# ========================================================================

print("\nSECOND CHUNK:\n")
print(chunks[1].page_content)

print("\nTHIRD CHUNK:\n")
print(chunks[2].page_content)

# ========================================================================
# STEP 8: METADATA VIEWING
# ==========================================================================

print(chunks[2].metadata)

print(chunks[0].metadata)

# =============================================================================
# STEP 9: EMBEDDINGS
# ============================================================================

embeddings = GoogleGenerativeAIEmbeddings(
    model = "models/gemini-embedding-001",
    google_api_key="GOOGLE_API_KEY"
)

print("Embedding Object Created")

# =================================================================================
# STEP  10: Create Vector
# =================================================================================

vector = embeddings.embed_query(
    chunks[0].page_content
)

print(type(vector))
print(len(vector))
print(vector[:5])

# ===========================================================================================
# STEP 11: CREATION OF VECTOR DATABASE
# ==========================================================================================

vectorstore = Chroma.from_documents(
    documents = chunks,
    embedding = embeddings
)

print("Vector Store Created")

# ==========================================================================================
# STEP 12: User Query or User Question
# ==========================================================================================

question = input("Enter your query: ")

#  ==========================================================================================
# STEP 13: RETRIEVAL
# =============================================================================================

results = vectorstore.similarity_search(
    question,
    k = 1
)
print("\nTop Retrieved Chunks:\n")
      
for i, doc in enumerate(results):
    print(f"\n----RESULT{i + 1}------")
    print(doc.page_content)

# =================================================================================================
# STEP 14: CREATE CONTEXT
# ==================================================================================================

context = ""

for doc in results:
    context += doc.page_content + "\n\n"

# ====================================================================================================
# STEP 15: GEMINI LLM
# ======================================================================================================

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key="GOOGLE_API_KEY""
)

print("\nLLM Created")

# =======================================================================================================
# STEP 16: BUILD PROMPT
# ==========================================================================================================

prompt = f"""
Answer the question using ONLY the context below.

Context:
{context}

Question:
{question}

Answer:
"""
print("Building Prompt")

# =============================================================================================
# STEP 12 : GENERATION
# ===============================================================================================

response = llm.invoke(prompt)

print("\n========================")
print("FINAL ANSWER")
print("========================\n")

print(response.content)

# ========================================================================
