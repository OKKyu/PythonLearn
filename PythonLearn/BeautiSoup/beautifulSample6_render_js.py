#!python3
# -*- coding:utf- -*-
'''
  beautifulSample6_render_js.py
    How to scrape web page that is rendered by javascript.
    There is necessary HTMLSession module in requests_html library.
    References Information is below url.
      https://stackoverflow.com/questions/26393231/using-python-requests-with-javascript-pages
'''
from requests_html import HTMLSession
from bs4 import BeautifulSoup

# Get target page with HTMLSession.
# You can get target page by below command, but It is not rendered yet.
session = HTMLSession()
s = session.get("http://galaxyheavyblow.web.fc2.com/fc2-imageviewer/?aid=1&iid=143")

# Render web page that you got it.
# If rendering time was over timeout, timeout error has occurred and rendering is disposed.
# Default timeout is 8 seconds.
# Type of error : pyppeteer.errors.TimeoutError.
s.html.render(timeout=200)

# Parse with BeautifulSoup.
soup = BeautifulSoup(s.html.html, "html.parser")
print("number of images is " + str(len(soup.find_all("img"))))

# This is end. Enjoy your Scraping!
