# SPDX-License-Identifier: Apache-2.0
# Copyright 2025 Atick Faisal
#
# This file is part of LLM README Tester.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at:
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

import pytest
from google import genai

# 🔐 Load Gemini API key from environment
API_KEY: str | None = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    raise OSError("Missing GOOGLE_API_KEY environment variable.")

# 🤖 Create Gemini client
client = genai.Client(api_key=API_KEY)

# 🧩 Available checks (ID: (Label, Question))
AVAILABLE_CHECKS: dict[str, tuple[str, str]] = {
    "description": (
        "Project description",
        "Does this README clearly explain what the project is for?",
    ),
    "install": (
        "Installation instructions",
        "Does it include installation instructions?",
    ),
    "usage": (
        "Usage examples",
        "Does it provide usage examples?",
    ),
    "license": (
        "License information",
        "Does it include license information?",
    ),
    "demo": (
        "Screenshot or demo link",
        "Does it include a screenshot or a link to a live demo?",
    ),
}


# 📄 Load README content
@pytest.fixture(scope="session")
def readme_content() -> str | None:
    try:
        with open("README.md") as f:
            return f.read()
    except FileNotFoundError:
        pytest.fail("README.md not found in the project root.")


# 🧠 Ask LLM a yes/no question about the README
def ask_llm(readme: str, question: str) -> str:
    prompt: str = f"""
        You are an expert at evaluating README files.
        Based on the following README, answer with only "Yes" or "No".

        README:
        {readme}

        Question:
        {question}
    """
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
    )
    return response.text.strip().lower()


# 📦 Dynamically generate tests based on user config
def pytest_generate_tests(metafunc) -> None:
    if "check_key" in metafunc.fixturenames:
        check_input: str = os.getenv("README_TEST_CHECKS", "all").lower()
        if check_input == "all":
            selected_keys: list[str] = list(AVAILABLE_CHECKS.keys())
        else:
            selected_keys = [
                key.strip() for key in check_input.split(",") if key.strip() in AVAILABLE_CHECKS
            ]

        metafunc.parametrize("check_key", selected_keys)


# 🧪 The unified test function
def test_readme_quality(readme_content: str, check_key: str) -> None:
    label, question = AVAILABLE_CHECKS[check_key]
    result = ask_llm(readme_content, question)
    assert result == "yes", f"❌ {label} is missing or unclear."
