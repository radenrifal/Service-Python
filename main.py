import pymysql
from config.app import app
from config.configuration import mysql
from flask import request, json, jsonify, flash

#get data member detail
@app.route('/changes')
def changesQuery():
    try:
        conn      = mysql.connect()
        cursor    = conn.cursor(pymysql.cursors.DictCursor)
        sqlQuery  = "CREATE TABLE adm_users (id BIGINT(20), username VARCHAR(255), password VARCHAR(255), name VARCHAR(255))"
        cursor.execute(sqlQuery)
        conn.commit()
        respone   = jsonify('Changes query successfully!')
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close() 

@app.errorhandler(404)
def showMessage(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone
        
if __name__ == "__main__":
    app.run()