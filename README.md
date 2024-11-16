# AI_Agent_project
AN AI Agent machine which gives details and replies to the prompt asked from an uploaded CSV file or google sheet

Description:
The AI Agent Project is an intelligent system built to automate tasks using AI-based models and APIs. The project integrates various components like GPT-based text generation, Google Sheets API for data management, and a custom search API. The agent leverages these tools to perform tasks that require natural language understanding and decision-making.

Features:
GPT Integration: Leverages OpenAI's GPT model for natural language understanding and text generation.
Google Sheets Integration: Automates interactions with Google Sheets to retrieve and store data.
Custom Search API: A custom-built API to perform search queries and return relevant results based on specific inputs.
Environment Configuration: Secure handling of API keys and credentials via .env and JSON configuration files.
Chat 3.5 turbo chat: For further queries to be asked while working on the Google sheets/CSV file 

Prerequisites:
Before running the project, make sure to have the following installed:

Python 3.x
pip (Python package installer)
Access to OpenAI API keys and Google Cloud Service credentials
Install the required Python dependencies (listed below)

Installation:
Clone this repository to your local machine:
Copy code
git clone https://github.com/nimish22git/AI_Agent_project.git
cd AI_Agent_project/Backend
pip install openai
pip install serpapi
pip install streamlit

Set up the environment variables:

Create a .env file in the root of the project and add your API keys and configuration values like below:

makefile
Copy code
OPENAI_API_KEY=your-openai-api-key
GOOGLE_API_KEY=your-google-api-key

Service Account JSON:
Add your Google Cloud Service Account credentials in the xxxx-xxxx-xxxxxxxxxxxx.json file. Make sure this file is secure and added to .gitignore to prevent it from being uploaded to GitHub.

Usage
Once the configuration is set up, run the project using:

Copy code
python app.py
This will start the AI Agent, and it will begin interacting with the APIs to perform its tasks.

Project Structure
The project is organized as follows:

AI_Agent_project/
├── Backend/
│   ├── app.py               # Main entry point for the application
│   ├── gpt_integration.py   # GPT-based interaction script
│   ├── search_api.py        # Custom search API functionality
│   ├── sheets_api.py        # Google Sheets API integration
│   ├── .env                 # Environment configuration file (DO NOT push to GitHub)
│   ├── prj-ai-agent-441303-g1-84adf963ac9d.json  # Google Cloud Service Account Credentials (DO NOT push to GitHub)
│   ├── requirements.txt     # List of dependencies
│   ├── __pycache__/         # Compiled Python files (auto-generated)
|   ├── .gitignore           # Git ignore file

Contributing
Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make changes and commit (git commit -am 'Add new feature').
Push to the branch (git push origin feature-branch).
Create a pull request to merge changes into the main branch.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
OpenAI for providing the GPT model.
Google Cloud for the Sheets API.
All contributors and open-source libraries used in this project.

Next Steps:
Add actual details where placeholders like your-openai-api-key are mentioned.
Ensure that sensitive files like .env and .json are not included in your GitHub repository by double-checking your .gitignore.
