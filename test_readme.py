from google import genai
import pytest
import os

API_KEY = os.getenv("GOOGLE_API_KEY")
client = genai.Client(api_key=API_KEY)


# Load README
@pytest.fixture(scope="session")
def readme_content():
    with open("README.md", "r") as f:
        return f.read()


# Ask Gemini (v2) a yes/no question
def ask_llm(readme, question):
    prompt = f"""
You are a helpful assistant who evaluates README files.
Based on the following README, answer with only "Yes" or "No".

README:
{readme}

Question:
{question}
"""
    response = client.models.generate_content(
        model="gemini-2.0-flash-001", contents=prompt
    )
    return response.text.strip().lower()


# --- TEST CASES ---


def test_project_description(readme_content):
    result = ask_llm(
        readme_content, "Does this README clearly explain what the project is for?"
    )
    assert result == "yes", "Project description is missing or unclear."


def test_installation_instructions(readme_content):
    result = ask_llm(readme_content, "Does it include installation instructions?")
    assert result == "yes", "Installation instructions are missing."


def test_usage_examples(readme_content):
    result = ask_llm(readme_content, "Does it provide usage examples?")
    assert result == "yes", "Usage examples are missing."


def test_license_info(readme_content):
    result = ask_llm(readme_content, "Does it include license information?")
    assert result == "yes", "License information is missing."
