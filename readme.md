# Smart Trolley Server
This is a set of instructions to run the server. This file exists so that you guys can understand what the actual fuck is going on. I will try to make it simple, but in case you dont understand, cry and beg for help (hope that this readme is fairly simple to understand and you dont end up in that situation)

# Understanding the tech

This backend has 2 major parts. <br>
<ol>
 <li> The python server
 <li> The database
</ol>

The python server is implemented using a python framework called FastAPI and for the database we are using PostgreSQL. (Why you ask? BECAUSE I SAID SO!!! Now if you dont have any other dumb questions lets move on.)

This folder (`smart-trolley-server`) has many files.<br> 
The start point of the file is the `main.py` file. It has all the api endpoints defined in it(the things that start with `@app`). I have tried my level best to add comments to the code so that you can understand whats happening in there. <br>
The `models.py` file defines what your database table will look like.<br>
The `db.py` file will connect to the database and talk to it. <br>
The `settings.py` file will read the environment variables and set them up for you.(More about environment variables what and how are explained ahead. Chill!!) <br>


# Installation and setup

This is the most important part and painful part. This has many moving parts and many things might go wrong. If anything goes wrong, stay strong and google your errors. 99% of the time the solutions on stackoverflow will help you (if it doesnt, then it is safe to assume that the Gods of the seven hells have forsaken you and there is no hope in the world. Or maybe you could just delete everything and start from the beginning.)

## Installing python
I hope you have this done if not, I dont know what to say other than go to https://www.python.org/downloads/ and download the latest version of python.

## Creating a virtual environment
Once you have python installed, you need to create a virtual environment. This is a folder that will contain all the python packages that you will need for this project. This will help you keep your system clean and not mess up with the packages that you have installed globally. To create a virtual environment, open your terminal and type the following command:
```
python3 -m venv venv
```
This will create a folder called `venv` in your current directory. This folder will contain all the python packages that you will need for this project. Now just creating the folder is just like your brain. Just coz it is there doesnt mean that it is useful. To use the virtual environment, you need to activate it. To activate this virtual environment, type the following command:
```
source venv/bin/activate
```
This will activate the virtual environment. Now if you type `which python` in your terminal, you will see that the path is now pointing to the python executable in the `venv` folder. This means that you are now using the python executable in the `venv` folder. This is the python executable that you will use for this project. Now if you type `pip list` you will see that there are no packages installed. This is because we have not installed any packages yet. To install all the necessary packages for the project, type the following command:
```
pip install -r req.txt
```

## Installing PostgreSQL

This is the database that we will be using. To install this, go to https://www.postgresql.org/download/ and download the latest version of PostgreSQL. Once you have installed it, you need to create a database. To do this, open your terminal and type the following command:
```
sudo -u postgres createuser -s $USER 
```
Now might be asked for your password.If asked, Enter your password and press enter.This will create a user with the same name as your username. Now type the following command:
```
sudo -u postgres psql
```
Doing this will open the postgres terminal.<br>
To view all the databases, type the following command:
```
\l
```
This will list out all the databases that are currently in your system.

Now type the following command:
```
CREATE DATABASE products;
```
Now that we have the database, we need a password in oder to connect to the database. To do this, type the following command:
```
\password
```
Enter and reenter your password . This will set the password for the user that you have created.


Here is a guide for help with installing and setting up PostgreSQL In case you get stuck.
`https://www.digitalocean.com/community/tutorials/how-to-install-postgresql-on-ubuntu-20-04-quickstart`<br>

## Setting up environment variables

In this folder there should be a file called `template.local.env`. Now create a new file called `.env` and use the `template.local.env` file as a template. Fill in the values for the environment variables. The values for the environment variables are explained in the template file. In case you get confused, just copy paste this into your `.env` file and change the values.
```
DATABASE_NAME="products"
DATABASE_USERNAME="postgres"
DATABASE_PASSWORD="your_postgres_password" (the password that you set in the previous step)
DATABASE_HOSTNAME="localhost"
```

# Understanding what you just did(and why).

You need python as this is a python project. You need postgres as db. Installing them is pretty straight forward.<br>
The reason that you created a virtual env is so that you dont mess up with the packages that you have installed globally. You need to activate the virtual env everytime you want to run the server. So dont forget to do that.<br>
It is a good practice to keep your environment variables in a file called `.env`. This is because you dont want to share your passwords and other credentials with the world.<br>

## Understanding the `settings.py` file
This file will read the values from the .env file and store in the variables inside the class. This is done so that you dont have to read the .env file everytime you want to use the environment variables. This will also help you in case you want to change the environment variables. You can just change the values in the .env file and restart the server. You dont have to change the code anywhere else.

# Running the server
Now if you have survived the whole ordeal, you are ready to run the server. To run the server, type the following command:
```
uvicorn main:app --reload
```
If you see something like 
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [678345] using watchgod
INFO:     Started server process [678378]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```
Then you have successfully started the server. Now you can go to http://127.0.0.1:8000 and you will see the hello world message.

## Creating products in the database
When you first start the server, the table will be created in the database. But the table will be empty. <br>
To add products to the database, just edit the `script.py` file and run the file. This will add products to the database. <br>

## Things you need to do
You need to update the `rpi.py` file. Add the code to read the rfid using the rpi and do as the comments in the file says. <br>

# Conclusion
This should be enough to get you started. If you have any questions, feel free to ask me. I will try my best to answer them. <br>
ps: You owe me 


