from flask import Flask, render_template, request, url_for, redirect
import creategraph

app = Flask(__name__)

@app.route('/', methods=('GET', 'POST'))
def home():
	if request.method == 'POST':
		p1 = request.form['p1']
		p2 = request.form['p2']
		p3 = request.form['p3']
		p4 = request.form['p4']
		p5 = request.form['p5']
		data = [p1,p2,p3,p4,p5]
		creategraph.graph(data)
		return redirect(url_for('report'))

	return render_template('index.html')

@app.route('/report', methods=('GET', 'POST'))
def report():
	return render_template('report.html')
