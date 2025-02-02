# Overview
This project is a Flask web application that manages and displays information about staff members, including their research impact scores and suggestions for further research based on their expertise.

# Key Components
## Flask Application Setup:

The application is created using the Flask framework.
The app.py file is the main entry point for the application.

## Staff Data:

A list of dictionaries (staff_data) contains information about staff members, including their name, number of publications, citations, H-index, and expertise.

## Impact Score Calculation:

The calculate_impact_score function calculates a research impact score for each staff member based on their publications, citations, and H-index.
Weights are assigned to each of these metrics to compute the final score.

## Suggestions Generation:

The generate_suggestions function provides research suggestions based on the staff member's expertise.

## Routes:

> /: The index route displays the staff members sorted by their impact scores.

> /add_staff: A POST route to add new staff members to the list.

> /dashboard: Displays aggregated metrics like total publications, citations, and H-index for all staff members.
