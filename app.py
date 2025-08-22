from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

# 默认奖品
prizes = ["苹果", "香蕉", "红包", "手表", "电话", "谢谢参与"]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/spin")
def spin():
    if not prizes:  # 防止 prizes 为空
        return jsonify({"index": -1, "prize": "暂无奖品，请先配置"})
    index = random.randint(0, len(prizes) - 1)
    prize = prizes[index]
    return jsonify({"index": index, "prize": prize})

@app.route("/set_prizes", methods=["POST"])
def set_prizes():
    global prizes
    data = request.json
    new_prizes = data.get("prizes", [])
    if isinstance(new_prizes, list) and len(new_prizes) >= 2:
        prizes = new_prizes
        return jsonify({"status": "ok", "prizes": prizes})
    return jsonify({"status": "error", "message": "奖品列表无效，至少需要 2 个奖品"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
