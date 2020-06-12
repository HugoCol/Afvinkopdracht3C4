# import modules
from flask import Flask, render_template, request
import mysql.connector

# app instance
app = Flask(__name__)


# commit test
# landing page
@app.route('/', methods=["POST", "GET"])
def database():
    '''
    input: user input to search the database
    :return: results from the dynamic database query
    '''
    if request.method == "POST":
        resultlist = []
        userinput = request.form.get("search", "")
        # connect to db
        conn = mysql.connector.connect(host="ensembldb.ensembl.org",
                                       user="anonymous",
                                       db="homo_sapiens_core_95_38")
        cursor = conn.cursor()
        # select everything which correlates to the user search term
        query = "select * from gene where description like \"%" + \
                userinput \
                + "%\""
        cursor.execute(query)
        # add every returned row from the database to a list
        for row in cursor:
            resultlist.append(row[9])
        cursor.close()
        conn.close()

        return render_template("Home.html",
                               resultlist=resultlist, )
    else:
        return render_template('Home.html',
                               resultlist='')


if __name__ == '__main__':
    app.run()
