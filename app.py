import os 

import logging
logging.basicConfig(level=logging.DEBUG)


from dotenv import load_dotenv

import streamlit as st
import pandas as pd

from search_api import search_query
from gpt_integration import extract_info


# Load environment variables from .env file
load_dotenv()


api_key = os.getenv("OPENAI_API_KEY")

print(f"OpenAI API Key: {api_key}")


st.title("AI Agent Dashboard")
uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.write("Preview of the Uploaded Data")
    st.dataframe(data.head())


    column = st.selectbox("Select Column for Entity Names", data.columns)
    query_template = st.text_input("Enter Query Template (e.g., 'Get the email of {entity}')")

    if st.button("Start Search"):
        results = []
        for entity in data[column]:
            query = query_template.replace("{entity}", entity)
            search_results = search_query(query)
            info = extract_info(f"Extract the email from: {search_results}")
            results.append([entity, info])

        results_df = pd.DataFrame(results, columns=["Entity", "Extracted Info"])
        st.dataframe(results_df)
        st.download_button("Download CSV", results_df.to_csv(index=False))





 # The GPT query function (additional)
def get_gpt_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=100
        )
        reply = response.choices[0].message.content.strip()
        return reply
    except Exception as e:
        st.error(f"Error: {e}")
        return "Error processing your request."

# Streamlit UI
st.title("GPT-3.5 Turbo Chat App")
user_prompt = st.text_input("Enter your prompt:")
if st.button("Get Response"):
    if user_prompt:
        response = get_gpt_response(user_prompt)
        st.write("GPT Response:")
        st.write(response) 

