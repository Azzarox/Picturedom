# Picturedom

-   [https://picturedom.herokuapp.com/](https://picturedom.herokuapp.com/)

## Docker Containers

### IMPORTANT:

I have changed the DATABASES constant in [settings.py](./Picturedom/Picturedom/settings.py) to use `HOST:"postgres"` in order to work with the docker-compose.yml.

There is a docker-compose.yml file which creates container of the app with postgresql.

To create the containers - `docker compose up` (Should be ran from the same directory where the docker-compose.yml file is located)

There are volumes for the /media folder so if any pictures are uploaded it should persist, as well as the database is made to persist.

If the container is ran for first time you would need to run:

-   `python manage.py makemigrates`
    and after that
-   `python manage.py migrate`.

You need to create superuser with `python manage.py createsuperuser` in order to create Category after going to `http://localhost:8000/admin`. Otherwise you won't be able to add photos.

To run the commands above you need to run the container and attach to it by using `docker exec -it <container_id> bash`.

### Django App Container

You can only create the Django App container using: `docker build -t <your_desired_name_of_image> .` - You should be inside the folder where is the Dockerfile to run this command.

To run the container use `docker run -it -p 8000:8000 <your_desired_name_of_image>`

## Project Overview

The project website is named **Picturedom** and the idea is to create something resembling **Instagram** or **Pinterest**. Mainly photo-oriented website.

## Main functionality

#### Images

-   can be liked and disliked
-   can be viewed
-   can be posted
-   can be commented on

#### Comments

-   can be liked and disliked
-   can be edited
-   can be deleted

#### Profile

-   can edit information about first and last names, age and email also add profile image

## Data Validations

#### Images

-   can't post file bigger than or equal to 8MB

#### Comments

-   can't add swearing words such as suck, fuck etc.
-   can't like or dislike when already liked or disliked already

#### Profile

-   can't have numbers or spaces in the first or last name of the user
-   can't have email ending with anything else except .bg .org .com .net .edu
-   can't have age bigger than or equal to 100
-   can't have profile image file size bigger than or equal to 1MB

#### Others

-   All forms have bot catching field and validator checking if the field is empty or not

## URL paths

### Disclaimer

Everywhere where the url has number 1, it means it is used <int:pk>

### Public

-   [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
-   [http://127.0.0.1:8000/photo/1](http://127.0.0.1:8000/photo/1)
-   [http://127.0.0.1:8000/photo/categories/1](http://127.0.0.1:8000/photo/categories/1)
-   [http://127.0.0.1:8000/register](http://127.0.0.1:8000/register)
-   [http://127.0.0.1:8000/login](http://127.0.0.1:8000/login)
-   [http://127.0.0.1:8000/logout](http://127.0.0.1:8000/logout)

### Private

-   [http://127.0.0.1:8000/photo/create](http://127.0.0.1:8000/photo/create)
-   [http://127.0.0.1:8000/photo/like/1](http://127.0.0.1:8000/photo/like/1)
-   [http://127.0.0.1:8000/photo/comments/1](http://127.0.0.1:8000/photo/create)
-   [http://127.0.0.1:8000/photo/comments/edit/1](http://127.0.0.1:8000/photo/comments/edit/1)
-   [http://127.0.0.1:8000/photo/comments/delete/1](http://127.0.0.1:8000/photo/comments/delete/1)
-   [http://127.0.0.1:8000/photo/comments/like/1](http://127.0.0.1:8000/photo/comments/like/1)
-   [http://127.0.0.1:8000/photo/comments/dislike/1](http://127.0.0.1:8000/photo/comments/dislike/1)
-   [http://127.0.0.1:8000/user/photos](http://127.0.0.1:8000/user/photos)
-   [http://127.0.0.1:8000/user/profile](http://127.0.0.1:8000/user/profile)

### Admin

-   [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

### Others

##### Handling custom error templates when debug is set to False

-   [http://127.0.0.1:8000/400/](http://127.0.0.1:8000/400/)
-   [http://127.0.0.1:8000/403/](http://127.0.0.1:8000/403/)
-   [http://127.0.0.1:8000/404/](http://127.0.0.1:8000/404/)
-   [http://127.0.0.1:8000/500/](http://127.0.0.1:8000/500/)

## Dependencies

-   django-crispy-forms
-   django-cleanup
-   psycopg2-binary
-   coverage
-   Pillow

### Note to self:

-   The project starts from the second 'Picturedom' folder (not where .gitignore is)
-   Run postgresql to load database service
-   This could be done many ways but the easiest (for Windows) is from Services, find postgresql and right click and 'start'
