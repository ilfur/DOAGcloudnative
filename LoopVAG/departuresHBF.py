# Abfahrten Nahverkehr von Nuernberg Hbf
# NLR 2019-09-04
# Python 3.7

import cx_Oracle
import time
import json
import urllib
from urllib.request import urlopen
from datetime import datetime

while True:
#   Abfahrten von Hbf (Code:510) in 5 min (timedelay=5)
    req = urllib.request.Request("https://start.vag.de/dm/api/abfahrten.json/vgn/510/?timedelay=5")
    try:
        response  = urlopen(req)
    except Exception as e:
        print (e.reason)
        time.sleep(30)
        continue
    json_data = response.read().decode('utf-8', 'replace')
    d = json.loads(json_data)
    crow = len(d['Abfahrten'])
#   Connection to ADW
    connection = cx_Oracle.connect("admin", "AutonomousIsAbFab42", "db201910311128_low", encoding="UTF8")
    cursor = connection.cursor()
    statement = 'insert into DEPARTURES (product, linenumber, direction, actual, planned) values (:2, :3, :4, :5, :6)'
    for i in range(0, crow):
        linenumber = d['Abfahrten'][i]['Linienname']
        product    = d['Abfahrten'][i]['Produkt']
        direction  = d['Abfahrten'][i]['Richtungstext']
        actual     = d['Abfahrten'][i]['AbfahrtszeitIst']
        planned    = d['Abfahrten'][i]['AbfahrtszeitSoll']
        a = datetime.fromisoformat(str(actual))
        p = datetime.fromisoformat(str(planned))
        cursor.execute(statement, (product,linenumber,direction,a,p))
    connection.commit()
    connection.close()
    time.sleep(300)
