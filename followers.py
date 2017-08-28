import logging
import tweepy
    
access_key = "your access key"
access_secret = "your access secret"
consumer_key = "your consumer key"
consumer_secret = "your consumer secret"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

def get_followingss(user_name):
    for user in tweepy.Cursor(api.friends, screen_name=user_name).items():
        print user.screen_name
        
def get_followerss(user_name):
    for user in tweepy.Cursor(api.followers, screen_name=user_name).items():
        print user.screen_name
        
        
def get_mentionss(user_name):       
    mentions = api.mentions_timeline(count=1)
    for mention in mentions:
        print mention.text
        print mention.user_name.screen_name
    
if __name__ == '__main__':
    uname = raw_input('Enter your user-name: ')
    #get_followingss(uname)
    #get_followerss(uname)
    get_mentionss(uname)