from flask import Flask
from datetime import datetime
import socket
import platform
import psutil
import subprocess

app = Flask(__name__)

start_time = datetime.now()


def get_pod_count():
    try:
        output = subprocess.check_output(
            "kubectl get pods --no-headers",
            shell=True
        ).decode()

        pods = output.strip().split('\n')

        return len([p for p in pods if p])

    except:
        return "N/A"


@app.route('/')
def dashboard():

    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    hostname = socket.gethostname()
    system = platform.system()

    uptime = datetime.now() - start_time
    uptime_str = str(uptime).split('.')[0]

    pod_count = get_pod_count()

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return f"""
    <!DOCTYPE html>
    <html>

    <head>

        <title>Real DevOps Monitoring Dashboard</title>

        <meta http-equiv="refresh" content="5">

        <style>

            body {{
                margin: 0;
                background: #0f172a;
                font-family: Arial, sans-serif;
                color: white;
            }}

            .navbar {{
                background: #020617;
                padding: 20px;
                text-align: center;
                font-size: 32px;
                font-weight: bold;
                color: #38bdf8;
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
                background: #1e293b;
                padding: 30px;
                border-radius: 18px;
                box-shadow: 0px 0px 15px rgba(0,0,0,0.3);
            }}

            .title {{
                color: #94a3b8;
                margin-bottom: 15px;
                font-size: 18px;
            }}

            .value {{
                font-size: 38px;
                font-weight: bold;
            }}

            .green {{
                color: #22c55e;
            }}

            .yellow {{
                color: #facc15;
            }}

            .red {{
                color: #ef4444;
            }}

            .footer {{
                text-align: center;
                margin-top: 40px;
                color: #94a3b8;
            }}

        </style>

    </head>

    <body>

        <div class="navbar">
            🚀 Real Kubernetes Monitoring Dashboard
        </div>

        <div class="container">

            <div class="grid">

                <div class="card">
                    <div class="title">CPU Usage</div>
                    <div class="value {'red' if cpu > 80 else 'yellow' if cpu > 50 else 'green'}">
                        {cpu}%
                    </div>
                </div>

                <div class="card">
                    <div class="title">Memory Usage</div>
                    <div class="value {'red' if memory > 80 else 'yellow' if memory > 50 else 'green'}">
                        {memory}%
                    </div>
                </div>

                <div class="card">
                    <div class="title">Disk Usage</div>
                    <div class="value {'red' if disk > 80 else 'yellow' if disk > 50 else 'green'}">
                        {disk}%
                    </div>
                </div>

                <div class="card">
                    <div class="title">Running Pods</div>
                    <div class="value green">
                        {pod_count}
                    </div>
                </div>

                <div class="card">
                    <div class="title">Hostname</div>
                    <div class="value" style="font-size:22px;">
                        {hostname}
                    </div>
                </div>

                <div class="card">
                    <div class="title">Operating System</div>
                    <div class="value" style="font-size:24px;">
                        {system}
                    </div>
                </div>

                <div class="card">
                    <div class="title">Deployment Time</div>
                    <div class="value" style="font-size:22px;">
                        {current_time}
                    </div>
                </div>

                <div class="card">
                    <div class="title">Application Uptime</div>
                    <div class="value" style="font-size:24px;">
                        {uptime_str}
                    </div>
                </div>

            </div>

            <div class="footer">
                Flask • Docker • Jenkins • Kubernetes • Minikube
            </div>

        </div>

    </body>

    </html>
    """


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)