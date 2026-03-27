import sys
import ollama

if len(sys.argv) < 2:
    print("Usage: python3 error.py <logfile>")
    sys.exit(1)

with open(sys.argv[1], "r") as f:
    logs = f.read()

response = ollama.chat(
    model='llama3',
    host='http://host.docker.internal:11434',  # IMPORTANT
    messages=[
        {
            'role': 'user',
            'content': f"""
You are a senior DevOps engineer.

Analyze the error log and:
1. Identify the root cause
2. Explain clearly
3. Give exact fix (commands/code)

Error log:
{logs}
"""
        }
    ]
)

print("\nAI Solution:\n")
print(response['message']['content'])
