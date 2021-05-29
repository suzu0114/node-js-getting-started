
# ツイートを取得

import tweepy
import config #各種token
import datetime

CK = config.environ["onsumer_key"]
CS = config.environ["onsumer_secret"]
ATS = config.environ["token"]
AT = config.environ["token_secret"]

auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, ATS)
api = tweepy.API(auth)

DT = datetime.datetime.now()
newDT = DT.strftime('%H時%M分')
tweet = "ただいまの時刻は"+newDT+"です。\n"

if DT.hour > 6 and DT.hour <= 12:
   tweet+="おはようございます！\n今日達成した目標を立てて行動を心がけます！"
elif DT.hour >= 12 and DT.hour < 18:
   tweet+="こんにちは\残り半日、頑張っていきましょう！"
elif DT.hour > 18 and DT.hour < 24:
   tweet+="こんばんは。\n一日も残りわずかです\n頑張りましょう"

api.update_status(status = tweet)