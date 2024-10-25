import requests

def fetch_blog_feed(blog_url,output_file="output.xml"):

    if not blog_url.endswith("/"):
        blog_url += "/"
    feed_url = blog_url + "feeds/posts/default?alt=atom&max-results=500"


    response = requests.get(feed_url)

    if response.status_code == 200:
        with open(output_file, "w" ,encoding="utf-8") as f:
            f.write(response.text)
        print(f"Data save successfully to {output_file}")
        return response.text  # XML content
    else:
        print(f"Failed to retrieve feed. Status code: {response.status_code}")
        return None


blog_url = "https://guercifzone-ar.blogspot.com/"
xml_data = fetch_blog_feed(blog_url)

if xml_data:
 print(xml_data)