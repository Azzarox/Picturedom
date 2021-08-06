## Project Overview:
The project is named **Picturedom** and the idea is to create something resembling **Instagram** or **Pinterest**. Mainly photo-oriented website.

## Main functionality:
#### Images:
- can be liked and disliked
- can be viewed
- can be posted
- can be commented on

#### Comments:
- can be liked and disliked
- can be edited
- can be deleted

#### Profile
- can edit information about first and last names, age and email also add profile image

## Data Validations
#### Images
- can't post file bigger than or equal to 8MB
#### Comments
- can't add swearing words such as suck, fuck etc.
- can't like or dislike when already liked or disliked already 
#### Profile
- can't have numbers or spaces in the first or last name of the user
- can't have email ending with anything else except .bg .org .com .net .edu
- can't have age bigger than or equal to 100
- can't have profile image file size bigger than or equal to 1MB
#### Others
- All forms have bot catching field and validator checking if the field is empty or not

## URL paths:
### Disclaimer
Everywhere where the url has number 1, it means it is used <int:pk>

### Public
- [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- [http://127.0.0.1:8000/photo/1](http://127.0.0.1:8000/photo/1) 
- [http://127.0.0.1:8000/photo/categories/1](http://127.0.0.1:8000/photo/categories/1) 
- [http://127.0.0.1:8000/register](http://127.0.0.1:8000/register)
- [http://127.0.0.1:8000/login](http://127.0.0.1:8000/login)
- [http://127.0.0.1:8000/logout](http://127.0.0.1:8000/logout)
### Private
- [http://127.0.0.1:8000/photo/create](http://127.0.0.1:8000/photo/create)
- [http://127.0.0.1:8000/photo/comments/1](http://127.0.0.1:8000/photo/create)
- [http://127.0.0.1:8000/photo/comments/edit/1](http://127.0.0.1:8000/photo/comments/edit/1)
- [http://127.0.0.1:8000/photo/comments/delete/1](http://127.0.0.1:8000/photo/comments/delete/1)
- [http://127.0.0.1:8000/photo/comments/like/1](http://127.0.0.1:8000/photo/comments/like/1)
- [http://127.0.0.1:8000/photo/comments/dislike/1](http://127.0.0.1:8000/photo/comments/dislike/1)
- [http://127.0.0.1:8000/user/photos](http://127.0.0.1:8000/user/photos)
- [http://127.0.0.1:8000/user/profile](http://127.0.0.1:8000/user/profile)
### Others
- [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

##### Handling custom error templates when debug is set to False
- [http://127.0.0.1:8000/400/](http://127.0.0.1:8000/400/)
- [http://127.0.0.1:8000/403/](http://127.0.0.1:8000/403/)
- [http://127.0.0.1:8000/404/](http://127.0.0.1:8000/404/)
- [http://127.0.0.1:8000/500/](http://127.0.0.1:8000/500/)

