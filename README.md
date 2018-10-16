# Welcome to my build out of a flask app, using templates and a layout for pages. This is the first in a set of guides to build out flask apps, with postresql databases and host onto heroku. 

### Who knows I might even go nuts and make the final version work as an endpoint api as well.

(These guides are being built out on a Mac system so if you are not on a Mac, adjust as needed)

First, 

- Navigate in your terminal where you would like to create your project.

- Lets create a new folder for out project, (You could name this anything, but for the this demo I will be using very basic naming for folders, files, methods, etc.) `mkdir demo_flask_build`

- Now that you have created our base folder, lets `cd demo_flask_build` and inside of that folder create a new file called app.py. `touch app.py`

- This will be our main program file for this app. Most of what we build will be referensed through this file at some point.

- Lets now create our Dev Enviroment, if you are using python3 you will have pip installed already. So lets install pipenv as our enviroment. Run `pip3 install pipenv` in your terminal.

- Just as a side note, so long as you are in demo_flask_build in your terminal, (or what ever you called your project) you are in what is known as the root of your project. (Or the root folder) When we create something in the root folder, such as your app.py it will create it at the "root", so if you run `ls` in your terminal you should see app.py.

- Ok, now back to our enviroment setup. Now that you have pipenv installed, run `pipenv install`

- This will set up your coding enviroment, and create 2 new files for us.  You will see if you run `ls` at your root, that we now have 3 files. app.py which is still empty, and a Pipfile and Pipfile.lock. Which will track the code packages we will need to run this app, and make them avalaible to our coding enviroment that you set up with pipenv.


- Lets push our code at this point to git hub. If you have git installed run the following commands, if you do not, or do not want to use git, skip this step.

- Run `git init`, `git add .`, `git commit -m "Initial commit"`.

- That will create a git repo on your local machine, if you want to push it to git hub feel free to do so now.

### Now that we have all of that set up, lets start adding in our libraries and start coding!

Lets first get our app.py file to load up as a flask app, lets add the following code to our app.py.

On line one
```
from flask import Flask, render_template
```

So we are going to import Flask, and we are going to import render_template.

With these 2 imports in place lets keep going.

on line three
```
app = Flask(__name__)
```
This is our First Parameter, 

The idea of the first parameter is to give Flask an idea of what belongs to your application. This name is used to find resources on the filesystem, can be used by extensions to improve debugging information and a lot more.

So it’s important what you provide there. If you are using a single module, __name__ is always the correct value. (This is what we are doing for this app) If you however are using a package, it’s usually recommended to hardcode the name of your package there. (From the flask docs, link for more information: http://flask.pocoo.org/docs/0.12/api/#application-object)

So once we have that in place lets create our first route, and set up our file to run,

Get your app.py to look like this, (I added comments so you can see what is going on)

```
#importing flask and render templates so we can use flask.
from flask import Flask, render_template

#setting up our app.
app = Flask(__name__)

# Setting up our first route,
@app.route('/')
def index():
	return "<h1>Welcome to my flask app</h1>"

# To check our page and run our app to launch our local host.
if __name__ == '__main__':
	app.debug = True
	app.run()
```

Once you have your code in place lets fire up our server and see what happens!

run the following in your terminal, (This will run your app and spin up a test server, thanks to flask)

`python3 app.py`

This will spin up and you will see something like this in your terminal,

` * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)`

This tells me that my app is running on http://localhost:5000/

If you see a different set of numbers on yours (which is possible), what ever the last number is `http://127.0.0.1:5000/` in this case 5000, that is your local host number. So `http://127.0.0.1:3000/` would be http://localhost:3000/, etc.


So if you can see your, Welcome to my flask app, message, success! You have now spun up a basic small flask app! Next we need to add more functinality and be able to use HTML and CSS pages.

Hit `Control + c` to close your server, and lets move on to the next section!









