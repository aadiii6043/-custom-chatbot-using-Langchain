from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from langchain_chroma import Chroma  # ✅ Corrected Import
from langchain_huggingface import HuggingFaceEmbeddings  # ✅ Updated Import
import os

# ✅ Use a Free Hugging Face Embedding Model
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# ✅ Load the Vector Database (ChromaDB) using absolute path
db_path = os.path.abspath("./chroma_db")
vector_db = Chroma(persist_directory=db_path, embedding_function=embeddings)

print(f"✅ Vector Store Loaded with {vector_db._collection.count()} documents")

app = Flask(__name__)
api = Api(app)

# ✅ Home Route for Testing
@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Chatbot API! Use the /chat endpoint to chat."})

class Chatbot(Resource):
    def post(self):
        data = request.get_json()
        user_query = data.get("query", "")

        print(f"📝 Received query: {user_query}")

        try:
            results = vector_db.similarity_search(user_query, k=3)  # Get 3 best matches
            print(f"🔎 Raw Results: {results}")  # Debugging output

            if results:
                # ✅ Split courses properly into a list
                response = []
                for doc in results:
                    response.extend(doc.page_content.split("\n"))  # Split by newline
            else:
                response = ["Sorry, I couldn't find a relevant answer."]
        except Exception as e:
            response = [f"⚠️ Error in similarity search: {e}"]
        
        print(f"📢 Response: {response}")
        return jsonify({"response": response})

api.add_resource(Chatbot, "/chat")

if __name__ == "__main__":
    app.run(debug=True)