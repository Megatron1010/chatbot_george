from flask import Flask, request
import requests


app = Flask(__name__)

PAGE_ACCESS_TOKEN = "EAAMkZBZCiLpCABABXGgrsATop8I3X8gGc08R0XTOEsAB8CNkFkZBhDAdLAT7oGYGuZAKOc61EVKJB2JW88v3mfNFHhHnZBEjJVuvog7GhLcr5JZCUPqV3QOCPZBVtPO9iY0X02ns43r5rQ60IXIxiUyydZCWmRIa5damKwpBLzObRfJeegdLOjbo"
FB_API_URL = "https://graph.facebook.com/v11.0/me/messages?access_token=<PAGE_ACCESS_TOKEN>"
VERITY_TOKEN = "20506974"


def get_bot_response(message):
    """This is just a dummy function, returning a variation of what
    the user said. Replace this function with one connected to chatbot."""
    return "This is a dummy response to '{}'".format(message)


def verify_webhook(req):
    if req.args.get("hub.verify_token") == VERIFY_TOKEN:
        return req.args.get("hub.challenge")
    else:
        return "incorrect"

def respond(sender, message):
    """Formulate a response to the user and
    pass it on to a function that sends it."""
    response = get_bot_response(message)
    send_message(sender, response)


def is_user_message(message):
    """Check if the message is a message from the user"""
    return (message.get('message') and
            message['message'].get('text') and
            not message['message'].get("is_echo"))


@app.route("/webhook", methods=['GET','POST'])
def listen():
    """This is the main function flask uses to
    listen at the `/webhook` endpoint"""
    if request.method == 'GET':
        return verify_webhook(request)

    if request.method == 'POST':
        payload = request.json
        event = payload['entry'][0]['messaging']
        for x in event:
            if is_user_message(x):
                text = x['message']['text']
                sender_id = x['sender']['id']
                respond(sender_id, text)

        return "connection successfully established"
