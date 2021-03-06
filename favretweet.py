#!/usr/bin/env python3
# ecnitoctoc/favretweet.py

import tweepy
import logging
from config import create_api
logging.basicConfig(filename='/home/twitter/ecnitoctoc/log.bot', level=logging.INFO, format='%(asctime)s %(levelname)-8s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
#logging.basicConfig(
#        format='%(asctime)s %(levelname)-8s %(message)s',
#        level=logging.INFO,
#        datefmt='%Y-%m-%d %H:%M:%S')import json

#logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

class FavRetweetListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        logger.info("Processing tweet ")
        if tweet.in_reply_to_status_id is not None or \
            tweet.user.id == self.me.id or tweet.user.following == True:   #troisième option à corriger et déplacer
            logger.info("Not you")
            # This tweet is a reply or I'm its author so, ignore it
            return

#        if tweet.user.following == False:
#            logger.error("Not following", exc_info=True)
#            return

        if not tweet.favorited:
            # fav si pas déjà fav
            try:
                tweet.favorite()
            except Exception as e:
                logger.error("Error on fav", exc_info=True)
        if not tweet.retweeted:
            # rt si pas déjà fait
            try:
                tweet.retweet()
            except Exception as e:
                logger.error("Error on retweet", exc_info=True)

    def on_error(self, status):
        logger.error(status)

def main(keywords):
    api = create_api()
    tweets_listener = FavRetweetListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=keywords)

if __name__ == "__main__":
    main(["#ecnitoctoc"])
