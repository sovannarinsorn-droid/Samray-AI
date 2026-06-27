from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

TELEGRAM_BOT = os.getenv("TELEGRAM_BOT", "https://t.me/smos_sne1")

@app.route("/")
def index():
    return render_template("index.html", telegram_bot=TELEGRAM_BOT)

@app.route("/submit", methods=["POST"])
def submit():
    data = request.get_json()
    url = (data or {}).get("url", "").strip()
    if not url:
        return jsonify({"ok": False, "msg": "សូមបញ្ចូល link"}), 400
    # Redirect user to Telegram bot with the URL pre-filled
    tg_link = f"https://t.me/smos_sne1?start={url}"
    return jsonify({"ok": True, "redirect": tg_link})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
