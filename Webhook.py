#!/usr/bin/python3
# Released under GPLv3+ Licence
# Arash Baheri<arashbaheri@icloud.com>, 2022
from flask import Flask, request, jsonify
import requests
from kavenegar import *

app = Flask(__name__)

@app.route('/', methods = ['POST'])

def main():
    payload = request.get_json(force = True)
    response = payload['alerts'][0]['annotations']['summary']
    status = payload['status']
    severity = payload['alerts'][0]['labels']['severity']
    massage = f"{severity}-{status} : \n{response}"
    decide_to_send(severity, massage)
    return jsonify(payload)


def decide_to_send(severity, massage):
    if severity == 'warning':
        return telegram(massage)
    elif severity == 'critical':
        telegram(massage)
        return sms(massage)


def telegram(massage):
    token = 'YOUR TELEGRAM BOT API TOKEN'
    chat_id = 'YOUR TELEGRAM CHAT ID'
    url = 'https://api.telegram.org'
    return requests.get(f'{url}/bot{token}/sendmessage?chat_id={chat_id}&text={massage}')


def sms(massage):
    api_key = 'YOUR KAVENEGAR API KEY'
    sender = 'YOUR KAVENEGAR SENDER'
    receptor = 'YOUR NUMBER'
    try:
        api = KavenegarAPI(api_key)
        params = {
            'sender': sender,
            'receptor': receptor,
            'message': massage,
        }
        return api.sms_send(params)

    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)


if __name__ == "__main__":
    app.run(host='localhost', port=4560)
