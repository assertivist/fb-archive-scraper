fb-archive-scraper
==================

I was really excited when Facebook began offering a service to download all your content in an archive. I downloaded my archive and attempted to browse it without an internet connection only to find...

The Photos Weren't There
========================
... a bunch of broken images! Upon further inspection, all the image elements in my photo album archive page pointed to images out on Facebook's servers.

I wrote a simple script to "fix" this problem. What it does is go through your archive and scrapes all the remote content that Facebook put in your archive to be local content, and then updates the html files to point to the local content instead. There you go, a REAL archive of your Facebook photos and statuses, not dependent on any internet connection when browsing locally.

How to use
==========


You will require a python 2.7 installation and the [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/) python module.
The script is stupid simple.

Then: `python fb-archive-scraper.py <path to archive>`

Always use a copy of your archive to run the script on, I'm not responsible for any damages caused by using this script.
