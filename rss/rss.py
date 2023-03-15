import feedparser

# URL du flux RSS de Hacker News
url = "https://www.developpez.com/index/rss"

# Récupération des articles à partir du flux RSS
feed = feedparser.parse(url)

# Parcours des articles et affichage des titres et des liens
for entry in feed.entries:
    print("Titre : ", entry.title)
    print("Lien : ", entry.link)
    print()
