import os
import requests

from flask import Flask, request, jsonify, render_template
from decoder import decode_code

app = Flask(__name__)

# =========================
# Environment Variables
# =========================

WHATSAPP_ACCESS_TOKEN = os.environ.get("WHATSAPP_ACCESS_TOKEN")
PHONE_NUMBER_ID = os.environ.get("PHONE_NUMBER_ID")
VERIFY_TOKEN = os.environ.get("VERIFY_TOKEN")


# =========================
# Home
# =========================

@app.route("/")
def home():
    return render_template("index.html")


# =========================
# Existing Calculator API
# =========================

@app.route("/calculate", methods=["POST"])
def calculate():

    data = request.json

    code = data["code"]
    cost = float(data["cost"])
    margin = float(data["margin"])

    decoded = decode_code(code)

    selling_price = cost / (1 - margin)

    return jsonify({
        "code": code,
        "decoded": decoded,
        "cost": cost,
        "margin": margin,
        "selling_price": round(selling_price, 2)
    })


# =========================
# WhatsApp Webhook
# =========================

@app.route("/webhook", methods=["GET", "POST"])
def webhook():

    # -------------------------
    # Meta Webhook Verification
    # -------------------------

    if request.method == "GET":

        mode = request.args.get("hub.mode")
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")

        if mode == "subscribe" and token == VERIFY_TOKEN:
            return challenge, 200

        return "Verification failed", 403

    # -------------------------
    # Receive WhatsApp Message
    # -------------------------

    data = request.get_json()

    print("================================")
    print("WhatsApp Webhook Received:")
    print(data)
    print("================================")

    return "OK", 200


# =========================
# Send WhatsApp Message
# =========================

def send_whatsapp_message(to, message):

    url = f"https://graph.facebook.com/v23.0/{PHONE_NUMBER_ID}/messages"

    headers = {
        "Authorization": f"Bearer {WHATSAPP_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {
            "body": message
        }
    }

    response = requests.post(
        url,
        headers=headers,
        json=payload
    )

    print("WhatsApp API Response:")
    print(response.status_code)
    print(response.text)

    return response


# =========================
# Run
# =========================

if __name__ == "__main__":

    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port
    )