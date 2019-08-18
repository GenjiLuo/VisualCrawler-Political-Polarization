################## Twitter Streaming API ###################

## packages
import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import re
import pandas

## initializing auth keys
consumer_key = 'WAfMFUeX727ZJyHbxRG5TqbHx'
consumer_secret_key = 'QempGWO01nvNXJROIBHdIPAcGsC78qCzM4XI7ZYbZEsTlL0jb2'
access_token = '1132328609270697985-o0RjHLFH5oEeNw5It2gOiJgPOPBpMD'
access_token_key = 'CmFuCC6UAZpV8GgSs5Y3pH3dGWX5x1zL6cNry2ESQT7Pr'

##overriding class definitions
class listener(StreamListener):

    def on_data(self, data):
        print(data)
        #return True
    
    def on_status(self, status):
        print(status.text)

    def on_error(self, status):
        if status == 420:
            return False
        print(status)

## authentication
auth = OAuthHandler(consumer_key, consumer_secret_key)
auth.set_access_token(access_token, access_token_key)

## api instance creation
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

# The below list comprises of Twitter User ID corresponding to each newspaper user screen name Eg., 759251 is the twitter user id of screen name 759251. More can be added to the list by simply looking up at http://gettwitterid.com/?user_name=CNN&submit=GET+USER+ID
follow_list = [ '4898501','12699932','14216661','12848262','612473',
				'11178352','807095','16973333','255877649','17446621',
				'14085040','14511951','87818409','2467791','3108351',
				'819800','20818801','34713362','2855891277','16477702',
				'6577642','17448662','14293310','1652541','9235982',
				'67358777','759251','9300262','35773039','15210284',
				'18851248','4170491','91478624','14352556','16041234',
				'8861182','97739866','64643056','29097819','16664681',
				'14857525','20094138','15754281','20402945',
				'15438913','16887175','7309052','28785486','16666806',
				'7313362','51241574','14173315','12811952','8795772',
				'13115682','14304462','1429761','1917731','19417492',
				'20139563','16543775','17895820','17546958','1367531',
				'762231576','16544024','20545835','21344507','16467567','27703934',
				'92120051','34109146','15926431','15572679','16117304',
				'8940342','17348525','457984599','15615783','6039302'
				'13323862','8216772','20269833','15369276','15679641'
				'14955722','15050354','14410896','1018921','14528874']

#track_list=['trump','donald trump','president','donald','US Congress','angela merkel','government']

############## Twitter Streaming ############
## starting the twitter stream
twitterStream = Stream(auth, listener(), wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)
#twitterStream.filter(follow = follow_list, track = track_list, languages = ['en'])   # track and follow do not work as AND!!!

##  Filtering the stream to include results from newspaper handles alone
twitterStream.filter(follow = follow_list, languages = ['en'])   