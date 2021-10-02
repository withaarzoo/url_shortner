import pyshorteners

link = input("Enter the link : ")
shortener = pyshorteners.Shortener()
X = shortener.tinyurl.short(link)
print(X)
