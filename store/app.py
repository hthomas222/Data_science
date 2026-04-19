from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/leonism/sample-superstore/master/data/superstore.csv')




app = Flask(__name__)

@app.route('/')
def index():
	info = df.describe().to_html(classes="table", border=0)
	ty = df.dtypes.to_frame("dtype").to_html(classes="table", border=0)
	rows, cols = df.shape
	return render_template("index.html", info=info, ty=ty, rows=rows, cols=cols)


if __name__ == '__main__':
     app.run(port=1234, debug=True)
