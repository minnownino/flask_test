from flask import Flask, render_template, request, json, url_for, g

import MySQLdb

app = Flask(__name__)

def connect_db():
	mydb = MySQLdb.connect('localhost', 'root', 'root', 'TDI_PanCancerAtlas')
	cursor = mydb.cursor()
	return mydb, cursor

def get_db():
	"""
	opens a new connections
	"""
	if not hasattr(g, 'mysql'):
		g.mysql = connect_db()
	return g.mysql

@app.teardown_appcontext
def close_db(error):
	"""
	close database at the end of the reques
	"""
	if hasattr(g, 'mysql'):
		g.mysql.close()




@app.route('/')
def main():
	sql = "select Hugo_Symbol from Somatic_Mutations limit 1"
	mydb, cursor = connect_db()
	cursor.execute(sql)
	result = cursor.fetchall()[0][0]
	return render_template("index.html", result = result)

if __name__ == '__main__':
    app.run()
