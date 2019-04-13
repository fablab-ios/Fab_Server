from flask import Flask, request
import json
import mysql.connector

app = Flask(__name__)

credentials = json.load(open("credentials.json", "r"))


@app.route('/info', methods=["GET"])
def info():
    return open("info.txt", "r").read()


@app.route('/tickets', methods=["GET"])
def tickets():
    database = mysql.connector.connect(
        host=credentials["host"],
        user=credentials["user"],
        passwd=credentials["password"],
        database=credentials["database"]
    )
    cursor = database.cursor()

    since_timestamp = request.args.get("since")
    if since_timestamp is None:
        since_timestamp = "0"
    cursor.execute("SELECT * FROM tickets where timestamp > '" + since_timestamp + "'")
    data = cursor.fetchall()

    cursor.close()
    database.close()
    return json.dumps(data)


if __name__ == '__main__':
    app.run()
