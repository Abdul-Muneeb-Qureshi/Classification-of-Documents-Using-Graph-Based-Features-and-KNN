import csv
import string
import re
import collections
collections.Callable = collections.abc.Callable
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer


def preprocess_text(text):
    # Tokenization
    tokens = word_tokenize(text.lower())
    
    # Removing punctuation
    tokens = [token for token in tokens if token not in string.punctuation]
    
    # Removing stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]
    
    # Stemming
    stemmer = SnowballStemmer("english")
    tokens = [stemmer.stem(token) for token in tokens]
    
    return tokens


def save_to_file(text, filename , link , category):
    cleaned_text = re.sub(r'\s+', ' ', text) 
    cleaned_text = re.sub(r'[^\w\s]', '', cleaned_text)  

    stemmed_text = preprocess_text(cleaned_text)
    
    # Writing to CSV in append mode
    with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        # Checking if the file is empty to write the header row
        if csvfile.tell() == 0:
            writer.writerow(['Link', 'simpleText', 'stemmed_text','Category', 'Graph' ])  # Header row
        writer.writerow([link, cleaned_text, stemmed_text, category, ""])  # Data row

