from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Kartheek'}
    return render_template('index.html', user=user)

if __name__ == "__main__":
	app.run()