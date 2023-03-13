# STDA (simple to do application)


A simple note taking application made using `django`, `bootstrap`, and `sqlite`.

# Features
This application contains features related to creating and deleting notes. It maintains a simple    `authentication` system to `authenticate` user.

# Demo

To get a demo of it's woking check this [demo website] (https://simpletodo.pythonanywhere.com)

![alt text](https://github.com/deepakdubey8756/simple-to-do/blob/main/asset/todo.png)

# Design
This document provides a high-level overview of the note taking application. The application will allow users to `create`, `edit`, and `delete notes`.

## User Stories:
The following user stories will be implemented in the application:

As a user I want to be able to 
1. create a new note.
2. view all my notes.
3. edit a note.
4. delete a note.

## Models:
The following models will be created in the application:

### Note: 
The main model that will store information about a note, including the `title and content of the note.

## Views:
The following views will be created to handle the user stories:
### Create Note: 
A view that will allow users to create a new note.
### View Notes:
 A view that will display a list of all the notes created by the user.
### Edit Note: 
A view that will allow users to edit an existing note.
### Delete Note: 
A view that will allow users to delete a note.
## Templates:
The following templates will be created for each view:
### index.html:
 A template for the Create Note view.
view_notes.html: A template for the View Notes view.

## URLs:
The following URLs will be defined for each view:

### /
 The URL for the index page to display Notes.


### /edit/<note_id>
The URL for the Edit Note view, where <note_id> is the ID of the note to be edited.

### deleteNote/<id>
 The URL for the Delete Note view, where <id> is the ID of the note to be deleted.


### accounts/signup
This url will signup user

### accounts/login
This url will login user

### accounts/logout
to logout user

## Conclusion:
This design document outlines the basic structure of the note taking application that i have developed using Django. The application will allow users to create, view, edit, and delete notes. The models, views, templates, and URLs have been defined to provide a clear understanding of the functionalities that will be implemented in the application.
