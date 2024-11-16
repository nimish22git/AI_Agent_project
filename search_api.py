import os
from dotenv import load_dotenv

from serpapi import GoogleSearch

load_dotenv()

serpapi_key = os.getenv("SERPAPI_API_KEY")

def search_query(query):
    params = {
        "q": query,
        "api_key": serpapi_key,
        "engine": "google"
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    return results.get("organic_results", [])



print(f"SerpAPI Key: {serpapi_key}")


print(search_query("Get email address of OpenAI"))