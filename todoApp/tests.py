from django.test import TestCase
from django.contrib.auth.models import User 
from .models import Notes
from datetime import datetime

class ModelTest(TestCase):

    def setup(self):
        print("Testing model")


    def assertUser(self, user, username, email, password):
        self.assertEqual(user.username, username)
        self.assertEqual(user.email, email)
        self.assertNotEqual(user.password, password)

    
    def assertNote(self, note, title, description):
        self.assertEqual(note.title, title)
        self.assertEqual(note.description, description)
        self.assertEqual(note.isCompleted, False)


    def assertDate(self, old_date, new_date):
        self.assertEqual(old_date, new_date)


    def test_new_note(self):
        username = "deepak"
        email = "dubeydeepak@gmail.com"
        password = "thisIsMyPassWord"

        print("testing user.....")
        user = User.objects.create_user(username, email, password)
        self.assertUser(user, username, email, password)
        initial_notes = Notes.objects.filter(author=user)

        print("testing total notes before creating new note...")
        self.assertEqual(len(initial_notes), 0)

        note_title = "this is my testing title"
        note_description = "this is my testing description"

        note = Notes.objects.create(author = user, title = note_title, description=note_description)
        note.save()
        
        now = datetime.now()

        note_creation_time = [
            note.date_modified.year,
            note.date_modified.month,
            note.date_modified.day,
            note.date_modified.hour,
            ]
        current_time = [now.year,
                        now.month,
                        now.day,
                        now.hour, 
                        ]
        
        print("testing new notes...")
        self.assertNote(note, note_title, note_description)
        self.assertDate(note_creation_time, current_time)


        print("Checking total notes after creating new note")
        final_notes = Notes.objects.filter(author = user)
        self.assertEqual(len(final_notes), 1)

    