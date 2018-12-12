Logs Analysis
Jizong Liang

### About

A project from Udacity Full Stack Nanodegree. The task is to build a reporting tool that prints out reports (in plain text) based on the data in the

database. This reporting tool is a Python program using the psycopg2 module to connect to the database.

The database includes newspaper articles and web server log for the site.

We do the following 3 queries to draw business conclusions from the data

* What are the most popular three articles of all time?

* Who are the most popular article authors of all time?

* On which days did more than 1% of requests lead to errors?


## How To Run?

You will need:

* Python 3

Check out the details [here](https://www.python.org/downloads/release/python-371/) to download python 3.

* Vagrant

You can download Vagrant from the official website [here](https://www.vagrantup.com/downloads.html), but you will need to manually config all the packages

and setting in order to run this program, I recommend you to download it from [here](https://github.com/JizongL/fullstack-nanodegree-vm), it

includes PostgreSQL database and support software needed for this project.

* VirtualBox

Check out the details [here](https://www.virtualbox.org/wiki/Downloads)


### Setup

Install Vagrant And VirtualBox

### To Run

Launch Vagrant VM and log in

```terminal
vagrant up
`vagrant ssh`
```

To download the data [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

You will need to unzip this file after downloading it. The file inside is called `newsdata.sql`. Put this file into The

`vagrant` directory, which is shared with your virtual machine.

To load the data, use the following command.  

```terminal
psql -d news -f newsdata.sql
```

The newsdata database includes three tables:

* Authors table

* Articles table

* Log table

To execute the program, run  

```terminal
python3 log_analysis_2018.py
```
