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

def print_entries(entries):
    """
    Prints the title, link, description, and published date of each entry in the RSS feed.
    """
    if entries and len(entries) > 0:
        print(f"{len(entries)} entries found in the RSS feed:")
        show_entries = input("Would you like to print all the entries? [y/n]: ")
        if show_entries.lower() == 'y':
            print("Entries:")
            for entry in entries:
                if entry.get('title'):
                    print("Entry Title:", entry.title)
                if entry.get('link'):
                    print("Entry Link:", entry.link)
                if entry.get('description'):
                    print("Entry Description:", entry.description)
                if entry.get('published'):
                    print("Entry Published:", entry.published)
                print("-" * 40)
    else:
        print("No entries found in the RSS feed.")
    print("-" * 40)


def website_info(websites):
    """
    Fetches and displays the title, link, and description of the RSS feed
    from the given website URLs.
    """
    for website in websites:
        d = feedparser.parse(website)
        if 'feed' in d:
            if 'title' in d.feed:
                print("Feed Title:", d.feed.title) # type: ignore
            if 'link' in d.feed:
                print("Feed Link:", d.feed.link) # type: ignore
            if 'description' in d.feed:
                print("Feed Description:", d.feed.description) # type: ignore
            print("-" * 40)
            print_entries(d.entries)
        else:
            print("Invalid RSS feed.")
        print("-" * 40)


def main():
    """
    Main function to run the RSS feed reader.
    """
    print("Welcome to the RSS Feed Reader!")
    website = get_valid_url()
    if website:
        website_info(website)
    else:
        print("Please enter a valid link.")
if __name__ == "__main__":
    main()
    