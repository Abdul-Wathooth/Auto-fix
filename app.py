from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return '''
        <h2>Enter a Number</h2>
        <form action="/check">
            <input type="number" name="n">
            <button type="submit">Check</button>
        </form>
    '''

@app.route("/check")
def check():
    n = int(request.args.get("n"))

    if n >= 10:
        return "n is greatest"
    else:
        return "n is not greatest"

app.run(host="0.0.0.0", port=5000)
