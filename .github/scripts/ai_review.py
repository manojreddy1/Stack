import os
import subprocess

# Use base branch from environment
base_branch = os.environ.get("GITHUB_BASE_REF", "main")

# Fetch base branch explicitly (safety)
subprocess.run(["git", "fetch", "origin", base_branch], check=True)

# Compute diff between base branch and PR HEAD
diff = subprocess.check_output(
    ["git", "diff", f"origin/{base_branch}...HEAD"]
).decode("utf-8")

if not diff.strip():
    print("No changes detected in PR.")
    exit(0)

# Call AI (example)
import openai

openai.api_key = os.environ["OPENAI_API_KEY"]

prompt = f"Review the following iOS Swift code diff and suggest improvements:\n\n{diff}"

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "user", "content": prompt}],
    temperature=0
)

review_text = response.choices[0].message.content
print("AI Review:\n", review_text)
