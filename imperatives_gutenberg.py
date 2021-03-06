#!/usr/bin/env python
# encoding=utf-8

import random
import nltk
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import gutenberg

lemmatizer = WordNetLemmatizer()

wrong_obs = ['mrs', 'ms', 'miss', 'his']
wrong_vbs = ['sing', 'concerning', 'king', 'bring']

def find_phrases(regexp):
	fids = gutenberg.fileids()
	rs = []
	for fid in fids:
		txt = nltk.Text(gutenberg.words(fid))
		ts = nltk.text.TokenSearcher(txt)
		r = ts.findall(regexp)
		for x in r:
			if x[0].lower() in wrong_vbs:
				x[0] = 'looking at'
			if x[-1].lower() in wrong_vbs:
				x[-1] = 'me'
		rs.extend(r)

	return rs

def main():
	regexp = '<.*ing><the><.*s>'
	rs = find_phrases(regexp)
	for r in rs:
		if random.choice([0, 1]):
			chc = random.choice(['start', 'stop'])
		elif random.choice([0, 1]):
			chc = random.choice(['occasionally', 'constantly'])
			r[0] = lemmatizer.lemmatize(r[0].lower(), 'v')
		else:
			chc = random.choice(['always', 'never'])
			r[0] = lemmatizer.lemmatize(r[0].lower(), 'v')
		if random.choice([0, 1]):
			r[1] = random.choice(['all those', 'so many', 'more than five', ''])
		r = ' '.join(r).lower().replace('  ', ' ')
		print '{0} {1}.'.format(chc, r).capitalize()

if __name__ == '__main__':
	main()
