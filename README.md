# Video Games Reviews Website

###### Contributors:
[Tyler Goldsmith](https://github.com/TylerGoldsmith/milestone-3)

###### Functionality:
- Log in
    - Using username and encrypted password
    - Using encryoted email and encrypted password
- Creating an account
- Logging out
- Email Activation
- Searching Video Games by:
    - Ratings
    - Genre
    - Name
    - Platform
    - Publisher
- Posting reviews and ratings
- Viewing details of a game:
    - Ratings
    - Genre
    - Name
    - Platforms
    - Publisher
    - Game Description
    - Reviews

The project I am attempting to create is a video game review site in which you can sift through different games to see what you would enjoy to play. Splitting games into categories such as genre, highest rated, newest release will help pinpoint games a user may want to play. This will also remove games they would not be interested in so they waste less time looking at games they do not want to play.

###### Languages used
Front End:

    - React(JS)

    - SASS(CSS)

Back End:

    -Django(Python)

## Installing
### Clone the project
```
git clone https://github.com/TylerGoldsmith/milestone-3
cd milestone-3
```
### Actuvate Virtual Environment
```
Start at the top level
python3 -m venv venv
source venv/Scripts/activate
```
### Install Dependencies in Back End
``` 
Start at top level
cd backend
python -m pip install Django
pip install django-cors-headers
pip install django-cryptography
```

### Run the migrations in Back End
```
Start at top level
cd backend
python manage.py migrate
```

### Create migrations in Back End
```
Start at top level
cd backend
python manage.py migrations
```

### Run server
```
Start at top level
python manage.py runserver
```

### Install Dependencies in Front End
```
cd frontend
npm i create-react-app
npm i sass
```

### Run programs
```
sass --watch src/assets/scss/style.scss:src/assets/css/style.css
npx serve .
```

### Data Structure
![Data Structure Image](/frontend/src/assets/images/readme/vg_reviews_datastructure.jpg)

###### Technical Sources:
[Django-rest-framework](https://www.django-rest-framework.org/tutorial/1-serialization/)

[Digital Ocean](https://www.digitalocean.com/community/tutorials/build-a-to-do-application-using-django-and-react)

###### Asset Sources:
Empty