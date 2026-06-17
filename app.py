from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>🚀 CI/CD Demo App</h1>
    <p>GitHub Actions + Docker Hub</p>
    """

@app.route('/version')
def version():
    return {"version": "1.0"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)