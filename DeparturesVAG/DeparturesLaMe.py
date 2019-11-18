# DeparturesLaMe.py

from flask import Flask, Response
import cx_Oracle
import json

app = Flask(__name__)
@app.route("/departureslame")


def departureslame():
        connection = cx_Oracle.connect("admin", "ADMIN_PWD", "TNS_SERVICE_NAME", encoding="UTF8")

        output = ''
        cursor = connection.cursor()
        cursor.execute("""select product, linenumber, direction, to_char(actual,'hh24:mi') "aktuell" \
                          from (select distinct product, linenumber, direction, actual from departures order by actual desc) \
                          where rownum<9""")
        for product, linenumber, direction, aktuell in cursor:
            output = output + product + ' ' + linenumber + ' => ' + direction + ': ' + aktuell + ' *** '

        print(json.dumps({ "frames": [{ "text":output, "icon":"i2782" }]}))
        return(Response(json.dumps({ "frames": [{ "text":output, "icon":"i2783" }]}), mimetype='application/json'))

# 87 Smile, 3253 Beer, 2782 Bus, 6582 Lea, 6216 R2D2
