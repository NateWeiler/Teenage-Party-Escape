# Teenage Party Escape

https://github.com/NateWeiler/Teenage_Party_Escape


Lab: Flask Adventure Game
In this lab, you'll convert your OOP text-based adventure game into a web application. The goal will be to practice working with Flask to create a server capable of handling requests and building responses. You will also work on your Test-Driven Development process.

The initial setup will require you to sign up for a free Heroku account. Heroku is a Platform as a Service (PaaS) meaning it's a web service that helps you manage servers that can run your applications built in Python and other languages.

If you need help writing your own tests, please review the Automated Testing lab from a few weeks before. Also, re-read the Flask Tutorial page on Test Coverage to review using pytest and coverage for a Flask application. Finally, you should keep Pytest's documentation open as a reference.

Setup
Copy the python-skeleton project and set up your game's project structure. If you don't remember, follow the instructions in the README.
Create your virtual environment, activate it, and install flask and pytest.
Once you have a basic Hello World app running and tested, you should commit and push to GitHub.
Then you can follow this tutorial to deploy this to Heroku.
Make sure that the project setup for a simple app is working before you start developing your game! Adding more code on to a broken setup is going to make debugging it that much harder. If you see the app running on a Heroku URL and can make quick changes to it, then you are good to go!

Requirements
UI built with HTML/CSS served dynamically via Flask
Fully tested by Pytest
Followed a feature branch git workflow
Deployed automatically to Heroku on updates to master branch
Optional, but recommended:

Validated and sanitized user input
Created user stories to plan the project
Employed OOP classes for the game engine and scenes
Organized classes in separate Python modules using Flask Blueprints
Stored data in cookies and/or Postgres database to store user progress, save states, or preferences