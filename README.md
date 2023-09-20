# HogwartsApp
HogwartsApp: a small data analytics project

## Description
This is a demo project that represents a hypothetical situation for a company that has a web application. The entry point is a set of data and related questions. The desired outcome is, apart from the analytical answer to these questions, to run a whole project using best practices and simulate the role of Data Analyst as an information broker at the centre of the organisation. On the technical side, that includes the application code, plus a pdf presentation of the results addressing the main stakeholders.

This mini project is developed in Python.

## Contents and Structure
README.md - the current file

hogwarts_requirements.txt - the required libraries

documentation.md - a simple fusion of user/technical documentation, vision statement, etc.

hogwarts_app_metrics_presentation.pdf - the presentation prepared for the stakeholders

### The HogwartsApp
We have built the HogwartsApp, for the students of the four houses of Hogwarts -the school of witchcraft and wizardry. We have access to the data being produced by the users and we would like to get insights into how the app is being used.

### The dataset
The data come from two sources within the app:
- 1 The User registry that holds 3 pieces of information:
    - The user identification.
    - The timestamp that represents when the user registered with the service.
    - The house where the student is enrolled: Gryffindor, Hufflepuff, Ravenclaw, and Slytherin.
- 2 The Actions registry that holds another 3 pieces of information
    - The user identification.
    - The timestamp that represents when the user performed an action.
    - The kind of action performed chosen from a wide range of actions offered by the app.

### Tentative objectives
Given the data, we have three main objectives that we address in the analysis:
- 1  We would like to provide an answer to certain questions with respect our users and the ways in which they use the app. In specific:

    - Which Hogwarts house has the most active students?

    - Which are the most active students in terms of total time spent performing actions and total number of actions performed?

    - What is the average duration of a user session? Which student has spent the longest uninterrupted session? For our purposes a session is defined as the time interval between two actions, but only if these actions take place less than 5 minutes apart; if two actions take place more than 10 minutes apart, then they are not part of the same session.

- 2 We would like to define a series of useful metrics on user engagement, analyse them and represent them graphically.

- 3 We would like to prepare a presentation for the business stakeholders where we communicate our main findings.
