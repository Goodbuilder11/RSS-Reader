"""
This script fetches and displays the title, link, and description 
of an RSS feed from a given website URL.
"""

import feedparser

def get_valid_url():
    """
    Prompts the user to enter a valid website URL.
    Returns a list of URLs.
    """
    urls = []
    while True:
        url = input("Enter the website URL: (One per line, leave blank to finish): ")
        print("-" * 40)
        if url == "":
            if len(urls) == 0:
                print("No URLs entered. Exiting.")
                return None
            break
        if url.startswith("http://") or url.startswith("https://"):
            urls.append(url)
        else:
            print("Invalid URL. Please enter a valid URL starting with http:// or https://")
    return urls


def website_info(websites):
    """
    Fetches and displays the title, link, and description of the RSS feed
    from the given website URLs.
    """
    for website in websites:
        d = feedparser.parse(website)
        if 'title' in d.feed:
            print("Feed Title:", d.feed.title)
        if 'link' in d.feed:
            print("Feed Link:", d.feed.link)
        if 'description' in d.feed:
            print("Feed Description:", d.feed.description)
        print("-" * 40)


def main():
    """
    Main function to run the RSS feed reader.
    """
    print("Welcome to the RSS Feed Reader!")
    website = get_valid_url()
    website_info(website)
if __name__ == "__main__":
    main()
