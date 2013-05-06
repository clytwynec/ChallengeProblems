from collections import defaultdict
import sys
import string

with open(sys.argv[1]) as f:
	text = f.read().lower()

for item in string.punctuation: 
	text = text.replace(item, '')

words = text.split()
word_count = defaultdict(lambda:0)

for word in words:
	if 'e' not in word:
		word_count[word] += 1

ordered_by_count = sorted(word_count.iteritems(), key= lambda (x): x[1], reverse = True)
print ordered_by_count[0:10]