# **LangChain Chatbot API for Technical Courses**

## **Overview**
This project is a **RESTful API** designed to provide conversational responses based on technical course data from **Brainlox**. It leverages **LangChain** for natural language processing and vector similarity search to return relevant course information based on user queries.

The API allows users to:
- Extract course data from **Brainlox**.
- Create embeddings and store them in a **vector database**.
- Query the API with natural language questions to get relevant course information.

The API is built using **Flask** and **LangChain** with **Hugging Face** embeddings.

---

## **Features**

1. **Data Extraction (Web Scraping):**
   - Scrapes course data from **[Brainlox Technical Courses](https://brainlox.com/courses/category/technical)**.
   - Extracts course titles, descriptions, and prices for further processing.

2. **Vector Store Creation (`POST /vector_store`):**
   - Generates embeddings using **Hugging Face models**.
   - Stores the embeddings in **ChromaDB** for efficient similarity search.

3. **Chatbot API (`POST /chat`):**
   - Accepts JSON input with a user query.
   - Returns the most relevant course information based on vector similarity search.

---

## **Technologies Used**

- **Python:** Programming language for the API.
- **Flask:** Framework for building the RESTful API.
- **LangChain:** Framework for building language-based applications.
- **Hugging Face Transformers:** Free embedding models for natural language processing.
- **ChromaDB:** Vector database for efficient similarity search.
- **BeautifulSoup:** Web scraping library to extract course data.
- **pandas:** Data processing and manipulation.

---

## **How to Use**

2. **Create a Virtual Environment & Install Dependencies**  
For **Windows**:  
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

3. **Run the Vector Store Creation**  
This will scrape the data, generate embeddings, and store them in **ChromaDB**.  
```bash
python vectorstore/vector_store.py
```

4. **Start the Flask API**  
This will start the API on `http://127.0.0.1:5000`.  
```bash
python api/chatbot_api.py
```

5. **Make a POST Request to the Chatbot API**  
Use **curl** or any API client like **Postman** to test the API.  
```bash
curl -X POST "http://127.0.0.1:5000/chat" -H "Content-Type: application/json" -d '{"query": "What courses are available?"}'
```

---

## **Example API Responses**

### **POST `/chat` Request:**
```json
{
  "query": "What courses are available?"
}
```

### **Response:**
```json
{
  "response": [
    "LEARN SCRATCH PROGRAMING: $30",
    "LEARN CLOUD COMPUTING BASICS-AWS: $30",
    "LEARN MOBILE DEVELOPMENT: $30",
    "LEARN CORE JAVA PROGRAMMING ONLINE: $30",
    "LEARN ROBOTICS: $30"
  ]
}
```

---

## **Project Structure**

```
/Project
│
├── api
│   └── chatbot_api.py              # Flask REST API for chatbot
│
├── scraper
│   ├── __init__.py                 # Marks scraper as a package
│   └── scraper.py                  # Scrapes Brainlox courses
│
├── vectorstore
│   └── vector_store.py             # Creates embeddings and stores in ChromaDB
│
├── chroma_db                       # Directory storing vector embeddings (generated, do not push)
│
├── requirements.txt                # Project dependencies
└── README.md                       # Project overview and usage instructions
```

---

## **Contributing**

We welcome contributions to improve this project. To contribute:

1. **Fork** the repository.
2. **Create** a new branch:
   ```bash
   git checkout -b feature-branch
   ```
3. **Make your changes** and commit them:
   ```bash
   git commit -m "Add your message"
   ```
4. **Push** to the branch:
   ```bash
   git push origin feature-branch
   ```
5. Open a **Pull Request**.

---

## **License**

This project is open-source and available under the **MIT License**.
