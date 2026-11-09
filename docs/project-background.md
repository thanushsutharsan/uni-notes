# Project background

[Back to UniNotes README](../README.md#documentation)

## Contents

- [Description](#description)
- [Purpose](#purpose)
- [Project Rationale](#project-rationale)
  - [Problem Being Solved](#problem-being-solved)
  - [Why This Project Was Chosen](#why-this-project-was-chosen)
  - [Value to Users](#value-to-users)
  - [Real-World Application](#real-world-application)
- [Technologies Used](#jump-technologies-used)

---

## Description

UniNotes is a full-stack Django web application designed for university students who want a simple and organised way to access revision resources and manage their own study notes.

The application combines a study-note marketplace with a personal revision area. Students can register for an account, browse available study notes, search for resources, filter notes by subject, view individual note details and purchase resources through Stripe Checkout. Once a payment has been successfully confirmed, the purchased resource is added to the student's account and can be accessed through their personal purchase library.

Registered users can also create and manage their own private revision notes. These notes can be created, viewed, edited and deleted by their owner, providing full CRUD functionality while ensuring that users cannot access or modify another student's private revision content.

UniNotes uses Django, Python, HTML, CSS and JavaScript together with a relational database, Django authentication and Stripe payment processing to provide a complete full-stack application.

## Purpose

The purpose of **UniNotes** is to provide university students with a simple and organised platform for accessing revision resources and managing their own study material. The application brings together two main areas of revision in one place: students can browse and purchase prepared study notes, while also creating and managing their own private revision notes through their account.

Users can search the available study-note library using keywords or filter resources by subject, allowing them to find relevant material more efficiently. Each study note has its own page containing information such as the subject, title, description and price. Registered users can purchase notes through Stripe Checkout, and completed purchases are stored within their account so that the resources can be accessed and downloaded again from the **My Purchases** section.

UniNotes also provides a personal revision area. Logged-in users can create revision notes containing a title, subject and written content, with the option to upload a supporting file. These notes can later be viewed, edited or deleted. This gives students a private space to organise their own revision alongside the resources they have purchased.

Overall, the purpose of the project is to create a useful study platform that makes revision resources easier to find, access and organise.

## Project Rationale

### Problem Being Solved

University students often use several different methods to organise their revision. Study resources may be downloaded from different websites, saved in different folders or stored separately from a student's own notes. This can make revision less organised and can make it more difficult to quickly locate the material needed for a particular subject.

Another problem is finding relevant revision resources efficiently. When a large amount of material is available, students need a clear way of locating notes that relate to the subject or topic they are studying.

UniNotes addresses these problems by providing a centralised study platform. Available study notes are organised by subject and can be searched using keywords. Students can therefore narrow down the available resources instead of manually looking through unrelated material.

The application also links purchased resources to the user's account. Once a purchase has been successfully confirmed, the purchased note appears within the user's personal purchases area and can be downloaded from there. This provides a clearer way of keeping track of resources that the student has already obtained.

In addition, UniNotes allows students to create and maintain their own revision notes. Each user's revision notes are associated with their own account, meaning they have a personal study area where they can create, view, update and delete their material.


### Why This Project Was Chosen

This project was chosen because revision and organisation are common requirements for university students and therefore provide an appropriate real-world problem for a web application to solve.

A study platform also provides the opportunity to develop functionality that goes beyond displaying static information. UniNotes requires users to interact with stored data in several different ways, including registering and logging into an account, searching and filtering study notes, purchasing resources, downloading previously purchased material and managing personal revision notes.

The project was also chosen because it allows several realistic web-development concepts to be combined within one application. For example, the application manages relationships between users, study notes, subjects, purchases and personal revision notes. User authentication is important because purchases and private revision material must remain linked to the correct account.

The revision-note feature also provides meaningful CRUD functionality. Users can **Create** a revision note, **Read** their saved notes, **Update** existing notes and **Delete** notes they no longer require. This functionality has a genuine purpose within the application rather than being included only as a technical demonstration.

The purchasing system adds another realistic element to the project. Stripe Checkout is integrated into the application so that a payment can be processed and verified before a purchase is recorded. This makes the project more representative of the type of functionality that could be required within a real commercial web application.


### Value to Users

UniNotes provides value to users by making revision material easier to access and organise.

Students are able to browse the available study-note library and use keyword searching and subject filtering to reduce the number of irrelevant results. This improves usability because users do not need to manually search through every resource available on the website.

Creating an account provides further value because the application can provide personalised functionality. Purchased resources are connected to the authenticated user and displayed in the **My Purchases** section, giving the student a permanent record of the resources they have obtained and a convenient location from which to download them again.

The personal revision-note functionality provides an additional reason for students to use the application regularly. Rather than only using UniNotes when purchasing a resource, students can use their account as a study space. They can write their own revision content, categorise it by subject and optionally add an attachment. Existing notes can then be edited as their knowledge develops or deleted when they are no longer required.

The application therefore provides value through:

- Organised access to university study resources
- Keyword searching and subject filtering
- Individual pages containing information about each study note
- User accounts that retain purchase information
- Access to previously purchased notes from one location
- Secure payment processing through Stripe Checkout
- A private revision area for creating and managing personal notes
- Optional file attachments for personal revision material

These features work together to create a platform focused on making the student's revision process more organised and convenient.


### Real-World Application

UniNotes has a clear real-world application as an online platform for distributing digital educational resources. The overall concept is similar to existing digital marketplaces where users create accounts, search for products, complete online payments and retain access to purchased digital content.

In a real deployment, educational resources could be organised across different university subjects, allowing students to search for material that is relevant to their studies. New resources could be added to the platform over time, while the subject-based structure would allow the library to expand without changing the main way users navigate the website.

The purchase process also reflects a realistic digital-commerce workflow. A user selects a study note, completes payment through Stripe Checkout and, once the payment has been verified, a purchase record is associated with their account. The user can then access the purchased resource through their personal library.

The application also prevents the normal purchase flow from unnecessarily selling the same study note to the same user again once ownership has already been recorded.

The personal revision system extends the project beyond being only a digital shop. Students can use UniNotes as an ongoing revision tool by storing and updating their own notes alongside purchased resources.

Ownership checks are used when accessing, editing or deleting these revision notes so that one user cannot simply access another user's private notes through the normal application routes.

The project therefore demonstrates how a database-driven Django application can be applied to a genuine educational use case. It combines user authentication, database relationships, searching and filtering, CRUD functionality, file handling, payment processing and personalised content to produce an application that could be developed further into a larger university revision service.



<a name="jump-technologies-used"></a>

## Technologies Used

| Category | Technology | Purpose |
|---|---|---|
| Language | **Python 3.13.7** | Used as the main back-end programming language. Python handles the application logic, Django models, views, forms, validation, authentication, database queries, CRUD functionality and payment processing. |
| Language | **HTML5** | Used to structure the content of the website, including navigation, forms, study-note information, revision pages and authentication pages. Django template syntax is used alongside HTML to display dynamic database content. |
| Language | **CSS3** | Used to style the application and create the visual layout. Custom CSS controls typography, buttons, forms, study-note cards, navigation, spacing and responsive behaviour across different screen sizes. |
| Language | **JavaScript** | Used to add client-side interaction, mainly for the responsive navigation menu. It controls opening and closing the menu and updates accessibility attributes such as `aria-expanded`. |
| Framework | **Django 5.2.17** | The main web framework used to build UniNotes. Django manages models, views, templates, URLs, forms, authentication, sessions, database interaction, file uploads, security and automated testing. |
| Library | **Stripe Python Library 12.5.1** | Allows the Django application to communicate with Stripe. It is used to create Checkout Sessions, retrieve completed sessions and verify payment information before a purchase is recorded. |
| Library | **dj-database-url 2.3.0** | Converts the `DATABASE_URL` environment variable into a database configuration Django can use. This allows different database configurations to be used in development and production. |
| Library | **Psycopg 3.2.9** | Provides PostgreSQL connectivity so the Django application can communicate with a PostgreSQL database when one is configured. |
| Library | **WhiteNoise 6.9.0** | Used to serve static files such as CSS, JavaScript and images efficiently when the application is deployed. |
| Library | **python-dotenv 1.1.1** | Used to load local environment variables from an `.env` file. This allows sensitive configuration such as secret keys, Stripe keys and database details to remain outside the main source code. |
| Library | **Gunicorn 23.0.0** | Used as the production WSGI server for the deployed Django application. The project is configured to run using `gunicorn uninotes.wsgi`. |
| API | **Stripe API** | Connects UniNotes to Stripe Checkout. It allows the application to create payment sessions and verify successful payments without directly processing users' card information within UniNotes. |
| Database | **SQLite** | Used as the default local development database. It allows the project to be developed and tested without requiring a separate database server. |
| Database | **PostgreSQL Support** | The application can use PostgreSQL when a valid `DATABASE_URL` is supplied. This provides a database option suitable for production deployment. |
| Database Technology | **Django ORM** | Allows the application to interact with database records using Python objects rather than manually writing SQL queries. It is used to manage users, subjects, study notes, purchases and revision notes. |
| Payment Technology | **Stripe Checkout** | Provides the hosted payment system used when a registered user purchases a study note. UniNotes creates the Checkout Session and verifies the result before recording the purchase. Stripe test mode is used during development and assessment. |
| Development Tool | **Visual Studio Code** | Used to create and edit the Python, HTML, CSS, JavaScript, Markdown and configuration files within the project. |
| Development Tool | **Git** | Used for version control, allowing project changes to be recorded through commits and providing a development history. |
| Development Tool | **GitHub** | Used as the remote repository for storing the project source code and Git commit history. |
| Development Tool | **Django Development Server** | Used to run and test the application locally during development using `python manage.py runserver`. |
| Development Tool | **Django Test Framework** | Used to run automated tests with `python manage.py test`, helping verify that application functionality behaves as expected. |
| Development Tool | **Django Migrations** | Used to keep the database structure synchronised with changes made to the Django models using commands such as `python manage.py migrate`. |
| Deployment Tool | **Heroku** | The deployment platform prepared for the project. Production configuration can be supplied using environment variables such as `DATABASE_URL` and `ALLOWED_HOSTS`. |
