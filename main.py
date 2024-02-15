import requests

question = input("What is your question?")
url = "https://chatgpt-api8.p.rapidapi.com/"

payload = [
    {
        "content": "Hello! I'm an AI assistant bot based on ChatGPT 3. How may I help you?",
        "role": "system"
    },
    {
        "content": question,
        "role": "user"
    }
]

headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": "e15fc80b6amshfb1da622649a231p107513jsn90c9cd535978",
    "X-RapidAPI-Host": "chatgpt-api8.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)

response = response.json()
print(response["text"])