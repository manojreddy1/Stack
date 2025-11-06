import os
import requests
import openai

GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]
PR_NUMBER = os.environ["GITHUB_REF"].split("/")[-1]  # PR number from ref
REPO = os.environ["GITHUB_REPOSITORY"]

headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3.diff"
}

url = f"https://api.github.com/repos/{REPO}/pulls/{PR_NUMBER}"

resp = requests.get(url, headers=headers)
if resp.status_code != 200:
    print(f"Failed to fetch PR diff: {resp.status_code}")
    exit(1)

diff = resp.text
if not diff.strip():
    print("No changes detected in PR.")
    exit(0)

# AI review
openai.api_key = os.environ["OPENAI_API_KEY"]

prompt = f"Review the following code diff:\n\n{diff}"

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "user", "content": prompt}],
    temperature=0
)

print("AI Review:\n", response.choices[0].message.content)
