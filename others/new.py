import pyshorteners
url = input("Main URL")
shortener = pyshorteners.Shortener()
url_short = shortener.gitio.short(url)
print(url_short)
