import requests

word = input("Please enter a word in any language: ")
# Create the API URL
ai_api_key = "424369doa037d0347bft3cfcc8cef956"
ai_context = "You are an experienced and renowned polyglot who knows all the languages in the world."
ai_prompt = f"What language does the word {word} belongs to? Please, make sure to only display the language, followed by an emoji with the flag associated to that language. Thanks!"
ai_api_url = f"https://api.shecodes.io/ai/v1/generate?prompt={ai_prompt}&context={ai_context}&key={ai_api_key}"

# Call the request
response = requests.get(ai_api_url)

# Handle the response
response_data = response.json()

# Display answer
print(response_data['answer'])