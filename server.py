from flask import Flask, render_template
import jinja2

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello world! What a bogger!"


if __name__ == "__main__":
    app.run(debug=True)
