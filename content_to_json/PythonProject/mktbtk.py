import requests
from bs4 import BeautifulSoup
import json

# Step 1: Fetch the website content
url = ""
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Step 2: Extract data (e.g., title, links, and post content)
title = soup.title.string  # Get the title of the page
#links = [{"text": a.get_text(), "url": a['href']} for a in soup.find_all('a', href=True)]

# Extract post content - Update the class or tag to match the target website
post_content = ''
post_container = soup.find('div', class_='post-content')  # Adjust this as needed
if post_container:
    paragraphs = post_container.find_all('p')
    post_content = '\n'.join([p.get_text(strip=True) for p in paragraphs])

# Step 3: Create JSON data
data = {
    "title": title,
    "post_content": post_content
}

# Step 4: Convert to JSON and save to file
with open('post_content.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)

print("Data saved to post_content.json")
