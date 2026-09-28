from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return '''
    <html>
        <head><title>Jenkins CI/CD Demo</title></head>
        <body>
            <h1>Jenkins CI/CD Deployment Successful!</h1>
            <p>Application deployed successfully on AWS EC2 using Docker.</p>
            <p>GitHub -> Jenkins -> Docker Hub -> EC2</p>
        </body>
    </html>
    '''

@app.route("/health")
def health():
    return {"status": "UP", "message": "Application is running successfully"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
