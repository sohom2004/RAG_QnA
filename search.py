import argparse
from langchain_chroma import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

PROMPT_TEMPLATE = """
Answer the question based only on the following context.
{context}

---
Answer the question based on the above context: {query}
"""

def query_per_document(db, query_string, k=3):
    results = db.similarity_search_with_relevance_scores(query_string, k=k)
    if len(results) == 0 or results[0][1] < 0.55:
        return "No results found."
    
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    responses = []
    for doc, _score in results:
        prompt = prompt_template.format(context=doc.page_content, query=query_string)
        response = llm.invoke(prompt)
        responses.append({
            "response": response.content,
            "source": doc.metadata.get("source", None)
        })
    
    formatted_response = "\n\n".join([f"Response: {r['response']}\nSource: {r['source']}" for r in responses])
    return formatted_response

def main():
    parser = argparse.ArgumentParser(description="Interactive QA terminal using Chroma + Gemini.")
    parser.add_argument("--persist_directory", type=str, default="./chroma", help="Path to Chroma persist directory.")
    args = parser.parse_args()
    
    global llm
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.1)
    embedding_function = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

    db = Chroma(persist_directory=args.persist_directory, embedding_function=embedding_function)
    
    print("Enter your question (type 'exit' to quit):\n")
    
    while True:
        query_string = input("👉 Your query: ")
        if query_string.strip().lower() in ['exit', 'quit', 'q']:
            print("\n👋 Exiting. See you next time!")
            break
        result = query_per_document(db, query_string)
        print("\n=== Query Result ===\n")
        print(result)
        print("\n====================\n")
    
if __name__ == "__main__":
    main()