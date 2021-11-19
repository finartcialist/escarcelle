# https://finartcialist.com/escarcelle/beta/en/atom_en.xml
# https://finartcialist.com/escarcelle/beta/fr/atom_fr.xml

from datetime import datetime as dt
from dateutil.tz import gettz
import os
from feedgen.feed import FeedGenerator
from bs4 import BeautifulSoup

fg = FeedGenerator()
fg.load_extension('base')

fg.id('https://www.finartcialist.com/escarcelle/fr/blog/index.html')
fg.title('escarcelle - le marché aux sentiments')
fg.author( {'name':'finartcialist', 'email':'escarcelle@finartcialist.com'})
fg.link(href="https://www.finartcialist.com/escarcelle/fr", rel='alternate')
fg.subtitle("Nouvelles")
fg.link(href="https://www.finartcialist.com/escarcelle/fr", rel="self")
fg.language("fr")

for root, subFolders, files in os.walk("./fr/blog/posts/"):
    path = os.path.basename(root)
    print(path)
    for f in files:
        if f != "atom_fr.xml" and f != "0.html":
            if len(path) > 0:
                path_to_html = 'fr/blog/posts/' + path + '/' + f
            else:
                path_to_html = 'fr/blog/posts/' + f
            print(path_to_html)
            with open('./' + path_to_html) as html_text:
                soup = BeautifulSoup(html_text, 'html.parser')
                title = soup.title.string

            fe = fg.add_entry()
            fe.id("https://www.finartcialist.com/" + path_to_html)
            fe.title(title)
            if len(path) > 0:
                fe.link(href="https://www.finartcialist.com/fr/blog/posts/" + path + '/' + f)
            else:
                fe.link(href="https://www.finartcialist.com/fr/blog/posts/" + f)
            fe.updated(dt.fromtimestamp(os.path.getmtime("./fr/blog/posts/" + path + '/'+ f),tz=gettz("America/New York")))

fg.atom_file('atom_fr.xml')

fg_en = FeedGenerator()
fg_en.load_extension('base')


fg_en.id('https://www.finartcialist.com/escarcelle/en/blog/index.html')
fg_en.title('escarcelle - the feelings market')
fg_en.author( {'name':'finartcialist', 'email':'escarcelle@finartcialist.com'})
fg_en.link(href="https://www.finartcialist.com/escarcelle/en", rel='alternate')
fg_en.subtitle("News")
fg_en.link(href="https://www.finartcialist.com/escarcelle/en", rel="self")
fg_en.language("en")



for root, subFolders, files in os.walk("./en/blog/posts/"):
    path = os.path.basename(root)

    for f in files:
        if f != "atom_en.xml" and f != "0.html":
            if len(path) > 0:
                path_to_html = 'en/blog/posts/' + path + '/' + f
            else:
                path_to_html = 'en/blog/posts/' + f
            print(path_to_html)
            with open('./' + path_to_html) as html_text:
                soup = BeautifulSoup(html_text, 'html.parser')
                title = soup.title.string  
                print(title)  
    
            fen = fg_en.add_entry()
            fen.id("https://www.finartcialist.com/" + path_to_html)
            fen.title(title)
            print(fen.title())
            if len(path) > 0:
                fen.link(href="https://www.finartcialist.com/en/blog/posts/" + path + '/' + f)
            else:
                fen.link(href="https://www.finartcialist.com/en/blog/posts/" + f)
            fen.updated(dt.fromtimestamp(os.path.getmtime("./en/blog/posts/" + path + '/'+ f),tz=gettz("America/New York")))
            
fg_en.atom_file('atom_en.xml')
