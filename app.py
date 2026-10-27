from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return (
        "<h1>DevOps Demo App V2</h1>"
        "<p>Built with Flask, tested and packaged automatically by a CI/CD pipeline.</p>"
    )


@app.route("/health")
def health():
    return jsonify(status="ok")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
