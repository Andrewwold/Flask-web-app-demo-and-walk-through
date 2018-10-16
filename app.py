#importing flask and render templates so we can use flask.
from flask import Flask, render_template

#setting up our app.
app = Flask(__name__)

# Setting up our first route,
@app.route('/')
def index():
	return render_template('index.html')

# To check our page and run our app to launch our local host.
if __name__ == '__main__':
	app.debug = True
	app.run()