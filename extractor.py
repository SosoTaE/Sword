import re

def extract_georgian_words_from_text(text):
  """
  Extracts all Georgian words from a text file.

  Args:
      filename: The name of the file to process.

  Returns:
      A list of Georgian words found in the file.
  """

  georgian_pattern = re.compile(r"[\u10A0-\u10FF]+")  # Georgian Unicode range

  words = georgian_pattern.findall(text)
  return words

def send_to_database(georgian_words):

  from pymongo import MongoClient

  CONNECTION_STRING = "mongodb+srv://doadmin:85071aJ6OYj9esZ3@db-mongodb-fra1-88675-10363f72.mongo.ondigitalocean.com/Sword?authSource=admin&replicaSet=db-mongodb-fra1-88675&tls=true"
  client = MongoClient(CONNECTION_STRING)

  database = client.Sword
  collection = database.words

  collection.insert_many([{"word": word, "addCount": 1,} for word in georgian_words])

import requests
from bs4 import BeautifulSoup

def extract_links_from_a_tags(url):
  """
  Extracts all links found within 'a' tags from a given URL.

  Args:
      url: The URL of the webpage to scrape.

  Returns:
      A list of extracted links (href attributes) from 'a' tags.
  """

  try:
      response = requests.get(url)
      response.raise_for_status()  # Raise an exception for bad status codes

      soup = BeautifulSoup(response.content, 'html.parser')
      a_tags = soup.find_all('a')

      links = [a['href'] for a in a_tags if 'href' in a.attrs]
      return links

  except requests.exceptions.RequestException as e:
      print(f"Error fetching the webpage: {e}")
      return []

def extract_links(text):
  """
  Extracts URLs from a given text using regular expressions.

  Args:
      text: The text string to search for URLs.

  Returns:
      A list of extracted URLs.
  """

  url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
  urls = url_pattern.findall(text)
  return urls

url = ""
links = extract_links_from_a_tags(url)


parsed_urls = set()

links.append(url)

for each in links:
  for url in set(extract_links(each)):
    try:
        if url in parsed_urls:
            continue
        response = requests.get(url)

      if response.status_code != 200:
        continue

      text = response.text

      georgian_words = set(extract_georgian_words_from_text(text))
      print(len(georgian_words), georgian_words)
      send_to_database(georgian_words)
      parsed_urls.add(url)
    except Exception as e:
      print("error")