from bs4 import BeautifulSoup
from urllib import request
import urllib.parse
import urllib.error
from urllib.request import urlopen

def make_soup(url):
    html = urlopen(url).read()
    return BeautifulSoup(html)

def get_images(url):
    soup = make_soup(url)
    #this makes a list of bs4 element tags

    image = soup.find(id="logo", src=True)
    if image is None:
        print('No images found.')
        return

    image_link = image['src']
    filename = image_link.split('/')[-1]
    request.urlretrieve(filename)
    return image_link
try:    
    get_images('https://pypi.python.org/pypi/ClientForm/0.2.10');
except ValueError as e: 
    print("File could not be retrieved.", e)
else:
    print("It worked!")

#a standard call looks like this
#get_images('http://www.wookmark.com')