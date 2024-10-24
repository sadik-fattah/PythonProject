import requests

def fetch_blog_feed(blog_url):
    # Ensure the URL format is correct
    if not blog_url.endswith("/"):
        blog_url += "/"
    feed_url = blog_url + "feeds/posts/default?alt=rss"

    # Make the request to the feed URL
    response = requests.get(feed_url)

    if response.status_code == 200:
        print("Feed successfully retrieved!")
        return response.text  # XML content
    else:
        print(f"Failed to retrieve feed. Status code: {response.status_code}")
        return None

# Example Usage
blog_url = "https://guercifzone-ar.blogspot.com/"  # Replace with your blog's URL
xml_data = fetch_blog_feed(blog_url)

if xml_data:
    # Output the XML data
    print(xml_data)