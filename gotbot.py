import praw
import re
import tweepy


consumer_key = "af3v5r8FhE2rGXNEt1Q3vEGGi"
consumer_secret = "BQWE3Hh30VX1LptNn9k6z0YbCu0bYCTx6xpvn6rxcuQQdDd1xk"
access_token = "2492242001-AhQ3EoEvgzRukljOZtfKZDckyhrL7nkXhxxWEti"
access_token_secret = "UVYp4x4FIxJMNRp8RlBCvjldKwmBz48mSaI40vQT5IFwq"

def cleantitle(title):
	return re.findall("^\[.*\](.*)", title)[0]

def parsepost(post):
	if not post.is_self: 
		status = cleantitle(post.title) + ":" + post.url
	else:
		status = cleantitle(post.title)
	return status


def main():	
	reddit = praw.Reddit(user_agent="twitter.com:tweets_iaf v 0.0.1 by /u/umeshunni")
	
	hotposts = reddit.get_subreddit('gameofthrones').get_top(limit=10)

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	twitter = tweepy.API(auth)

	for post in hotposts:
		status = parsepost(post)
		if post.is_self:
			print "Skipping: " + status 
		else:
			print "Tweeting: " + status 
			twitter.update_status(status)
	


if __name__ == "__main__":
    main()