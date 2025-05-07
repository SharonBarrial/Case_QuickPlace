from flask import Flask, jsonify, render_template
import psutil
from datetime import datetime
import logging

# Initialize Flask app
app = Flask(__name__)

# Enable logging to monitor errors or important information
logging.basicConfig(level=logging.INFO)

# Function to fetch system statistics
def get_system_stats():
    try:
        memory = psutil.virtual_memory().percent
        cpu = psutil.cpu_percent(interval=1)
        disk = psutil.disk_usage('/').percent
        return {
            'time': datetime.now().strftime('%H:%M:%S'),
            'ram': memory,
            'cpu': cpu,
            'disk': disk
        }
    except Exception as e:
        logging.error(f"Error fetching system stats: {e}")
        return {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    stats = get_system_stats()
    return jsonify(stats)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
