import urllib2
import re
from bs4 import BeautifulSoup

def fetch_data():

	songs = [
"http://www.songtextemania.com/vato_mulatto_songtext_luciano.html",
"http://www.songtextemania.com/flex_songtext_luciano.html",
"http://www.songtextemania.com/psychose_songtext_luciano.html",
"http://www.songtextemania.com/jager_songtext_luciano.html"
]

	result = []

	for arg in songs:
		response = urllib2.urlopen(arg)
		html = response.read()
		soup = BeautifulSoup(html, 'html.parser')
		text = ""
		for line in soup.find_all('div', class_ = "p402_premium"):
			for br in line.br.children:
				#print re.sub('<.*?>', '', unicode(br)), "ENDE!"
				text += re.sub('<.*?>', '', unicode(br))
			#print re.sub('<.*?>', '', line)
			result.append(text)
	return result

