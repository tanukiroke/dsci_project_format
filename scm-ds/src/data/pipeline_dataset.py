def seq_list(tweet):
	return [str(tweet)]

def lowercase(tweet):
	tweet = tweet.lower()
	return tweet

def tokenizer(tweet):
	tweet_tokens = tweet[0].split(" ")
	return tweet_tokens

def stpwords(tweet):
	stop_words = stopwords.word('english')
	tweet = list(tweet)
	tweet_nsw = [word for word in tweet if word not in stop_words]
	return tweet_nsw

def url_remover(tweet):
	tweets = [word for word in tweet if not word.__contains__("http")]
	return tweets

def bad_symbols(tweet):
	import re
	BAD_SYMBOLS_RE = re.compile('[^0-9a-z #+_]')
	clean_tweet = re.sub(BAD_SYMBOLS_RE, "", tweet)
	return clean_tweet

def corpus(df):
	size = len(df)
	corpus = []
	for index in range(0, size):
		corpus.extend(df[index])

	return corpus

def word_ocurrences(corpora):

	from collections import defaultdict
	from future.utils import iteritems

	word_ocurr = defaultdict(int)
	for word in corpora:
		word_ocurr[word]+=1

	max_count = max(iteritems(word_ocurr), key = lambda x: x[1])

	return max_count, dict(word_ocurr)

def rank_ocurr(word_count):
	ranked_words = {k:v for k, v in sorted(word_count.items(), key = lambda x: word_count[x[0]], reverse = True)}