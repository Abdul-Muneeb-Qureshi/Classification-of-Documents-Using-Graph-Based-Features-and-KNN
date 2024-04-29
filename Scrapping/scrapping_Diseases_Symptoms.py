import requests
from bs4 import BeautifulSoup
import collections
collections.Callable = collections.abc.Callable
from process_save_text import save_to_file
from tqdm import tqdm



# Function to scrape a website and return its text content

def scrape_website(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if request was successful
    if response.status_code == 200:
        # Parse HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract all text from the website
        article = soup.find('article' , class_="small single")

        text = article.get_text()
        return text
    
    else:
        print("Failed to retrieve website content. Status code:", response.status_code)
        return None



# Function to scrape links from a given URL
def scrape_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    h4_tags = soup.find_all('h4', class_='entry-title title')
    links = [h4.find('a')['href'] for h4 in h4_tags]
    return links

# Main function to orchestrate scraping and saving process
def main():
    urls = [
        'https://www.remedieslabs.com/blog/',
        'https://www.remedieslabs.com/blog/page/2/',
        'https://www.remedieslabs.com/blog/page/3/'
    ]
    i = 0
    filename = 'scrapping_Diseases_Symptoms.csv'
    for index, url in enumerate(urls, start=1):
        print(f"Scraping links from {url}...")
        links = scrape_links(url)
        print(f"Page {index} Links Scraped Successfully.")
        for link in tqdm(links, desc=f"Scraping page {index}"):
            scraped_text = scrape_website(link)
            if scraped_text:
                # filename = f"page_{i}.txt"
                save_to_file(scraped_text, filename , link , "Diseases_Symptoms")
                i += 1
        print("Done.\n")

if __name__ == "__main__":
    main()
