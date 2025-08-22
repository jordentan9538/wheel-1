from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# 奖品列表（你可以自己改）
prizes = ["一等奖", "二等奖", "三等奖", "四等奖", "五等奖", "谢谢参与"]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/spin")
def spin():
    # 随机选择一个奖品
    index = random.randint(0, len(prizes) - 1)
    prize = prizes[index]
    return jsonify({"index": index, "prize": prize})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
