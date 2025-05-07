import pandas as pd
import sqlite3
import numpy as np
from flask import Flask, jsonify, render_template
# Reconnect to the database
conn = sqlite3.connect('sales_data.db')

# Read the data into a pandas DataFrame
df = pd.read_sql_query('SELECT product, SUM(quantity) as total_quantity FROM sales GROUP BY product', conn)

conn.close()

# Convert the DataFrame to a dictionary for Chart.js
data_dict = df.to_dict(orient='list')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('./chart.html')

@app.route('/data')
def data():
    return jsonify(data_dict)

app.run(host='0.0.0.0', port=8000)