import openai
import os
from dotenv import load_dotenv




load_dotenv()


api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

# Print the API key to verify it is loaded correctly (for debugging purposes)
print(f"OpenAI API Key: {api_key}")

def extract_info(prompt):
    try:
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=100
        )
        
        reply = response.choices[0].message.content.strip()
        return reply
    except Exception as e:
        print(f"Error: {e}")
        return None

# Test the function
print(extract_info("Extract the email address from the following text: 'Contact us at support@openai.com'"))

















