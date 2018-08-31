import requests
import webbrowser
import bs4

searchKey = "https://www.flipkart.com/search?q=mobile"
#key = input()
#webbrowser.open(searchKey + key)
res = requests.get(searchKey)

try:
	res.raise_for_status()
except Exception as exc:
	print("There was a problem: %s" % (exc))

soup = bs4.BeautifulSoup(res.text, "html.parser")
