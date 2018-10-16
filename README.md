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




