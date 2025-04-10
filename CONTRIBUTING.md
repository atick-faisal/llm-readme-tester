# 🛠️ Contributing to LLM README Tester

First off, thanks for even considering it — that means you're one of the rare few who cares about
README quality, CI style, and probably uses dark mode.

This project is clean, type-safe, fast, and (so far) bug-free. Let's keep it that way, yeah?

---

## 💡 What You Can Contribute

- New README test cases (`test_readme.py`)
- Cool LLM-powered checks (add them under `AVAILABLE_CHECKS`)
- Code style/tooling improvements (as long as Ruff doesn't cry)
- Docs updates (typos count!)
- Marketplace polish, badge improvements, banner updates — go wild

---

## 🧼 Rules of the Road

1. **Use `uv` for all dependencies.**  
   Don't touch `requirements.txt`. It doesn’t exist anymore for a reason.

2. **Test everything.**  
   Run `pytest` and make sure it doesn’t break other people’s workflows.

3. **Lint it.**  
   Run `ruff check .` and `ruff check . --fix`.  
   If Ruff fails, you fail.

4. **Don't overcomplicate.**  
   This repo is meant to be simple and stylish. If you’re writing 100 lines of logic to check if the
   README has a semicolon, take a walk.

5. **Be nice.**  
   PR comments should be helpful, not spicy. Spicy is my job.

---

## 🧪 Local Dev Setup

```bash
uv pip install .[dev]
pytest
ruff check .
```

You can also use `python test_readme.py` if you're into directness.

---

## 🏷️ Versioning

We follow [semver](https://semver.org/).  
If your PR changes the CLI/inputs/outputs, bump the minor or patch version and update the `v1` tag
if needed.

---

## 📝 Licensing

By contributing, you agree your work will be licensed under [Apache 2.0](./LICENSE). No takebacks.

---

Thanks again, and may your READMEs be clear, your CI green, and your LLM responses `yes`.  
