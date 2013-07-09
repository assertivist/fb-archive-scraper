fb-archive-scraper
==================

I was really excited when Facebook began offering a service to download all your content in an archive, they were finally doing a Good Thing!

After downloading and inspecting the archive, I was quite pleased to see that much of the data that is 'behind the scenes' was included beyond the content that I uploaded myself.

Fast forward a couple months, and I'm on my laptop with no internet connection. I wanted to show a (real life, not Facebook) friend of mine a picture that I had uploaded a year or so ago. Of course, this MUST be in my archive! I fire up my web browser and point it to the index of the archive only to find...

==The Photos Weren't There==
... a bunch of broken images! Facebook had, for some reason, chose to include only a small amount of my photos in my content archive. This, to me, was unnacceptable; if you're going to offer a "download all your content" button, you had better make sure it downloads all your content!

The reason that Facebook pulls this nonsense even today escapes me. 

So I wrote a simple script to "fix" this problem. What it does is go through your archive and scrapes all the remote content that facebook put in your archive to be local content, and then updates the html files to point to the local content instead. There you go, a REAL archive of your Facebook photos and statuses, not dependent on any internet connection when browsing locally!

How to use
==========

`python fb-archive-scraper <path to archive>`

This will create a subfolder in each photo album folder called "scraped", and save the remote photos there. It also makes sure there are no remote files on any of the other archive pages, and creates a similar 'scraped' folder in the html section of your archive as well.

Limited Warranty
================

Always use a copy of your archive to run the script on, I'm not responsible for any damages caused by using this script.

This software is available AS IS and AT RISK!
