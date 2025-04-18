import requests
from rich import print
from rich.markdown import Markdown

# Create the API URL
ai_api_key = "424369doa037d0347bft3cfcc8cef956"
ai_context = "You are a renowned Italian chef who has specialized in writing easy-to-follow recipes for your magazine."
ai_prompt = f"Please give me a formatted recipe for Carbonara Pasta. Please make it concise and simple, summarized and straight to the point, in less than 10 steps. Do not add a title for each step. Thanks!"
ai_api_url = f"https://api.shecodes.io/ai/v1/generate?prompt={ai_prompt}&context={ai_context}&key={ai_api_key}"

# Call the request
response = requests.get(ai_api_url)

# Handle the response
response_data = response.json()
markdown_data = Markdown(response_data['answer'])

# Display answer
print(markdown_data)