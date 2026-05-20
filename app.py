from flask import Flask
from datetime import datetime
import socket
import platform

app = Flask(__name__)

@app.route('/')
def home():

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    hostname = socket.gethostname()
    system = platform.system()

    return f"""
    <!DOCTYPE html>
    <html>

    <head>
        <title>DevOps Kubernetes Dashboard</title>

        <style>

            * {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
                font-family: Arial, sans-serif;
            }}

            body {{
                background: linear-gradient(135deg, #0f172a, #1e293b);
                color: white;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
            }}

            .container {{
                width: 90%;
                max-width: 900px;
                background: rgba(255,255,255,0.05);
                border-radius: 20px;
                padding: 40px;
                backdrop-filter: blur(10px);
                box-shadow: 0 0 25px rgba(0,0,0,0.4);
            }}

            h1 {{
                text-align: center;
                color: #38bdf8;
                margin-bottom: 10px;
                font-size: 42px;
            }}

            .subtitle {{
                text-align: center;
                color: #cbd5e1;
                margin-bottom: 40px;
            }}

            .grid {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 20px;
            }}

            .card {{
                background: rgba(255,255,255,0.08);
                padding: 25px;
                border-radius: 15px;
                transition: 0.3s;
            }}

            .card:hover {{
                transform: translateY(-5px);
                background: rgba(255,255,255,0.12);
            }}

            .card h2 {{
                color: #22c55e;
                margin-bottom: 15px;
            }}

            .value {{
                font-size: 20px;
                font-weight: bold;
                color: #f8fafc;
            }}

            .status {{
                text-align: center;
                margin-top: 40px;
                font-size: 22px;
                color: #4ade80;
                font-weight: bold;
            }}

            .footer {{
                text-align: center;
                margin-top: 25px;
                color: #94a3b8;
                font-size: 14px;
            }}

        </style>
    </head>

    <body>

        <div class="container">

            <h1>🚀 DevOps Dashboard</h1>

            <div class="subtitle">
                Jenkins + Docker + Kubernetes CI/CD Pipeline
            </div>

            <div class="grid">

                <div class="card">
                    <h2>📦 Deployment Status</h2>
                    <div class="value">Running Successfully</div>
                </div>

                <div class="card">
                    <h2>⏰ Deployment Time</h2>
                    <div class="value">{current_time}</div>
                </div>

                <div class="card">
                    <h2>🖥️ Hostname</h2>
                    <div class="value">{hostname}</div>
                </div>

                <div class="card">
                    <h2>💻 Platform</h2>
                    <div class="value">{system}</div>
                </div>

            </div>

            <div class="status">
                ✅ Kubernetes Cluster Operational
            </div>

            <div class="footer">
                Built with Flask • Docker • Jenkins • Kubernetes
            </div>

        </div>

    </body>

    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)