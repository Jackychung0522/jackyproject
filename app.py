import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from fsm import TocMachine
from utils import send_text_message

load_dotenv()


machine = TocMachine(
    states=["user", "state1", "state2","restart","age","beginner","medium","highlevel","bserve","mserve","hserve","bfinish","mfinish","hfinish","bserved","hserved","mserved","bservedtop","bservedunder","bservedside","hservedtop","hservedside","hservedunder","mservedtop","mservedunder","mservedside","bkiller","mkiller","hkiller"],
    transitions=[
        {
            "trigger": "advance",
            "source": "user",
            "dest": "state1",
            "conditions": "is_going_to_state1",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "state2",
            "conditions": "is_going_to_state2",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "age",
            "conditions": "is_going_to_age",
        },

        {
            "trigger": "advance",
            "source": "age",
            "dest": "beginner",
            "conditions": "is_going_to_beginner",
        },
        {
            "trigger": "advance",
            "source": "age",
            "dest": "medium",
            "conditions": "is_going_to_medium",
        },
        {
            "trigger": "advance",
            "source": "age",
            "dest": "highlevel",
            "conditions": "is_going_to_highlevel",
        },
        {
            "trigger": "advance",
            "source": "beginner",
            "dest": "bserve",
            "conditions": "is_going_to_bserve",
        },
        {
            "trigger": "advance",
            "source": "medium",
            "dest": "mserve",
            "conditions": "is_going_to_mserve",
        },
        {
            "trigger": "advance",
            "source": "highlevel",
            "dest": "hserve",
            "conditions": "is_going_to_hserve",
        },
        {
            "trigger": "advance",
            "source": ["bserve","bservedside","bservedtop","bservedunder","bkiller"],
            "dest": "bfinish",
            "conditions": "is_going_to_bfinish",
        },
        {
            "trigger": "advance",
            "source": ["mserve","mservedside","mservedtop","mservedunder","mkiller"],
            "dest": "mfinish",
            "conditions": "is_going_to_mfinish",
        },
        {
            "trigger": "advance",
            "source": ["hserve","hservedside","hservedtop","hservedunder","hkiller"],
            "dest": "hfinish",
            "conditions": "is_going_to_hfinish",
        },

        {
            "trigger": "advance",
            "source": "bfinish",
            "dest": "bserve",
            "conditions": "is_going_to_bserve",
        },
        {
            "trigger": "advance",
            "source": "bfinish",
            "dest": "bserved",
            "conditions": "is_going_to_bserved",
        },
        {
            "trigger": "advance",
            "source": "bfinish",
            "dest": "bkiller",
            "conditions": "is_going_to_bkiller",
        },
        {
            "trigger": "advance",
            "source": "mfinish",
            "dest": "mserved",
            "conditions": "is_going_to_mserved",
        },
        {
            "trigger": "advance",
            "source": "mfinish",
            "dest": "mserve",
            "conditions": "is_going_to_mserve",
        },
        {
            "trigger": "advance",
            "source": "mfinish",
            "dest": "mkiller",
            "conditions": "is_going_to_mkiller",
        },
        {
            "trigger": "advance",
            "source": "hfinish",
            "dest": "hserved",
            "conditions": "is_going_to_hserved",
        },
        {
            "trigger": "advance",
            "source": "hfinish",
            "dest": "hserve",
            "conditions": "is_going_to_hserve",
        },
        {
            "trigger": "advance",
            "source": "hfinish",
            "dest": "hkiller",
            "conditions": "is_going_to_hkiller",
        },
        {
            "trigger": "advance",
            "source": "beginner",
            "dest": "bserved",
            "conditions": "is_going_to_bserved",
        },
        {
            "trigger": "advance",
            "source": "medium",
            "dest": "mserved",
            "conditions": "is_going_to_mserved",
        },
        {
            "trigger": "advance",
            "source": "highlevel",
            "dest": "hserved",
            "conditions": "is_going_to_hserved",
        },
        {
            "trigger": "advance",
            "source": "beginner",
            "dest": "bkiller",
            "conditions": "is_going_to_bkiller",
        },
        {
            "trigger": "advance",
            "source": "medium",
            "dest": "mkiller",
            "conditions": "is_going_to_mkiller",
        },
        {
            "trigger": "advance",
            "source": "highlevel",
            "dest": "hkiller",
            "conditions": "is_going_to_hkiller",
        },
        {
            "trigger": "advance",
            "source": "bserved",
            "dest": "bservedside",
            "conditions": "is_going_to_bservedside",
        },
        {
            "trigger": "advance",
            "source": "bserved",
            "dest": "bservedtop",
            "conditions": "is_going_to_bservedtop",
        },
        {
            "trigger": "advance",
            "source": "bserved",
            "dest": "bservedunder",
            "conditions": "is_going_to_bservedunder",
        },
        {
            "trigger": "advance",
            "source": "mserved",
            "dest": "mservedside",
            "conditions": "is_going_to_mservedside",
        },
        {
            "trigger": "advance",
            "source": "mserved",
            "dest": "mservedtop",
            "conditions": "is_going_to_mservedtop",
        },
        {
            "trigger": "advance",
            "source": "mserved",
            "dest": "mservedunder",
            "conditions": "is_going_to_mservedunder",
        },
        {
            "trigger": "advance",
            "source": "hserved",
            "dest": "hservedside",
            "conditions": "is_going_to_hservedside",
        },
        {
            "trigger": "advance",
            "source": "hserved",
            "dest": "hservedtop",
            "conditions": "is_going_to_hservedtop",
        },
        {
            "trigger": "advance",
            "source": "hserved",
            "dest": "hservedunder",
            "conditions": "is_going_to_hservedunder",
        },



        {
            "trigger": "advance",
            "source": ["bfinish","hfinish","mfinish"],
            "dest": "state1",
            "conditions": "is_going_to_state1",
        },
        {"trigger": "go_back", "source": ["state1", "state2","age","beginner","medium","highlevel","bserve","mserve","hserve"], "dest": "user"},
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)

app = Flask(__name__, static_url_path="")


# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text)
        )

    return "OK"


@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")
        response = machine.advance(event)
        if response == False:
            if machine.state == 'user':
                send_text_message(event.reply_token, '想要進入桌球世界嗎?想要打 "想要" ')
            else:
                send_text_message(event.reply_token, "Not Entering any State")


    return "OK"


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
    machine.get_graph().draw('my_state_diagram.png' ,prog='dot')
