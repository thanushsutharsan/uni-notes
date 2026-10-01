# UniNotes - A Simplfied Notes App (FULL-STACK)

## Description

UniNotes is a full-stack Django web application designed for university students who want a simple and organised way to access revision resources and manage their own study notes.

The application combines a study-note marketplace with a personal revision area. Students can register for an account, browse available study notes, search for resources, filter notes by subject, view individual note details and purchase resources through Stripe Checkout. Once a payment has been successfully confirmed, the purchased resource is added to the student's account and can be accessed through their personal purchase library.

Registered users can also create and manage their own private revision notes. These notes can be created, viewed, edited and deleted by their owner, providing full CRUD functionality while ensuring that users cannot access or modify another student's private revision content.

UniNotes uses Django, Python, HTML, CSS and JavaScript together with a relational database, Django authentication and Stripe payment processing to provide a complete full-stack application.