# STDA (simple to do application)


A simple note taking application makde using django, bootstrap, and sqlite.

# Features
This application contains features related to creating and deleting notes. It maintains a simple authentication system to authenticate user.

# Demo

To get a demo of it's woking check this  link...


# Design
This document provides a high-level overview of the note taking application. The application will allow users to create, edit, and delete notes.

## User Stories:
The following user stories will be implemented in the application:

As a user, I want to be able to create a new note.
As a user, I want to be able to view all my notes.
As a user, I want to be able to edit a note.
As a user, I want to be able to delete a note.

## Models:
The following models will be created in the application:
### Note: 
The main model that will store information about a note, including the title and content of the note.
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

## Conclusion:
This design document outlines the basic structure of the note taking application that i have developed using Django. The application will allow users to create, view, edit, and delete notes. The models, views, templates, and URLs have been defined to provide a clear understanding of the functionalities that will be implemented in the application.
