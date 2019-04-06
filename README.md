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

You will also need your favorite text editor. I personally like to use [Sublime Text](https://www.sublimetext.com/).

## Tutorial

The tutorial will be broken into a few steps.

### Setting up your environment

First, sign up for both [Heroku](https://heroku.com/) and [GitHub](https://github.com/).

Next, make sure you have Python 3 installed. If you don't, there are a [few tutorials](https://realpython.com/installing-python/) on the web you can find for your particular system.

Once you have Python 3 installed, you can install Flask and Cassiopeia using pip or pip3.

```
$ pip3 install cassiopeia
$ pip3 install Flask
```

We will start by [creating a new GitHub repository](https://help.github.com/en/articles/create-a-repo). We can name this repository whatever we want (I named mine "smol-birb"). You can also make a short description. If you do not have a [Student Account](https://education.github.com/pack) for GitHub, you will most likely select "Public" for the visibility of your repository. Finally, we want to initialize our repository with a README.

Next, we will [clone this folder](https://help.github.com/en/articles/cloning-a-repository) onto our local machine. This can be done by looking for the bright green "Clone or download" button on the main page of the repository and getting the clone URL. Then, open **Terminal** or **Git Bash Shell** (if you're on Windows). We want to clone this repository to our machine by using

```
$ git clone [clone URL]
```

Then, just navigate to your cloned directory and we can begin to code the application!

### Coding the application
TBC, but for the most part, can just use the code in smol-birb repository

### Deploy to Heroku

There are two ways to deploy to Heroku. You can deploy directly to Heroku using `heroku create` in the directory, or you can hook up an existing Heroku application to a GitHub repository. 
