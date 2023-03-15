import feedparser

# URL du flux RSS de Hacker News
url = "https://www.developpez.com/index/rss"

# Récupération des articles à partir du flux RSS
feed = feedparser.parse(url)

# Ouverture du fichier rss.txt en mode écriture
with open("rss.txt", "w") as f:
    # Parcours des articles et écriture des titres et des liens dans le fichier
    for entry in feed.entries:
        f.write("Titre : " + entry.title + "\n")
        f.write("Lien : " + entry.link + "\n\n")
