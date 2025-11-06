import os
import subprocess

base_branch = os.environ.get("GITHUB_BASE_REF", "main")

# Ensure the base branch exists locally
subprocess.run(["git", "fetch", "origin", base_branch], check=True)

# Show all branches for debugging
subprocess.run(["git", "branch", "-a"], check=True)

# Compute diff
try:
    diff = subprocess.check_output(["git", "diff", f"origin/{base_branch}...HEAD"]).decode("utf-8")
except subprocess.CalledProcessError as e:
    print("Error computing diff:", e)
    exit(1)

if not diff.strip():
    print("No changes detected in PR.")
    exit(0)

# AI review example
import openai
openai.api_key = os.environ["OPENAI_API_KEY"]

prompt = f"Review the following code diff:\n\n{diff}"
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "user", "content": prompt}],
    temperature=0
)

print("AI Review:\n", response.choices[0].message.content)
