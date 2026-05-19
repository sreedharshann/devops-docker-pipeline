from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>DevOps CI/CD Project</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #0f172a;
                    color: white;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                }

                .container {
                    text-align: center;
                    background: #1e293b;
                    padding: 40px;
                    border-radius: 15px;
                    box-shadow: 0 0 20px rgba(0,0,0,0.4);
                }

                h1 {
                    color: #38bdf8;
                }

                p {
                    font-size: 18px;
                }

                .status {
                    margin-top: 20px;
                    color: #22c55e;
                    font-weight: bold;
                }
            </style>
        </head>

        <body>
            <div class="container">
                <h1>🚀 DevOps CI/CD Pipeline</h1>

                <p>Flask Application Successfully Deployed</p>

                <div class="status">
                    ✅ Jenkins + Docker Pipeline Running
                </div>
            </div>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)