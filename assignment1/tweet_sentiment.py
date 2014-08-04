import sys
import json
from pprint import pprint

def hw(sentiment_dict, statuses):
    for text in statuses:
        score = 0
        for word in text.split(" "):
            try:
                score += sentiment_dict[word]
            except:
                pass
        print score

def lines(fp):
    print str(len(fp.readlines()))

def get_sentiment_from_afinn():
    afinnfile = open("AFINN-111.txt")
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    return scores # Print every (term, score) pair in the dictionary

def get_text_from_tweet_file(tweet_file):
    data = json.loads(tweet_file.read())
    return [status["text"] for status in data["statuses"]]

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    sentiment_dict = get_sentiment_from_afinn()
    text = get_text_from_tweet_file(tweet_file)

    hw(sentiment_dict, text)
    lines(sent_file)
    lines(tweet_file)

if __name__ == '__main__':
    main()
