from bs4 import BeautifulSoup
from urllib import request
import urllib.parse
import urllib.error
from urllib.request import urlopen
from urllib.error import HTTPError as e

def make_soup(url):
        html = urlopen(url).read()
        return BeautifulSoup(html, "html.parser")

def get_images(url):
    soup = make_soup(url)
    # this makes a list of bs4 element tags
    images = [img for img in soup.findAll('img')]
    print((str(len(images)) + "images found."))
    print('Downloading images to current working directory.')
    # compile our unicode list of image links
    image_links = [each.get('src') for each in images]
    for each in image_links:
        filename=each.split('/')[-1]
        try:
            urllib.request.urlretrieve(each, filename)
        except Warning:
            pass
    return image_links


def get_images(url):
    soup = make_soup(url)
    # this makes a list of bs4 element tags
    images = [img for img in soup.findAll('img')]
    print((str(len(images)) + "images found."))
    print('Downloading images to current working directory.')
    # compile our unicode list of image links
    imagethumblinks_links = [each.get('src') for each in images]
    i = 0
    #0: File url, 1:filename
    giftupplelist = []
    jpegtupplelist = []
    for each in imagethumblinks_links[10:13]:
        filename=each.split('/')[-1]
        fileUrl = "http://img.rule34.xxx//samples/" + each.split('/')[-2] + '/sample_' + (each.split('_')[-1])
        try:
          urllib.request.urlretrieve(fileUrl, filename)
        except urllib.error.HTTPError as e:
          if e.reason == 'Not Found':
            print("duck")
          fileUrl = fileUrl.replace('samples','images')[:-5]+".gif"
          filename = filename[:-4]+".gif"
          fileUrl = fileUrl.replace('sample_','')
          giftupplelist.append((fileUrl, filename))
          print(filename)
        except e:
          fileUrl = fileUrl.replace('samples','images')[:-3]+".jpeg"
          fileUrl = fileUrl.replace('sample_','')
          print(fileUrl)
          urllib.request.urlretrieve(fileUrl, filename)
        except:
          print(fileUrl)
    giftupplelist.pop(0)
    print(giftupplelist)
    for each in giftupplelist:
      try:
        urllib.request.urlretrieve(each[0], each[1])
      except:
        print(each[1], each[0])
        print("File failed to download, File skiped")

        
get_images(webs)