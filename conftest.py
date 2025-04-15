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
import re


# 🧹 Extracts the label from a test name by matching a specific pattern (e.g. [])
def clean_label(name: str) -> str:
    match = re.match(r"^test_[^\[]+\[(.+)]$", name)
    return match.group(1) if match else name


# noinspection PyUnusedLocal
# 📝 Generates a summary report for pytest results and writes it to a markdown file
def pytest_terminal_summary(terminalreporter, exitstatus, config):
    summary_file = os.getenv("GITHUB_STEP_SUMMARY")
    if not summary_file:
        return

    checks = []
    for report in terminalreporter.stats.get("passed", []):
        if report.when == "call":
            checks.append((clean_label(report.head_line), True))

    for report in terminalreporter.stats.get("failed", []):
        if report.when == "call":
            checks.append((clean_label(report.head_line), False))

    total = len(checks)
    passed = sum(1 for _, ok in checks if ok)
    score = int((passed / total) * 100) if total > 0 else 0

    with open(summary_file, "a") as f:
        f.write("## 📊 LLM README Report\n\n")
        f.write("| 🧪 Check | Result |\n")
        f.write("|----------|--------|\n")
        for label, ok in checks:
            emoji = "✅ Pass" if ok else "❌ Fail"
            f.write(f"| {label} | {emoji} |\n")
        f.write(f"\n**Overall Score: {score}%** {'🧠' if score >= 80 else '⚠️'}\n")
