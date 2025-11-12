from flask import Flask, render_template
import mysql.connector  # or use sqlite3 if preferred

app = Flask(__name__)

# --- DATABASE CONFIG ---
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'password',  # change this
    'database': 'gaming_platform'         # change this
}


@app.route('/')
def home():
    try:
        # try to connect
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        a=cursor.execute("show tables;")
        conn.close()
        status = "✅ Database Connected Successfully!"
    except Exception as e:
        status = f"❌ Database Connection Failed: {e}"
    return render_template('index.html', status=status)


if __name__ == '__main__':
    app.run(host='192.168.29.155', port=5000, debug=True)

