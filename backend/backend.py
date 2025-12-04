from flask import Flask, jsonify
from flask_cors import CORS
import os
import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)
CORS(app)

MYSQL_HOST = os.getenv('MYSQL_HOST', 'mysql-service')
MYSQL_USER = os.getenv('MYSQL_USER', 'appuser')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', 'apppassword')
MYSQL_DB = os.getenv('MYSQL_DB', 'appdb')

@app.route('/')
def home():
    return "<h1 style='color:green;text-align:center;margin-top:100px'>Backend Running Successfully!</h1><h2>DevOps Final Project – Abdelrahman Hamdy</h2>"

@app.route('/health')
def health():
    return jsonify({"status": "OK", "message": "Backend is healthy"})

@app.route('/db-test')
def db_test():
    try:
        conn = pymysql.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DB,
            connect_timeout=5
        )
        with conn.cursor() as cur:
            cur.execute("SELECT 'DB Connected!' as status")
            result = cur.fetchone()
        conn.close()
        return jsonify({"db": result})
    except Exception as e:
        return jsonify({"db_error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
