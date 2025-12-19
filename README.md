# Edufin-python_web_dev_project

We used a Python virtual environment during development. The environment itself is excluded from the repository using .gitignore, and dependencies are defined in requirements.txt


# Project Overview
EduFin is a Flask-based web application designed to help students track and manage their education-related expenses such as tuition fees, books, rent, and daily academic costs.

This application demonstrates the use of:


Backend logic with Python Flask


Frontend–backend interaction


SQLite3Database integration


Containerization using Docker


Creating Venv and gitgnore for best structure(venv cant be accessed in different PC)
while following clean coding practices and minimal project structure.

# Problem Statement and why Edufin
Students often struggle to monitor their education expenses efficiently.
Traditional methods like manual notes or spreadsheets are error-prone and difficult to maintain in this modern world where everyone are into Tech application 

EduFin addresses this problem by providing a centralized expense tracking system, Automatic date and time recording ,Monthly expense summaries and simple and intuitive user interface.

# Our project Edufin Key features
1.Add education-related expenses


2.View all recorded expenses


3.Delete existing expenses


4.Automatic date and time generation on the backend


5.Monthly expense summary


6.REST API endpoint returning expenses in JSON format


7.Clean blue-themed frontend UI


8.SQLite database integration


9.Dockerized application for easy deployment

# Technology used

 Backend: Python, Flask
 
 
 Frontend: HTML, CSS (Jinja2 Templates)
 
 
 Database: SQLite
 
 
 Containerization: Docker
 
 
 Version Control: Git & GitHub


# Application Routes we used total 6 routes
 
 Route            Description                 


/`              Landing / introduction page 

 
 `/add`           Add a new expense           
 
 
 `/expenses`      View all expenses           
 
 
 `/summary`       Monthly expense summary     
 
 
 `/api/expenses`  JSON API endpoint           
 
 
 `/delete/<id>`   Delete an expense     

# virtual environment 
Python virtual environment was used during development to isolate dependencies.
The virtual environment directory was intentionally excluded from version control using .gitignore, following Python and Git best practices as we canr access same venv into different PC
but all the dependencies are mentioned in requirements.txt.

# procedure to run the application(local)

write in git bash


"pip install -r requirements.txt" (# this command is used to install all the required packages)


python app.py (# to run the program

# procedure to run using docker

docker build -t edufin-app .


docker run -p 5000:5000 edufin-app

# developers collaboration(Team collaboration)
This project was developed by shashankbangaru(me) & saikumarchintala(my dev_mate)
Every Tasks such as development,frontend design, DB integration,docker setup & document setup were shared between us to result quick & effective teamwork

# Demo video : 
a short demo video in the repo is included with repository regarding application functionality,expense creation, monthly summary & docker execution

# Conclusion
EduFin is a complete  minimal Flask web application with real-world relevance.
The project follows standard software development practices and fulfills all project course requirements while remaining simple, clean, and easy to understand with required project demands as instructed.


