import ollama

stream = ollama.chat(
    model='llama3.2:3b',
    messages=[{'role': 'user', 'content': 'Explain simply the main benefits of a cloud dev environment to try out new dev tools in your browser'}],
    stream=True,
)

print("llama3.2 response:")

for chunk in stream:
  print(chunk['message']['content'], end='', flush=True)
