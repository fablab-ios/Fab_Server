from flask import Flask, request
import json
import mysql.connector
from urllib.parse import unquote

app = Flask(__name__)

credentials = json.load(open("credentials.json", "r"))


@app.route('/info', methods=["GET"])
def info():
    return json.dumps({
        "info": open("info.txt", "r").read()
    })


@app.route('/tickets/<email>', methods=["GET"])
def tickets(email):
    database = mysql.connector.connect(
        host=credentials["host"],
        user=credentials["user"],
        passwd=credentials["password"],
        database=credentials["database"]
    )
    cursor = database.cursor()

    command = "SELECT * FROM tickets where email='" + email + "'"

    cursor.execute(command)
    data = cursor.fetchall()

    cursor.close()
    database.close()

    return json.dumps(data)


@app.route("/notifications/<email>", methods=["GET"])
def notifications(email):
    database = mysql.connector.connect(
        host=credentials["host"],
        user=credentials["user"],
        passwd=credentials["password"],
        database=credentials["database"]
    )
    cursor = database.cursor()

    cursor.execute("SELECT * FROM notifications where email='" + email + "';")
    data = cursor.fetchall()

    cursor.execute("DELETE FROM notifications where email='" + email + "';")
    database.commit()

    cursor.close()
    database.close()

    return json.dumps(data)


if __name__ == '__main__':
    app.run()
