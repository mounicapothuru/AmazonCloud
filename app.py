from flask import Flask, render_template, jsonify, request
from sqlalchemy import create_engine, types
import pymysql
from pymysql import Error
import pandas as pd


app= Flask(__name__)



sqlEngine = create_engine('mysql+pymysql://root:Mounica@92@localhost:3307/instacart', pool_recycle=3600)

@app.route("/")
def index():
    return render_template('Home.html')


@app.route("/query/<query>",methods=['GET','POST'])
def home(query):
    dbConnection = sqlEngine.connect()
    try:
        columns=[]
        data=[]
        QueryResult = []
        df_insta = pd.read_sql(query, dbConnection)

        for row in df_insta.columns:
            columns.append(row);

        QueryResult.append(columns)
        QueryResult.append(df_insta.to_dict('records'))
        #QueryResult.append(data)


    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:

        dbConnection.close()
        print("MySQL connection is closed")
    return jsonify(QueryResult)


if __name__== "__main__" :
    app.run(debug=True)
