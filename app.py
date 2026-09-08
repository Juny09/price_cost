from flask import Flask, request, jsonify, send_file, render_template
from decoder import decode_code

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():

    data = request.json

    code = data["code"]
    cost = data["cost"]
    margin = data["margin"]

    decoded = decode_code(code)

    selling_price = cost / (1 - margin)

    return jsonify({
        "code": code,
        "decoded": decoded,
        "cost": cost,
        "margin": margin,
        "selling_price": round(selling_price, 2)
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)