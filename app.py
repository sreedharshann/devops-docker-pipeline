from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return f"""
    <html>
        <head>
            <title>CI/CD Verification App</title>

            <style>
                body {{
                    background: linear-gradient(to right, #1e3c72, #2a5298);
                    color: white;
                    font-family: Arial, sans-serif;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                }}

                .card {{
                    background-color: rgba(0,0,0,0.3);
                    padding: 40px;
                    border-radius: 20px;
                    text-align: center;
                    box-shadow: 0px 0px 20px rgba(0,0,0,0.4);
                }}

                h1 {{
                    font-size: 40px;
                    margin-bottom: 10px;
                }}

                .success {{
                    color: #00ff99;
                    font-size: 24px;
                    margin-top: 20px;
                }}

                .time {{
                    margin-top: 20px;
                    font-size: 18px;
                    color: #ffd166;
                }}
            </style>
        </head>

        <body>
            <div class="card">
                <h1>🚀 CI/CD Pipeline Verified</h1>

                <p>Your Jenkins + Docker deployment is working!</p>

                <div class="success">
                    ✅ New Version Successfully Deployed
                </div>

                <div class="time">
                    Deployment Time: {current_time}
                </div>
            </div>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)