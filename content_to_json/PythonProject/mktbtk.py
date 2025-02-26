import requests
from bs4 import BeautifulSoup
import json


url = ""
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')


title = soup.title.string  # Get the title of the page

post_content = ''
post_container = soup.find('div', class_='post-content')
if post_container:
    paragraphs = post_container.find_all('p')
    post_content = '\n'.join([p.get_text(strip=True) for p in paragraphs])

# Step 3: Create JSON data
data = {
    "title": title,
    "post_content": post_content
}


with open('post_content.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)

print("Data saved to post_content.json")
