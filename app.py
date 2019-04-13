from flask import Flask, request
import json
import mysql.connector
from urllib.parse import unquote

app = Flask(__name__)

credentials = json.load(open("credentials.json", "r"))


@app.route('/info', methods=["GET"])
def info():
    return open("info.txt", "r").read()


@app.route('/tickets', methods=["GET"])
def tickets():
    result_filter = unquote(request.args["filter"])
    database = mysql.connector.connect(
        host=credentials["host"],
        user=credentials["user"],
        passwd=credentials["password"],
        database=credentials["database"]
    )
    cursor = database.cursor()

    like_filter = "'%" + result_filter + "%'"
    command = "SELECT * FROM tickets" \
              " WHERE ticket_name LIKE " + like_filter + \
              " OR student_name LIKE " + like_filter + \
              " OR ticket_number LIKE " + like_filter + \
              " OR email LIKE " + like_filter

    all = "SELECT * FROM tickets"

    cursor.execute(command)
    data = cursor.fetchall()

    cursor.close()
    database.close()

    return json.dumps(data)


if __name__ == '__main__':
    app.run()
