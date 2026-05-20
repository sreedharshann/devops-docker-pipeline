from flask import Flask
import random
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def dashboard():

    cpu = random.randint(20, 95)
    memory = random.randint(30, 90)
    pods = random.randint(2, 5)

    current_time = datetime.now().strftime("%H:%M:%S")

    return f"""
    <!DOCTYPE html>
    <html>

    <head>

        <title>Kubernetes Monitoring Panel</title>

        <style>

            body {{
                margin: 0;
                padding: 0;
                background-color: #050816;
                color: #00ffcc;
                font-family: Consolas, monospace;
            }}

            .header {{
                background-color: #0b1120;
                padding: 20px;
                text-align: center;
                font-size: 36px;
                font-weight: bold;
                border-bottom: 2px solid #00ffcc;
            }}

            .container {{
                padding: 40px;
            }}

            .grid {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 25px;
            }}

            .card {{
                background-color: #111827;
                padding: 30px;
                border-radius: 15px;
                box-shadow: 0px 0px 15px rgba(0,255,204,0.2);
                transition: 0.3s;
            }}

            .card:hover {{
                transform: scale(1.03);
                box-shadow: 0px 0px 25px rgba(0,255,204,0.5);
            }}

            .title {{
                font-size: 18px;
                margin-bottom: 15px;
                color: #94a3b8;
            }}

            .value {{
                font-size: 40px;
                font-weight: bold;
            }}

            .online {{
                color: #22c55e;
            }}

            .warning {{
                color: #facc15;
            }}

            .danger {{
                color: #ef4444;
            }}

            .footer {{
                text-align: center;
                margin-top: 50px;
                color: #64748b;
            }}

        </style>

    </head>

    <body>

        <div class="header">
            ⚡ Kubernetes Cluster Monitoring Dashboard
        </div>

        <div class="container">

            <div class="grid">

                <div class="card">
                    <div class="title">CPU Usage</div>
                    <div class="value">{cpu}%</div>
                </div>

                <div class="card">
                    <div class="title">Memory Usage</div>
                    <div class="value">{memory}%</div>
                </div>

                <div class="card">
                    <div class="title">Running Pods</div>
                    <div class="value">{pods}</div>
                </div>

                <div class="card">
                    <div class="title">Cluster Status</div>
                    <div class="value online">ONLINE</div>
                </div>

                <div class="card">
                    <div class="title">CI/CD Pipeline</div>
                    <div class="value online">ACTIVE</div>
                </div>

                <div class="card">
                    <div class="title">Deployment Time</div>
                    <div class="value" style="font-size:28px;">
                        {current_time}
                    </div>
                </div>

            </div>

            <div class="footer">
                Powered by Flask • Docker • Jenkins • Kubernetes
            </div>

        </div>

    </body>

    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)