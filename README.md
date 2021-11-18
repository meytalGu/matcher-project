# matcher-project

This repository contains a basic django matcher app.  
We’ll assume you have Django 3.2 installed already + Python 3.6 and later.
____

## Quickstart


Matcher is a simple Django app to conducts web-base job matcher for candidates.  
From the command line, cd into maysite.py then run the following commands:

1. Run `python manage.py migrate` to create the matcher models.

2. Run `python manage.py runserver` to start the development server.

3. Visit http://127.0.0.1:8000/admin/ to create and update matcher objects (Skills, Jobs and Candidates).  
      `Username: testUser  Password: thisistest1` 

## Start playing


Given skill id, retrieves the skill info:  
`http://127.0.0.1:8000/matcher/<skillId>/skill/`

Given job id, retrieves the job info:  
`http://127.0.0.1:8000/matcher/<jobId>/job/`

Given candidate id, retrieves the candidate info:  
`http://127.0.0.1:8000/matcher/<candidateId>/candidate/`

Given candidate id, retrieves all candidate's skills:  
`http://127.0.0.1:8000/matcher/<candidateId>/candidateSkills/`


#### Cadidate Finder
Given a job id, retrieves the best 5 candidates which match the job (match title and match skill first):
`http://127.0.0.1:8000/matcher/<jobId>/candidateFinder/`

## Running Tests
All matcher tests are in /mysite/matcher/tests.py .  
From the command line, cd into maysite.py then run `python manage.py test matcher` in order to run the tests. 

