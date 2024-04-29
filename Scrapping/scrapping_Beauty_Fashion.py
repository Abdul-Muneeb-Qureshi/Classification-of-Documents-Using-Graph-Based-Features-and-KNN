import requests
from bs4 import BeautifulSoup
import collections
collections.Callable = collections.abc.Callable
from tqdm import tqdm
from process_save_text import save_to_file




def scrape_links(url):

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    blog_urls = soup.find_all('h4', class_= "title")
    links = [blog_url.find('a')['href'] for blog_url in blog_urls]

    return links



def scrape_website(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if request was successful
    if response.status_code == 200:
        # Parse HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract all text from the website
        article = soup.find('div' , class_="container article-content has-padding-top has-padding-bottom")

        text = article.get_text()
        return text
    
    else:
        print("Failed to retrieve website content. Status code:", response.status_code)
        return None

# Main function to orchestrate scraping and saving process
def main():
    url1 =  'https://janeiredale.com/blogs/makeup-blog'
    url2 = 'https://janeiredale.com/blogs/makeup-blog?page=2'
    i = 0
    filename = 'scrapping_Beauty_Fashion.csv'
    links1 = scrape_links(url1)
    links2 = scrape_links(url2)

    links = links1 + links2
    
   
    base_url = "https://janeiredale.com/"
    for link in tqdm(links, desc="Processing links"):
        full_link = base_url + link
        scraped_text = scrape_website(full_link)
        if scraped_text and len(scraped_text.split()) > 500:  # Check if text has more than 500 words
            save_to_file(scraped_text, filename, full_link, "Beauty_Fashion")
            i += 1
if __name__ == "__main__":
    main()
