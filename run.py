from markov_python.cc_markov import MarkovChain
from fetch_data import fetch_data

lyrics = fetch_data()

mc = MarkovChain()
for song in lyrics:
	mc.add_string(song)

print mc


"""text = mc.generate_text(400)

for i in range(0,400,5):
	for j in text[i:i+5]:
		print j,
	print ""
	if i % 4 == 0:
		print "\n"""