#a program to extract all anchor tags from the web page
#importing liberaries
#import requests to request http
import requests
#import beautifulsoup for parsing HTML content
from bs4 import BeautifulSoup

#mentioning URL to scrape
url = 'https://www.google.com/search?q=git+tutorial&oq=&gs_lcrp=EgZjaHJvbWUqCQgAECMYJxjqAjIJCAAQIxgnGOoCMgkIARAjGCcY6gIyDwgCEC4YJxjHARjqAhjRAzIJCAMQIxgnGOoCMgkIBBAjGCcY6gIyCQgFECMYJxjqAjIJCAYQIxgnGOoCMgkIBxAjGCcY6gLSAQk1NzUxOGowajeoAgiwAgE&sourceid=chrome&ie=UTF-8'

#HTTP GET request to the URL
response = requests.get(url)
#response would be stored in the 'response' varialbe

# check if the request was successful ( HTTP success status code 200)
if response.status_code == 200:
    # parse the HTML content of the page using Beautifulsoup
    #'soup' is an object and is created by passing the HTML content and specific 'html parser' is used
    soup = BeautifulSoup(response.text,'html.parser')


    #find and extract specific data from the webpage
    # e.g. let's say we want to extract all the links on the page
    # we use Beautifulsoup's 'find_all' method to find all the anchor tags, which represent links. 
    links = soup.find_all('a')


    # print the extracted links
    for link in links:
        print(link.get('href'))
    # print their href attribute which contains the URL to which the link points
    
else:
    print('Failed to retrieve the webpage. Status code:', response.status_code)
    