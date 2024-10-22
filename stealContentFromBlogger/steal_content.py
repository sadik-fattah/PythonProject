import requests
from bs4 import BeautifulSoup


def scrape_blog_posts(blog_url):
    page_number = 1
    all_posts = []

    while True:
        # Construct paginated URL
        url = f"{blog_url}/search?updated-max&start={page_number * 1}&max-results=10"
        print(f"Scraping: {url}")

        response = requests.get(url)
        if response.status_code != 200:
            print("Failed to retrieve data.")
            break

        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all post titles or links (adjust based on the blog's structure)
        posts = soup.find_all('h3', class_='post-title')

        if not posts:
            print("No more posts found.")
            break

        for post in posts:
            title = post.get_text(strip=True)
            link = post.find('a')['href']
            all_posts.append({'title': title, 'link': link})

        page_number += 1

    return all_posts


# Usage
blog_url = "https://manga-ai-land.blogspot.com/"  # Replace with the actual blog URL
posts = scrape_blog_posts(blog_url)

# Display the results
for post in posts:
    print(f"Title: {post['title']}, Link: {post['link']}")
