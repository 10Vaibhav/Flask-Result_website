# Flask-Result_website

A Flask-based web application for calculating and displaying student exam results.

## Description

This project is a simple web application built with Flask that allows users to input exam scores for different subjects and calculates the average score. It then determines whether the student has passed or failed based on the scores and displays the result.

## Features

- Input form for entering scores in five subjects: DAA, TFCS, BDA, DBMS, and LA
- Calculation of average score
- Pass/Fail determination based on individual subject scores and overall average
- Responsive design
- 
## Code Overview

### app.py

This is the main Flask application file. It contains routes for the home page and result submission. Key functions:

- `welcome()`: Renders the index.html template
- `submit()`: Handles form submission, calculates results, and renders the result.html template

### index.html

The home page template containing the form for score input.

### result.html

The result page template displaying the calculated average and pass/fail status.

### style.css

Contains styles for the input form and general page layout.

### result.css

Contains styles specific to the result page.

## Contributors

- Shantnu Talokar
- Shreyas Chaurey
- Shekhar Nipane
- Vaibhav Mahajan
