# cs333-final
Kirin Hardinger, Spring 2023

# Welcome to the amazing world of Pokémon! (but mini)

## Description

Enjoy a mini version of a Pokémon battle simulator! Play locally with a friend as you each choose a team of 3 Pokémon and battle to the very end.

## How to run
To most reliably run this code and ensure all dependencies are included, a Docker image can be pulled at this repository: https://hub.docker.com/repository/docker/khardinger/cs333-final/general

The main program can be executed using Docker by pulling the latest image from Dockerhub, then running it using the following command:

`docker run -i khardinger/cs333-final:latest`

__It is important that the `-i` is included so that it is run interactively!__

## Testing information
Testing is executed using Python's `unittest` and measured using `Coverage.py`

Documentation for both can be found here:  
https://docs.python.org/3/library/unittest.html  
https://coverage.readthedocs.io/en/7.2.4/

This test suite includes <u>19</u> unit tests and <u>6</u> integration tests.

## Deployment information

The workflow for this GitHub repository is set up such that a Docker image is only pushed to DockerHub if test suite passes with 75%+ code coverage. The latest image can be pulled from: https://hub.docker.com/repository/docker/khardinger/cs333-final/general

## Update log
<b>19-April-2023</b>      
GitHub repository is initialized as a central codebase

<b>25th-April-2023</b>    
Design and planning document is drafted

<b>27th-April-2023</b>    
Initial project setup - draft of main functions, classes, and workflow to automate building, testing, and deployment

<b>28th-April-2023</b>    
Updated workflow so that image is only pushed to Docker if test suite passes with 75%+ code coverage

<b>29th-April-2023</b>    
Final functionality and testing is implemented

<b>1st-May-2023</b>    
Dockerfile and README is updated for instructions on how to run the project using Docker

# Thank you for stopping by!
