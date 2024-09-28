import streamlit as st
import requests

# Function to fetch news articles
def fetch_news(api_key, category):
    base_url = "https://newsapi.org/v2/top-headlines"
    params = {
        'category': category,
        'apiKey': api_key,
        'language': 'en',  # You can change the language if needed
    }
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        return response.json()['articles']
    else:
        st.error("Error fetching news. Please check the category or API key.")
        return None

# Streamlit application
st.title("News Aggregator")
st.write("Fetch the latest news articles based on your preferences.")

# Input for API key
api_key = "226e3dde4bea489586c585251cb7b293"  # Your API key

# Select news category
category = st.selectbox("Select a category:", 
                        ["business", "entertainment", "general", "health", "science", "sports", "technology"])

if st.button("Get News"):
    articles = fetch_news(api_key, category)
    
    if articles:
        for article in articles:
            st.subheader(article['title'])
            st.write(article['description'])
            st.write(f"[Read more]({article['url']})")
            st.write("---")  # Separator
