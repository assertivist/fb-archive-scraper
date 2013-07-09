from os.path import basename
from urlparse import urlsplit
from bs4 import BeautifulSoup
import urllib2
import os

def scrape(profile_index_local_file, currdir):
    with open(profile_index_local_file) as f:
        html = f.read()
        soup = BeautifulSoup(html)
        #print(soup.prettify())
        for img in soup.find_all('img'):
            src = img.get('src')
            if '..' not in src:
                print src
                elems = src.split('/')
                filename = elems[-1]
                download(src, filename)
                print filename
                newfilename = "%s/stolen/%s" % (currdir,filename)
                print newfilename
                img['src'] = newfilename
        print soup.prettify()

def url2name(url):
    return basename(urlsplit(url)[2])

def download(url, localFileName = None):
    localName = url2name(url)
    req = urllib2.Request(url)
    r = urllib2.urlopen(req)
    if r.info().has_key('Content-Disposition'):
        # If the response has Content-Disposition, we take file name from it
        localName = r.info()['Content-Disposition'].split('filename=')[1]
        if localName[0] == '"' or localName[0] == "'":
            localName = localName[1:-1]
    elif r.url != url: 
        # if we were redirected, the real file name we take from the final URL
        localName = url2name(r.url)
    if localFileName: 
        # we can force to save the file as specified name
        localName = localFileName
    fullpath = os.path.abspath("facebook-assertivist/stolen/%s" % localName)
    f = open(fullpath, 'w+')
    f.write(r.read())
    f.close()


if __name__ == "__main__":
    print("running")
    scrape('facebook-assertivist/html/photos.htm')
