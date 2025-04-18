import requests
from rich import print
from rich.markdown import Markdown

# User input
city = input("Enter a city to know the top 3 restaurants in this city: ")

# Create the API URL
ai_api_key = "424369doa037d0347bft3cfcc8cef956"
ai_context = "You are a renowned chef who has traveled around the world trying to find the best restaurants in the world."
ai_prompt = f"Please give me a formatted list of the 3 top restaurants in {city}. Use the following for the title: Top 3 Restaurants in {city}. Make sure to add an emoji after the name of the restaurant, and a quick description of the restaurant under the name. Thanks!"
ai_api_url = f"https://api.shecodes.io/ai/v1/generate?prompt={ai_prompt}&context={ai_context}&key={ai_api_key}"

# Call the request
response = requests.get(ai_api_url)

# Handle response
response_data = response.json()
markdown_data = Markdown(response_data['answer'])

# Display data
print(markdown_data)