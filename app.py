
from flask import Flask, render_template, request
from src.helper import download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain_ollama import ChatOllama
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import *
import os

app = Flask(__name__)

# Load environment variables
load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

if not PINECONE_API_KEY:
    raise ValueError("PINECONE_API_KEY is missing from .env")


os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY

# Load embeddings
embeddings = download_hugging_face_embeddings()

# Connect to Pinecone index
index_name = "medical-chatbot"

docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)

# Retriever
retriever = docsearch.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3}
)

# OpenAI model
llm = ChatOllama(
    model="llama3.2:3b",
    temperature=0.4
)
# Prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{input}")
])

# RAG chain
question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

# Routes
@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/get", methods=["POST"])
def chat():
    msg = request.form.get("msg", "").strip()

    if not msg:
        return "Please enter a question.", 400

    try:
        print("Question received:", msg)
        print("Searching Pinecone and generating answer...")

        response = rag_chain.invoke({"input": msg})

        answer = response.get("answer", "No answer was generated.")
        print("Answer generated successfully.")

        return answer

    except Exception as e:
        app.logger.exception("Chat request failed")
        return f"Error: {str(e)}", 500


# Run app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
