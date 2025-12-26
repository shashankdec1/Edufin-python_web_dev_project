# EduFin – Education Finance Tracker (Flask Web Application)

EduFin is a minimal yet complete Flask-based web application designed to help students track and manage education-related expenses such as tuition fees, books, rent, and daily academic costs.
The project demonstrates full-stack web development, clean project structure, and containerized deployment using Docker.

# Project Overview

Managing education expenses manually using notes or spreadsheets is inefficient and error-prone.
EduFin provides a centralized, digital solution that enables students to:

Record expenses easily

View expense history

Get monthly summaries

Access data via REST API

Run the application locally or using Docker

This project follows Python & Git best practices, including virtual environment usage, .gitignore, and dependency management.

#  Problem Statement – Why EduFin?

Students often struggle to monitor education expenses efficiently.
Traditional methods lack automation, insights, and accessibility.

EduFin solves this by providing:

Automatic date & time tracking

Monthly expense summaries

Simple and intuitive UI

Database-backed persistent storage

API access for extensibility

# Key Features

Add education-related expenses

View all recorded expenses

Delete existing expenses

Automatic date & time generation (backend)

Monthly expense summary

REST API endpoint returning JSON data

Clean blue-themed frontend UI

SQLite database integration

Dockerized application for easy deployment

# Technology Stack

Backend

Python

Flask

Frontend

HTML

CSS

Jinja2 Templates

Database

SQLite

Containerization

Docker

Version Control

Git

GitHub

#  Application Routes (Total: 6)
Route	Description
/	Landing / Introduction page
/add	Add a new expense
/expenses	View all expenses
/summary	Monthly expense summary
/api/expenses	REST API (JSON response)
/delete/<id>	Delete an expense
#  Virtual Environment & Dependency Management

A Python virtual environment (venv) was used during development to isolate project dependencies.

The venv folder is excluded from the repository using .gitignore

Dependencies are listed in requirements.txt

This follows best practices since virtual environments are system-specific and cannot be reused across machines

#  Running the Application Locally
# Step 1: Install dependencies

Run the following command in Git Bash / Terminal:

pip install -r requirements.txt

# Step 2: Start the application
python app.py(make sure to run the application in respective python directory)


The application will run on:

http://localhost:5000

# Running the Application Using Docker
Step 1: Build Docker image
docker build -t edufin-app .

Step 2: Run Docker container
docker run -p 5000:5000 edufin-app


# Dev_Team Collaboration

This project was collaboratively developed by:

# Shashank Bangaru (Me)

# Sai Kumar Chintala (Development Teammate)

All tasks including:

Backend development

Frontend design

Database integration

Docker setup

Documentation

were shared efficiently to ensure quick and effective teamwork.

# Conclusion

# EduFin is a complete, minimal Flask web application with real-world relevance.
# It follows standard software engineering practices, clean coding principles, and fulfills all academic project requirements while remaining simple, scalable, and easy to understand.
