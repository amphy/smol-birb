# A Small Riot API Sample Application

This was created for [SAIL 2019](https://sail.cs.illinois.edu/) at the University of Illinois at Urbana-Champaign. The course is intended to be a 50 minute course to introduce students with no prior programming knowledge to the development and deployment cycle. 

Objectives for this course:
- Set-up a development environment
- Know how to use tools like Git/GitHub and Heroku
- Program a small Flask application
- Learn to use an external API

## Requirements

### Installations
- [Python3](https://www.python.org/downloads/)
- [Flask](http://flask.pocoo.org/)
- [Cassiopeia](https://github.com/meraki-analytics/cassiopeia)
- [Git](https://git-scm.com/downloads)
- [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)

### Accounts
- [GitHub Account](https://github.com/)
- [Heroku Account](https://heroku.com/)
- [Riot API Developer](https://developer.riotgames.com/)

You will also need your favorite text editor. I personally like to use [Sublime Text](https://www.sublimetext.com/).

## Tutorial

The tutorial will be broken into a few steps.

### Setting up your environment

First, sign up for both [Heroku](https://heroku.com/) and [GitHub](https://github.com/). Also sign up for an account on the [Riot API Developer](https://developer.riotgames.com/) website. Feel free to go ahead and generate a **Development API Key** after you register since we will need it later.

Next, make sure you have Python 3 installed. If you don't, there are a [few tutorials](https://realpython.com/installing-python/) on the web you can find for your particular system.

Once you have Python 3 installed, you can install Flask and Cassiopeia using `pip` or `pip3`. You may want to do this in a `virtualenv` ([more info](https://realpython.com/python-virtual-environments-a-primer/)), but for this tutorial, it isn't necessary.

```
$ pip3 install cassiopeia
$ pip3 install Flask
```

We will start by [creating a new GitHub repository](https://help.github.com/en/articles/create-a-repo). We can name this repository whatever we want (I named mine "smol-birb"). You can also make a short description. If you do not have a [Student Account](https://education.github.com/pack) for GitHub, you will most likely select "Public" for the visibility of your repository. Finally, we want to initialize our repository with a README.

Next, we will [clone this folder](https://help.github.com/en/articles/cloning-a-repository) onto our local machine. This can be done by looking for the bright green "Clone or download" button on the main page of the repository and getting the clone URL. Then, open **Terminal** or **Git Bash Shell** (if you're on Windows). We want to clone this repository to our machine by using

```
$ git clone [clone URL]
```

Then, just navigate to your cloned directory and we can begin to setup and code the application!

### Setting up and coding the application

First, make sure you've generated a [development API key](https://developer.riotgames.com/api-keys.html) for the Riot API. There are instructions on the linked page as well as more information about the different type of API keys. The most important thing to remember is that we **DO NOT** want to ever expose the key anywhere, so keep that in mind when developing future applications. To avoid that, we will put our API key in the environment variables (which we will discuss later), but you could also use a config file that is [gitignored](https://help.github.com/en/articles/ignoring-files.

Next, let's set up our files. In the folder that was created when you cloned your repository (should be the name of your repository), we want to create the following structure (README.md should already be included):

```
your-repository-name
  |_ static
  |_ templates
  |_ README.md
```

As a note, I use the term directory and folder interchangeably.

Our `root` directory is the directory that everything is located in (in this case, `your-repository-name`).

The `static` folder will be used for any resources that won't change once the app is built (i.e. CSS files, JS files, image files) and the `templates` folder will contain our HTML templates for our site. These templates will allow us to have a standardized look for each page, but still be able to change the information inside the page.

In our `root` directory, we want to create a file called `server.py`. The `.py` specifies that it is a Python file. With this, we have finished setting up the structure of the application and can now begin coding!

**TBC, but to start you can take a look at server.py**

To run the app locally, we will want to first set up our environmental variables using:

```
export FLASK_APP=server.py
export RIOTAPI_KEY=[Your Key Here]
```

This sets up our Flask app as server.py and also hides away our Riot API Key (so we don't accidentally reveal it).

Then, you can run `python3 server.py` or `python server.py` to start the application locally.

### Deploy to Heroku

There are two ways to deploy to Heroku. You can deploy directly to Heroku using `heroku create` in the directory, or you can hook up an existing Heroku application to a GitHub repository. 
