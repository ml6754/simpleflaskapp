from flask import Flask
app = Flask(__name__)

#pages
@app.route("/")
def home():
    return "Simple Flask App"

if __name__ == '__main__':
    app.run(debug=True)