import requests

def joke():
    api = "https://official-joke-api.appspot.com/random_joke"
    reponse = requests.get(api).json()
    return f"{reponse["setup"]}\n{reponse['punchline']}"

print(joke())
