import os
import subprocess
import sys

# Get base and head branches
base_branch = os.environ.get("GITHUB_BASE_REF")
head_branch = os.environ.get("GITHUB_HEAD_REF")

if not base_branch or not head_branch:
    print("Missing branch information from environment.")
    sys.exit(1)

# Fetch both branches explicitly
subprocess.run(["git", "fetch", "origin", base_branch], check=True)
subprocess.run(["git", "fetch", "origin", head_branch], check=True)

# Get the merge-base commit
merge_base = subprocess.check_output(
    ["git", "merge-base", f"origin/{base_branch}", f"origin/{head_branch}"]
).decode("utf-8").strip()

# Compute diff from merge-base to HEAD
diff = subprocess.check_output(
    ["git", "diff", f"{merge_base}..origin/{head_branch}"]
).decode("utf-8")

if not diff.strip():
    print("No changes detected in PR.")
    sys.exit(0)

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
