import os
import openai
import subprocess
import requests
import json

openai.api_key = os.environ["OPENAI_API_KEY"]
github_token = os.environ["GITHUB_TOKEN"]
repo = os.environ["GITHUB_REPOSITORY"]
pr_number = os.environ["GITHUB_REF"].split("/")[-2]

# Get the git diff for the PR
diff = subprocess.check_output(["git", "diff", "origin/main...HEAD"]).decode("utf-8")

prompt = f"""
You are an expert iOS developer reviewing a pull request.
Here is the diff. Provide:
1. A short summary of the main changes.
2. Potential bugs or logical errors.
3. Style or readability improvements.
4. Suggestions for better Swift practices.

Diff:
{diff}
"""

response = openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.2,
)

review_text = response.choices[0].message.content.strip()

# Post comment to GitHub PR
api_url = f"https://api.github.com/repos/{repo}/issues/{pr_number}/comments"
headers = {"Authorization": f"token {github_token}"}
requests.post(api_url, headers=headers, json={"body": review_text})
