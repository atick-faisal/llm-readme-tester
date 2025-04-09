# ⚡ LLM README Tester

<p align="center">
  <img src="https://raw.githubusercontent.com/atick-faisal/llm-readme-tester/main/assets/banner.jpg" alt="LLM README Tester Banner"/>
</p>


<p align="center">
    <a href="https://github.com/atick-faisal/llm-readme-tester/releases">
        <img src="https://img.shields.io/github/release/atick-faisal/llm-readme-tester?colorA=363a4f&colorB=b7bdf8&style=for-the-badge">
    </a>
    <a href="https://github.com/atick-faisal/llm-readme-tester/issues">
        <img src="https://img.shields.io/github/issues/atick-faisal/llm-readme-tester?colorA=363a4f&colorB=f5a97f&style=for-the-badge">
    </a>
    <a href="https://github.com/atick-faisal/llm-readme-tester/contributors">
        <img src="https://img.shields.io/github/contributors/atick-faisal/llm-readme-tester?colorA=363a4f&colorB=a6da95&style=for-the-badge">
    </a>
    <img src="https://img.shields.io/github/actions/workflow/status/atick-faisal/llm-readme-tester/test-action.yml?style=for-the-badge&logo=python&label=tests&colorB=91d7e3&colorA=363a4f" />
</p>

💡 **Turn your README into tested code.**  
This GitHub Action runs *LLM-powered unit tests* on your `README.md` file using Google's **Gemini API**.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## ✅ What it checks

- 📌 Does your README explain what the project is for?
- 🧪 Does it include installation instructions?
- 🧰 Does it provide usage examples?
- 📄 Does it mention a license?
- 📸 Does it include a screenshot or a live demo link?

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## 🚀 Quickstart

Drop this into your workflow to automatically test every README change:

```yaml
- uses: atick-faisal/llm-readme-tester@v1
  with:
    google_api_key: ${{ secrets.GOOGLE_API_KEY }}
```

🔐 Make sure you add your [Gemini API key](https://ai.google.dev/) as a secret named `GOOGLE_API_KEY`.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## 🧪 Example Output

```
test_readme.py ....F                                                     [100%]

FAILED test_readme.py::test_license_info - ❌ License information is missing.
```

<p align="center"><img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/footers/gray0_ctp_on_line.svg?sanitize=true" /></p>
<p align="center"><a href="https://sites.google.com/view/mchowdhury" target="_blank">Qatar University Machine Learning Group</a>
<p align="center"><a href="https://github.com/atick-faisal/Jetpack-Android-Starter/blob/main/LICENSE"><img src="https://img.shields.io/static/v1.svg?style=for-the-badge&label=License&message=Apache 2.0&logoColor=d9e0ee&colorA=363a4f&colorB=b7bdf8"/></a></p>