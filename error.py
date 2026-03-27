import sys
import ollama

if len(sys.argv) < 2:
    print("Usage: python3 error.py <logfile>")
    sys.exit(1)

with open(sys.argv[1], "r") as f:
    logs = f.read()

response = ollama.chat(
    model='llama3',
    messages=[
        {
            'role': 'user',
            'content': f"""
You are a DevOps expert.
Analyze the error and give a clear fix.

Error:
{logs}
"""
        }
    ]
)

print("\n🤖 Local AI Solution:\n")
print(response['message']['content'])
