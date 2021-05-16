# Backend_Role_Assignment
# Problem Statement:
An API to fetch latest videos from youtube sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.
## How to run the project
- Clone the project by using `git clone https://github.com/sangeetarao/Backend_Role_Assignment.git`
- Make sure you have python installed
- Get Google API Key and add it to settings.py file under YOUTUBE_API_KEYS.
- Redirect to the fampay folder
- Run requirements.txt file `pip install -r requirements.txt`
- Run server by running the following commands on the terminal:
- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py runserver` 
- Go to the mentioned url on the terminal to access the project 

## How to run project on docker:
- Install docker
- On terminal `docker-compose build` . This will install all requirements 
- On terminal `docker-compose up` . This will bring up the server. 
- Go to local host to access the project.


