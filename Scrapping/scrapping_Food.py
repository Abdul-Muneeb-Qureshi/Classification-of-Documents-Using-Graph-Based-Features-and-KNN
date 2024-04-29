import requests
from bs4 import BeautifulSoup
import collections
collections.Callable = collections.abc.Callable
from tqdm import tqdm
from process_save_text import save_to_file




def scrape_links(url):

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    urls=[]

    for i in range(1, 25):
        class_name = f'archive-tile archive-{i}'
        blog_url = soup.find('div', class_= class_name)
        if(blog_url):
            url = blog_url.a['href']
            urls.append(url)

    return urls



def scrape_website(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if request was successful
    if response.status_code == 200:
        # Parse HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract all text from the website
        article = soup.find('div' , class_="recipe-body")

        text = article.get_text()
        return text
    
    else:
        print("Failed to retrieve website content. Status code:", response.status_code)
        return None

# Main function to orchestrate scraping and saving process
def main():
    url =  'https://iamafoodblog.com/tag/chicken'
    i = 0
    filename = 'scrapping_Food.csv'
    links = scrape_links(url)


    
   
    for link in tqdm(links, desc="Processing links"):
        scraped_text = scrape_website(link)
        selected_text = ' '.join(scraped_text.split()[:1000])
        if scraped_text:
            save_to_file(selected_text, filename, link , "Food")
            i += 1
if __name__ == "__main__":
    main()
