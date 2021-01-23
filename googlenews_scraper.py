# Request html script related for web scraping
from requests_html import HTMLSession

# creating session variable
session = HTMLSession()

# Defining out url
url = "https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en"

# retrieving info from web page
r = session.get(url)

# render the web in background
r.html.render(sleep=1, scrolldown=0)

# got article from web page, created empty list
articles = r.html.find('article')
headlineList = []

# retieving information from article in dictionary and than appended to list
for item in articles:
    try:
         newsitem = item.find('h3', first=True)
         headlines = { 
         'title':  newsitem.text,
         'link' : newsitem.absolute_links
         }    
         headlineList.append(headlines)
    except:
         pass 

# print(len(headlineList))    

for news in headlineList:
    for key in news:
        print(key, '->', news[key])