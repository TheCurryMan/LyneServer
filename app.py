from flask import Flask
from flask import request
import requests
import json
from firebase import firebase

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():

    userID = request.args.get('userID')
    lyneID = request.args.get('lyneID')
    fb = firebase.FirebaseApplication('https://lyne.firebaseio.com/', None)
    data = fb.get('/lynes/'+lyneID, None)

    title = data["name"]
    header = {"Content-Type": "application/json; charset=utf-8",
              "Authorization": "Basic NmIxNmQwNjQtNjUxMi00MTg4LWFlOGMtZjE5YTFlMDdkYWY1"}

    payload = {"app_id": "87a88c34-ce46-41bb-bcbe-867248438aaa",
               "include_player_ids": [userID],
               "contents": {"en": "It's now your turn. You are 1st in Lyne!"},
               "headings": {"en": title},
               "ios_badgeType": "Increase",
               "ios_badgeCount": "1",
               }

    req = requests.post("https://onesignal.com/api/v1/notifications", headers=header, data=json.dumps(payload))

    print(req.status_code, req.reason)

    return title + " " + userID


if __name__ == '__main__':
    app.run()
