from os.path import basename
from urlparse import urlsplit
from bs4 import BeautifulSoup
import os
import errno 
import sys
import urllib2

def scrape(html_file):
    with open(html_file) as f:
        html = f.read()
        soup = BeautifulSoup(html)
        html_dir = os.path.split(html_file)[0]
        for img in soup.find_all('img'):
            src = img.get('src')
            if 'http' in src: #get all remote images
                elems = src.split('/') 
                filename = elems[-1] #image file name
                new_path = os.path.join(os.path.join(html_dir, 'scraped/'), filename)
                new_dir = os.path.split(new_path)[0]
                make_sure_path_exists(new_dir)
                download(src, new_path) #save it
                print "downloaded %s" % filename
                newfilename = os.path.relpath(new_path, html_dir) 
                img['src'] = newfilename #change the src in img tag

    with open(html_file, 'w+') as f:
        f.write(soup.prettify().encode('ascii', 'xmlcharrefreplace')) #save html

def url2name(url):
    return basename(urlsplit(url)[2])

def download(url, localFileName):
    localName = url2name(url)
    req = urllib2.Request(url)
    r = urllib2.urlopen(req)
    with open(localFileName, 'w+') as f:
        f.write(r.read())

def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

if __name__ == "__main__":
    try:
        main_dir = sys.argv[1]
    except:
        print "usage: fb-archive-scraper.py <path to fb archive>"
    
    #first do the photo albums
    photos = os.path.join(main_dir, 'photos')
    if os.path.exists(photos):
        for filename in os.listdir(photos):
            full_fname = os.path.join(photos, filename)
            if os.path.isdir(full_fname):
                print "scraping photo album with id: ", filename
                albumdir = os.path.join(photos, full_fname)
                albumindex = os.path.join(albumdir, 'index.htm')
                if os.path.isfile(albumindex):
                    scrape(albumindex)
    #make sure we didn't miss any images on the other pages of the archive
    html_dir = os.path.join(main_dir, 'html')
    if os.path.exists(html_dir):
        for filename in os.listdir(html_dir):
            full_fname = os.path.join(html_dir, filename)
            if os.path.isfile(full_fname) and '.htm' in filename:
                print "scraping for ", filename
                scrape(full_fname)
