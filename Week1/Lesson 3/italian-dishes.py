import requests
from rich import print
from rich.markdown import Markdown

# Create the API URL
ai_api_key = "424369doa037d0347bft3cfcc8cef956"
ai_context = "You are a renowned Italian chef who has specialized in writing easy-to-follow recipes for your magazine."
ai_prompt = f"Please only give me a list of 5 italian recipes. Make sure to order them alphabetically, capitalize every word and add an emoji in front of each recipe representing that dish. Also, separate each dish with a ;. Example: 🍝 Bolognese; . Thanks!"
ai_api_url = f"https://api.shecodes.io/ai/v1/generate?prompt={ai_prompt}&context={ai_context}&key={ai_api_key}"

# Send request
response = requests.get(ai_api_url)

# Handle response
response_data = response.json()

# Display answer
print(response_data['answer'])