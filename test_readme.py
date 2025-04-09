from google import genai
import pytest
import os

# 🔐 Load Gemini API key from environment
API_KEY = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    raise EnvironmentError("Missing GOOGLE_API_KEY environment variable.")

# 🤖 Create Gemini client
client = genai.Client(api_key=API_KEY)


# 📄 Load README content
@pytest.fixture(scope="session")
def readme_content():
    try:
        with open("README.md", "r") as f:
            return f.read()
    except FileNotFoundError:
        pytest.fail("README.md not found in the project root.")


# 🧠 Ask LLM a yes/no question about the README
def ask_llm(readme, question):
    prompt = f"""
You are an expert at evaluating README files.
Based on the following README, answer with only "Yes" or "No".

README:
{readme}

Question:
{question}
"""
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=prompt
    )
    return response.text.strip().lower()


# 🧪 Test 1: Project description present?
def test_project_description(readme_content):
    result = ask_llm(
        readme_content, "Does this README clearly explain what the project is for?"
    )
    assert result == "yes", "❌ Project description is missing or unclear."


# 🧪 Test 2: Installation instructions included?
def test_installation_instructions(readme_content):
    result = ask_llm(readme_content, "Does it include installation instructions?")
    assert result == "yes", "❌ Installation instructions are missing."


# 🧪 Test 3: Usage examples included?
def test_usage_examples(readme_content):
    result = ask_llm(readme_content, "Does it provide usage examples?")
    assert result == "yes", "❌ Usage examples are missing."


# 🧪 Test 4: License info included?
def test_license_info(readme_content):
    result = ask_llm(readme_content, "Does it include license information?")
    assert result == "yes", "❌ License information is missing."


# 🧪 Test 5: Screenshot or live demo present?
def test_screenshot_or_demo(readme_content):
    result = ask_llm(
        readme_content, "Does it include a screenshot or a link to a live demo?"
    )
    assert result == "yes", "❌ Screenshot or demo link is missing."
