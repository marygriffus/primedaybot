import twitter
import schedule
import time
import datetime
from local_settings import *

def connect():
    api = twitter.Api(consumer_key=MY_CONSUMER_KEY,
                          consumer_secret=MY_CONSUMER_SECRET,
                          access_token_key=MY_ACCESS_TOKEN_KEY,
                          access_token_secret=MY_ACCESS_TOKEN_SECRET)
    return api

if __name__=="__main__":

    def is_prime(num):
        if num == 1:
            return False
        elif num == 2 or num == 3:
            return True
        else:
            for _ in range(2, num - 1):
                if num % _ == 0:
                    return False
            return True

    def prime_tweet():
        greatness_scale = ["pretty bad", "not too bad", "rockingly", "AMAZING"]
        to_tweet = ''

        now = datetime.datetime.now
        day = is_prime(int(now.day))
        mo = is_prime(int(now.month))
        year = is_prime(int(now.year))
        awesomeness = 0

        if day:
            awesomeness += 1
            to_tweet += "Nice Day! "
        if mo:
            awesomeness += 1
            to_tweet += "Nice month! "
        if year:
            awesomeness += 1
            to_tweet += "Nice year! "

        to_tweet += "Things are going " + greatness_scale[awesomeness] + "!"

        api = connect()
        status = api.PostUpdate(to_tweet)

    schedule.every().day.at("7:00").do(prime_tweet)
