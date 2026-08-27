# 📚 Generative AI & Machine Learning — Notes & Practice

A personal learning repository containing hands-on code, experiments, and notes as I work through **Machine Learning**, **NLP**, and **Generative AI / LLM** concepts.

> ⚠️ This repo is for learning purposes only. Code here is exploratory and not production-ready.

---

## 🧠 Topics Covered

### Machine Learning
- NumPy & Pandas fundamentals
- Data preprocessing & train/test splitting
- Linear & logistic regression
- Decision trees & random forests
- Classification & evaluation metrics (confusion matrix, classification report)
- Sentiment analysis on IMDB dataset

### Generative AI / LLMs (LangChain + Gemini)
- Chatting with LLMs using `SystemMessage` / `HumanMessage`
- Structured output extraction with Pydantic
- Tool calling / function calling
- Listing and exploring available Gemini models

### RAG Fundamentals
- Sentence embeddings with `sentence-transformers`
- Cosine similarity (manual NumPy implementation)
- Text chunking with `RecursiveCharacterTextSplitter`

---

## 🛠️ Setup

```bash
# 1. Clone the repo
git clone <repo-url>
cd "Generative AI and Machine Learning"

# 2. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your API key (for LLM scripts)
# Create a .env file in the RAG/ folder:
echo GOOGLE_API_KEY=your_key_here > RAG/.env
```

---

## 🔑 API Keys

LLM-related scripts (`RAG/`) use Google Gemini via `langchain-google-genai` and `google-genai`.  
Store your key in a `.env` file — it is already listed in `.gitignore`.

---

## 📦 Key Dependencies

| Library | Purpose |
|---|---|
| `langchain`, `langchain-google-genai` | LLM integration & chaining |
| `langchain-text-splitters` | Document chunking |
| `sentence-transformers` | Local sentence embeddings |
| `google-genai` | Direct Gemini API access |
| `scikit-learn` | ML models & metrics |
| `pandas`, `numpy` | Data manipulation |
| `matplotlib`, `seaborn` | Visualisations |
| `pydantic` | Structured LLM output |
| `python-dotenv` | Environment variable loading |

---

## 📝 Notes

- Models used: **Google Gemini** (via LangChain and the native SDK)
- Embedding model: `all-MiniLM-L6-v2` (runs locally, no API key needed)
- This repo grows alongside my learning — expect rough edges and experiments!
