import requests
from bs4 import BeautifulSoup
import collections
collections.Callable = collections.abc.Callable
from tqdm import tqdm
from process_save_text import save_to_file




def scrape_links(url):

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    li_tags = soup.find_all('li', class_='listing-item')
    links = [li.find('a')['href'] for li in li_tags]

    return links



from bs4 import BeautifulSoup
import requests

def scrape_website(url):
    # Send a GET request to the URL
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    
    # Check if request was successful
    if response.status_code == 200:
        # Parse HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the entry-content div
        entry_content_div = soup.find('div', class_="entry-content")
        
        # Initialize text
        text = ''
        
        # Extract text from paragraphs and headings in sequence
        for child in entry_content_div.children:
            if child.name == 'p':
                text += child.get_text() + '\n'
            elif child.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                text += child.get_text() + '\n'
            elif child.name == 'span':
                text += child.get_text() + '\n'
        
        return text.strip()  # Remove leading and trailing whitespace
    else:
        print("Failed to retrieve website content. Status code:", response.status_code)
        return None

# Main function to orchestrate scraping and saving process
def main():
    url =  'https://www.flourandspiceblog.com/category/desserts/'
    i = 0
    filename = 'scrapping_Food2.csv'
    links = scrape_links(url)
    
   
    for link in tqdm(links, desc="Processing links"):
        scraped_text = scrape_website(link)
        selected_text = ' '.join(scraped_text.split()[8:1008])  # Limit to first 1000 words
        if scraped_text and len(scraped_text.split()) > 500:  # Check if non-empty and more than 500 words
            save_to_file(selected_text, filename, link, "Food")
            i += 1
      
if __name__ == "__main__":
    main()
