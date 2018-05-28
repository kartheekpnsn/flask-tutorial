from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/Search', methods = ['GET', 'POST'])
def search():
    if request.method == "POST":
        keyword = request.form['keywords']
        authors = {
         'Klein Stefan': {'score': 0.25},
         'Ohs JanHendrik': {'score': 0.5},
         'Schoenbauer Stefan': {'score': 0.25}
        }
        authors[keyword] = {'score' : 1}
        return render_template('index.html', authors = authors)

if __name__ == "__main__":
	app.run()