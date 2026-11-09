# 🩺 Medical Chatbot

An AI-powered medical question-answering chatbot built using **Retrieval-Augmented Generation (RAG)**. It retrieves relevant information from medical PDF documents and generates context-based responses using a locally running Llama 3.2 model.

---

## 📸 Application Demo

![Medical Chatbot Demo](https://github.com/Malleswari-27/Medical_chatbot/blob/main/screenshots/medical-chatbot-demo.png)

*The chatbot interface showing a user query and an AI-generated response.*

---

## ✨ Features

- 💬 Interactive medical chatbot interface.
- 📚 Answers questions using medical PDF documents.
- 🔍 Semantic search using Pinecone Vector Database.
- 🧠 Context-based response generation using RAG.
- 🤗 Hugging Face sentence embeddings.
- 🦙 Local LLM integration using Ollama (Llama 3.2:3B).
- 🌐 Flask-based web application.
- 🔒 Local LLM inference without requiring a paid LLM API.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.10 | Programming language |
| Flask | Web application framework |
| LangChain | RAG pipeline |
| Pinecone | Vector database |
| Hugging Face | Text embeddings |
| all-MiniLM-L6-v2 | Embedding model |
| Ollama | Local LLM execution |
| Llama 3.2:3B | Answer generation |
| PyPDF | PDF document extraction |
| Bootstrap | Frontend styling |
| HTML, CSS, JavaScript | User interface |

---

## 🏗️ Project Architecture

The application follows a Retrieval-Augmented Generation (RAG) architecture.

### Document Processing and Indexing

1. Medical PDF documents are loaded from the `data/` directory.
2. Text is extracted using PyPDF.
3. Extracted documents are filtered.
4. Text is divided into chunks using RecursiveCharacterTextSplitter.
5. Hugging Face converts text chunks into vector embeddings.
6. Embeddings are stored in Pinecone.

### Question Answering

1. The user submits a medical question through the chatbot interface.
2. Flask receives the question.
3. The question is processed through the RAG pipeline.
4. Pinecone retrieves the three most relevant document chunks.
5. Retrieved context is passed to the Llama 3.2:3B model through Ollama.
6. The generated response is displayed in the chatbot interface.

---

## 📂 Project Structure

```text
Medical_chatbot/
│
├── data/
│   └── Medical_book.pdf
│
├── research/
│
├── src/
│   ├── __init__.py
│   ├── helper.py
│   └── prompt.py
│
├── static/
│   └── style.css
│
├── templates/
│   └── chat.html
│
├── screenshots/
│   └── medical-chatbot-demo.png
│
├── .env
├── .gitignore
├── app.py
├── store_index.py
├── setup.py
├── requirements.txt
├── template.sh
├── LICENSE
└── README.md
```

---

## ⚙️ Prerequisites

Before running the application, make sure you have:

- Python 3.10 installed.
- Git installed.
- Ollama installed.
- Pinecone account and API key.
- Internet connection for downloading dependencies and the embedding model.

---

## 🚀 Installation and Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/Malleswari-27/Medical-chatbot.git
```

Navigate into the project directory:

```bash
cd Medical-chatbot
```

### Step 2: Create a Virtual Environment

```bash
python -m venv myenv
```

Activate the environment.

**Windows:**

```bash
myenv\Scripts\activate
```

**Linux / macOS:**

```bash
source myenv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure Pinecone API Key

1. Create an account at https://www.pinecone.io/
2. Generate your Pinecone API key.
3. Create a `.env` file in the project root directory.

Add the following:

```env
PINECONE_API_KEY=your_pinecone_api_key
```

Replace the placeholder with your actual API key.

**Important:** Never upload your `.env` file or expose your API key on GitHub.

### Step 5: Install and Configure Ollama

Download Ollama:

https://ollama.com/download

Pull the Llama 3.2:3B model:

```bash
ollama pull llama3.2:3b
```

Verify the model:

```bash
ollama list
```

Make sure the Ollama service is running before starting the chatbot.

---

## 🗂️ Medical Document Configuration

Place your medical PDF documents inside the `data/` directory.

Example:

```text
data/
└── Medical_book.pdf
```

The application automatically loads PDF files from this directory when building the vector index.

---

## 🧠 Build the Pinecone Vector Index

Before launching the chatbot for the first time, execute:

```bash
python store_index.py
```

This script:

- Loads medical PDF documents.
- Extracts and splits text.
- Generates embeddings.
- Connects to Pinecone.
- Creates the `medical-chatbot` index if it does not exist.
- Uploads document embeddings to Pinecone.

**Note:** The configured index uses 384-dimensional vectors, cosine similarity, and AWS `us-east-1`.

Wait until the terminal displays:

```text
SUCCESS: Document chunks uploaded to Pinecone.
```

You only need to build the index when setting up the knowledge base or updating its documents.

---

## ▶️ Run the Application

After successfully creating the vector index, start the Flask application:

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:8080
```

You should now see the Medical Chatbot interface.

---

## 🧪 How to Test the Chatbot

Once the application is running:

1. Open the chatbot in your browser.
2. Enter a medical-related question.
3. Click the send button.
4. Wait for the chatbot to retrieve relevant information from Pinecone.
5. Review the generated response.

### Example Test Questions

| Test Case | Example Question |
|---|---|
| General health | What are the common causes of a cold? |
| Symptoms | What are the symptoms of anemia? |
| Diseases | What is diabetes? |
| Medical knowledge | What causes high blood pressure? |
| Follow-up | Can you explain that in simple words? |

**Expected Result:** The chatbot should retrieve relevant medical information from the indexed documents and generate a context-based response.

---

## 🔧 Troubleshooting

| Problem | Possible Solution |
|---|---|
| Missing Pinecone API key | Verify the `.env` file and API key |
| Pinecone index not found | Run `python store_index.py` |
| Ollama connection error | Make sure Ollama is running |
| Model not found | Run `ollama pull llama3.2:3b` |
| Missing Python package | Run `pip install -r requirements.txt` |
| PDF loading error | Verify that PDF files exist inside `data/` |
| No response from chatbot | Check the Flask terminal for errors |

---

## ⚠️ Medical Disclaimer

This project is developed for educational and informational purposes only.

- The chatbot is not a replacement for professional medical advice.
- Generated responses may be incomplete or inaccurate.
- Always consult a qualified healthcare professional for diagnosis and treatment.
- Do not use this application for medical emergencies or clinical decision-making.

---

## 🚧 Future Improvements

- Add support for multiple medical knowledge sources.
- Improve response accuracy and retrieval quality.
- Add conversation history.
- Improve chatbot response formatting.
- Add source citations for retrieved medical information.
- Deploy the application to a cloud platform.

---

## 📄 License

This project is distributed under the license included in the repository. See [LICENSE](LICENSE) for details.

---

## 👨‍💻 Author
P. H V V N S S K Malleswari

GitHub: https://github.com/Malleswari-27
LinkedIn: https://www.linkedin.com/in/padisetti-malleswari-846ke596a7e
Email: malleswaripadisetti@gmail.com

🌟 Show Your Support
If you find this project useful or interesting, please give it a ⭐ on GitHub — it really helps!

**Medical Chatbot Project**
Developed using Python, Flask, LangChain, Pinecone, Hugging Face, and Ollama.

---
