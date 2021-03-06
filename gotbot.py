import praw
import re
import tweepy
import secrets

def cleantitle(title):
	return re.findall("^\[.*\](.*)", title)[0]

def parsepost(post):

	if not post.is_self: 
		if "reddituploads" in post.url:
			status = ""
		else:
			status = cleantitle(post.title) + ": 	" + post.url
	else:
		status = cleantitle(post.title)
	return status


def main():	
	
	secrets.init()

	reddit = praw.Reddit(user_agent="twitter.com:tweets_iaf v 0.0.2 by /u/umeshunni")
	
	hotposts = reddit.get_subreddit('gameofthrones').get_top(limit=10)

	auth = tweepy.OAuthHandler(secrets.consumer_key, secrets.consumer_secret)
	auth.set_access_token(secrets.access_token, secrets.access_token_secret)

	twitter = tweepy.API(auth)

	for post in hotposts:
		status = parsepost(post)
		if post.is_self or not status:
			print ("Skipped: " + status) 
		else:
			print ("Tweeting: " + status )
			#twitter.update_status(status)
	


if __name__ == "__main__":
    main()
