import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url="https://ollama.com/v1",
    api_key=os.environ["OLLAMA_API_KEY"],
)

messege_history = []

while True:
    sporsmal = input("Abdullah: ")
     
    messege_history.append({"role": "user", "content": sporsmal})
    if sporsmal == "stop":
        print("Takk for praten")
        break

    response = client.chat.completions.create(
        model="gemma4:31b",
        messages= messege_history,
    )
   
    print("Ollama:", response.choices[0].message.content)
  



"""

import os
from openai import OpenAI

client = OpenAI(
    base_url="https://ollama.com/v1",
    api_key=os.environ["OLLAMA_API_KEY"],
)

response = client.chat.completions.create(
    model="gemma4:31b",
    messages=[{"role": "user", "content": "Say hello in one sentence."}],
)
print(response.choices[0].message.content)

"""
