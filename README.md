# UniNotes - A Simplfied Notes App (FULL-STACK)

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


# User Experience Design (UX)

The User Experience (UX) of **UniNotes** has been designed around making university revision resources easy to find, purchase, access and organise. The application aims to reduce unnecessary steps for users and provide a clear journey from first visiting the website to accessing purchased study materials or managing personal revision notes.

The design focuses on simple navigation, clear page layouts, accessible forms, responsive behaviour and personalised functionality for registered users. Important actions such as browsing notes, searching for resources, registering, logging in, accessing purchases and creating revision notes are available through clearly identified areas of the website.

The UX has also been designed around different user states. Visitors who are not logged in can still browse available study notes and explore subjects, while registered users gain access to personalised features including **Revision** and **My Purchases**. This allows users to understand the value of the website before creating an account while protecting account-specific content.


## UX Goals

The main UX goal of UniNotes is to create a clear and efficient revision platform that university students can use without needing extensive instructions.

The key UX goals are:

- **Simple navigation** – users should be able to move between the Home, Browse, Revision and My Purchases areas without becoming confused about where features are located.
- **Efficient resource discovery** – users should be able to search for study notes using keywords and filter available resources by subject rather than manually looking through every note.
- **Clear information hierarchy** – headings, sections, cards and page titles are used to make content easier to scan and understand.
- **Minimal steps to important actions** – important functions such as searching, viewing a note, purchasing a note and accessing purchased resources should require as few unnecessary steps as possible.
- **Personalised user experience** – authenticated users should have clear access to their own purchases and private revision notes.
- **Consistent interface design** – buttons, forms, navigation elements and content cards should behave and appear consistently throughout the application.
- **Responsive usability** – the website should remain usable across different screen sizes, with navigation that can adapt to smaller displays.
- **Accessible interaction** – form fields use labels, images include alternative text where appropriate and the website provides features such as a skip-to-content link and accessible navigation labels.
- **Clear user feedback** – users should receive confirmation when important actions such as creating an account, saving a revision note, updating a note or deleting a note have been completed.
- **Useful empty states** – when no content matches a search or no content is available, the interface should explain this clearly rather than leaving the user with an unexplained blank area.

These goals support the overall purpose of UniNotes by reducing friction and allowing students to spend more time using revision resources rather than learning how to use the website.


## Target Audience

The target audience was considered when deciding which features should be prioritised within UniNotes. The application is primarily aimed at university students who need a convenient way to locate revision material and organise their studies.

The design therefore focuses on speed, simplicity and organisation rather than providing unnecessary features that could make the application more complicated.


### Primary Users

The primary users of UniNotes are **university students looking for revision and study resources**.

These users may:

- Be studying one or more university subjects
- Need additional resources to support their revision
- Want to search for notes relating to a particular subject or topic
- Prefer having digital study resources available through one account
- Want to keep track of study materials they have already purchased
- Create their own revision notes while studying
- Update revision material as their understanding develops
- Upload supporting files alongside their personal revision notes
- Access study resources from different devices

For these users, the most important parts of the user experience are being able to quickly locate relevant material, understand what a study note contains and access purchased resources without unnecessary difficulty.

The keyword search and subject filter support this audience by reducing the amount of irrelevant content users need to look through. The **My Purchases** area gives returning users a clear location for accessing resources they have already obtained.

The private revision-note functionality also supports students who want to use UniNotes as more than a marketplace. They can create, view, update and delete their own revision notes, giving them a personalised study area within the same application.


### Secondary Users

The secondary users are **students who are exploring the platform before deciding whether to register or purchase a resource**.

These users may arrive at UniNotes looking for a particular study subject without already having an account.

For this reason, important parts of the website such as the homepage, subject selection, study-note library, search functionality and individual study-note information can be explored before the user accesses account-specific functionality.

This allows potential users to understand what UniNotes offers before being required to create an account.

Unauthenticated users are also clearly shown that the Revision area is available to registered users. This provides information about additional functionality without allowing private account features to be accessed by users who are not logged in.

The experience is therefore designed to provide useful information to new visitors while giving registered users additional personalised functionality.


## User Needs

The needs of the target users influenced the functionality and structure of UniNotes.

A major user need is the ability to **find relevant study resources quickly**. University students may be looking for material relating to a specific course or topic and should not need to search manually through unrelated notes. UniNotes addresses this by providing keyword searching and subject-based filtering.

Users also need enough information to decide whether a resource is relevant before purchasing it. Individual study-note pages therefore provide information about the selected resource, including its title, subject, description and price.

Registered users need a reliable way to keep track of resources they have already purchased. The **My Purchases** section provides a personalised area where previous purchases are displayed and purchased resources can be accessed again.

Another important user need is organisation. Students often create their own revision material in addition to using external resources. UniNotes therefore allows authenticated users to maintain their own private revision notes. Users can:

- Create new revision notes
- View their saved revision notes
- Edit existing revision notes
- Delete revision notes they no longer require
- Organise notes using a subject
- Add written revision content
- Optionally attach supporting files

Privacy is also an important user need. Personal revision notes are associated with the account that created them. When revision notes are viewed, edited or deleted, the application checks that the authenticated user owns the requested note.

Users also need reassurance that their actions have been completed successfully. UniNotes provides feedback messages following important actions such as registration and revision-note management.

Overall, the main user needs identified for the project are:

- Quick access to relevant revision resources
- Clear navigation
- Search and filtering functionality
- Clear information before making a purchase
- Secure online payment
- Access to previously purchased resources
- A personalised revision area
- Control over personal revision content
- Clear feedback after completing actions
- An interface that remains usable on different screen sizes
- Accessible and understandable forms and navigation


## Business Goals

Although UniNotes is primarily designed around the needs of students, the application also has business goals that support its potential use as a real digital study-resource platform.

One business goal is to provide a structured way of **selling digital study resources online**. Study notes include pricing information and can be purchased using Stripe Checkout. This creates a realistic commercial process where users can discover a resource, view its details, complete a payment and then access the purchased material through their account.

Another goal is to encourage users to create accounts and return to the platform. UniNotes supports this by providing functionality that continues to provide value after the initial purchase. Users can revisit their purchased resources through **My Purchases** and maintain their own revision material through the Revision area.

Providing useful account functionality can encourage repeat use because the platform becomes a place where users can both access external study material and manage their own revision.


The key business goals are:

- Provide a platform for distributing paid digital revision resources
- Make it easy for users to discover relevant resources
- Reduce barriers between discovering a note and purchasing it
- Provide secure payment processing through Stripe Checkout
- Encourage account registration by providing personalised functionality
- Encourage users to return through persistent access to previous purchases
- Increase the usefulness of the platform through personal revision-note functionality
- Build user trust through clear navigation, secure account-based access and predictable interactions
- Maintain an organised structure that can support additional subjects and study resources
- Create a foundation that could be developed into a larger educational resource platform

The business goals and user needs work together rather than being treated separately. For example, effective searching benefits students by helping them locate relevant material while also supporting the business goal of making resources easier to discover. Similarly, the My Purchases area benefits users by keeping their resources organised while encouraging them to return to the platform.

This balance between **user requirements and business objectives** is an important part of the UX strategy for UniNotes and ensures that features have a clear purpose within the overall application.


## User Stories

The user stories for UniNotes were created based on the needs of the two target audiences identified during the UX planning process.

The **primary users** are university students who actively use UniNotes to find revision resources, purchase study notes and manage their own revision material.

The **secondary users** are students who are exploring the platform before deciding whether to register or purchase a study resource.

Creating user stories for both audiences helped ensure that the application considers the experience of new visitors as well as students who regularly use the personalised features of the platform.


### First-Time Visitor Goals

#### User Story 1 – Primary User

**As a university student looking for revision resources, I want to browse the available study notes so that I can see whether UniNotes contains material that is relevant to my studies.**

This user story relates to the **primary target audience** because university students need a quick way to identify resources that could support their revision.

The Browse area allows users to view the available study notes without needing to search through unrelated areas of the website.


#### User Story 2 – Secondary User

**As a student visiting UniNotes for the first time, I want to explore the available subjects and study notes before creating an account so that I can decide whether the platform is useful to me.**

This user story relates to the **secondary target audience** because these users may not yet be ready to register or make a purchase.

Allowing visitors to explore the available resources first reduces unnecessary barriers and helps them understand what the application provides.


#### User Story 3 – Primary User

**As a university student looking for a specific revision topic, I want to search for study notes using keywords so that I can find relevant resources quickly.**

This relates to the **primary target audience** because students may already know the particular subject or topic they need help with.

The search functionality reduces the amount of unrelated content users need to manually browse.


#### User Story 4 – Secondary User

**As a student exploring the platform, I want to filter study notes by subject so that I can quickly see whether resources are available for an area I am studying.**

This relates to the **secondary target audience** because a potential user may want to investigate the available content before deciding whether to use the platform regularly.

Subject filtering provides a simple way of narrowing the available resources.


#### User Story 5 – Primary User

**As a university student, I want to view detailed information about a study note so that I can understand what the resource contains before deciding whether to purchase it.**

This relates to the **primary target audience** because students need enough information to make an informed decision before purchasing a digital resource.


#### User Story 6 – Secondary User

**As a first-time visitor, I want the website navigation to be clear and understandable so that I can easily discover the main areas of the application without needing instructions.**

This relates to the **secondary target audience** because new visitors will not already know how UniNotes is structured.

Clear navigation helps these users move between areas such as the homepage and study-note library without becoming confused.


### Registered User Goals

#### User Story 7 – Primary User

**As a registered university student, I want to purchase a study note securely so that I can access revision material that supports my studies.**

This directly relates to the **primary target audience** because purchasing revision resources is one of the main functions provided by UniNotes.

Stripe Checkout provides the payment process while the application records the completed purchase against the user's account.


#### User Story 8 – Secondary User

**As a student who has explored UniNotes and decided that it is useful, I want to register for an account so that I can access the personalised features of the website.**

This represents the transition of a **secondary user** from exploring the application to becoming a registered user.

Registration allows the student to move beyond browsing resources and access functionality such as purchases and private revision notes.


#### User Story 9 – Primary User

**As a registered student, I want to create my own revision notes so that I can organise personal study material within UniNotes.**

This relates to the **primary target audience** because students may want to combine purchased revision resources with notes they create themselves.

Users can create revision notes containing information such as a title, subject and written content.


#### User Story 10 – Secondary User

**As a student who has recently registered, I want the personalised areas of the website to be easy to identify so that I can understand the additional features available through my account.**

This relates to users who originally belonged to the **secondary target audience** and have decided to register after exploring the platform.

Areas such as **Revision** and **My Purchases** provide additional functionality once the user has an account.


#### User Story 11 – Primary User

**As a registered student, I want to upload a supporting file to a revision note so that I can keep related revision material together.**

This relates to the **primary target audience** because students may have additional files that support the written revision information stored within their notes.


#### User Story 12 – Primary User

**As a registered student, I want my personal revision notes to remain private so that other users cannot view, edit or delete my study material.**

This relates to the **primary target audience** because users need confidence that personalised content is linked to their own account.

UniNotes uses authentication and ownership checks when users access or modify personal revision notes.


### Returning User Goals

#### User Story 13 – Primary User

**As a returning student, I want to view the study notes I have previously purchased so that I can access my revision resources again without purchasing them a second time.**

This directly relates to the **primary target audience** because students are likely to return to purchased material while revising.

The **My Purchases** section provides a centralised location for previously purchased study notes.


#### User Story 14 – Secondary User

**As a returning visitor who previously explored the platform without registering, I want to search and browse the available resources again so that I can decide whether there is now a resource I want to use.**

This relates to the **secondary target audience** because not every visitor will register during their first visit.

Keeping browsing and searching accessible allows these users to continue evaluating the platform when they return.


#### User Story 15 – Primary User

**As a returning registered student, I want to edit an existing revision note so that I can update my revision material as my knowledge develops.**

This relates to the **primary target audience** because revision material often changes as students continue studying a topic.

The Update functionality allows existing revision notes to be modified rather than requiring the student to create a completely new note.


#### User Story 16 – Primary User

**As a returning registered student, I want to delete revision notes that I no longer need so that my personal revision area remains organised and relevant.**

This relates to the **primary target audience** because students need control over the content stored within their personal revision area.


#### User Story 17 – Secondary User

**As a returning visitor, I want to continue exploring the website using clear and consistent navigation so that I can quickly return to the resources that interest me.**

This relates to the **secondary target audience** because returning visitors who have not yet registered should still be able to use the main browsing functionality without difficulty.


#### User Story 18 – Primary User

**As a returning registered student, I want to access and download a resource I have already purchased so that I can continue using it during future revision sessions.**

This relates to the **primary target audience** because purchased digital resources need to remain useful after the initial transaction.

Providing access through **My Purchases** gives users a consistent location for returning to their purchased study material.


## User Story Acceptance Criteria

Acceptance criteria were created for the user stories to define what must happen for each requirement to be considered successfully implemented.

Using acceptance criteria also provides measurable requirements that can later be compared against the finished application during testing.


### US1 – Browse Study Notes

**User Story:** As a university student looking for revision resources, I want to browse the available study notes so that I can see whether UniNotes contains material relevant to my studies.

**Acceptance Criteria:**

- The user can access the study-note browsing area.
- Available study notes are displayed clearly.
- Each available resource provides enough information for the user to identify the note.
- The user can select a study note to view more information about it.


### US2 – Explore Before Registering

**User Story:** As a student visiting UniNotes for the first time, I want to explore the available subjects and study notes before creating an account.

**Acceptance Criteria:**

- A visitor can access the homepage without logging in.
- A visitor can browse available study resources.
- A visitor can explore available subjects.
- Registration is not required simply to view the available study-note library.


### US3 – Search for Study Notes

**User Story:** As a university student looking for a specific revision topic, I want to search for study notes using keywords.

**Acceptance Criteria:**

- A search input is available within the study-note browsing functionality.
- The user can enter a keyword or search term.
- Relevant study notes are displayed based on the search.
- When no matching resource is available, the user receives an appropriate empty-state message.


### US4 – Filter by Subject

**User Story:** As a student exploring the platform, I want to filter study notes by subject.

**Acceptance Criteria:**

- Available subjects can be selected by the user.
- Selecting a subject reduces the displayed study notes to relevant resources.
- The user can clearly identify which resources belong to the selected subject.
- Filtering should help the user locate relevant material without manually reviewing every note.


### US5 – View Study Note Information

**User Story:** As a university student, I want to view detailed information about a study note before deciding whether to purchase it.

**Acceptance Criteria:**

- The user can select an individual study note.
- The study-note page displays its title.
- The subject of the resource is displayed.
- A description of the resource is available.
- The price is clearly shown before the user begins the purchasing process.


### US6 – Clear Navigation

**User Story:** As a first-time visitor, I want the website navigation to be clear and understandable.

**Acceptance Criteria:**

- The main navigation is clearly visible.
- Navigation labels describe the destination of the link.
- Users can move between the main areas of UniNotes.
- Navigation remains usable across different screen sizes.


### US7 – Purchase a Study Note

**User Story:** As a registered university student, I want to purchase a study note securely.

**Acceptance Criteria:**

- The user must be authenticated before completing account-specific purchasing functionality.
- The selected study note has a clearly displayed price.
- The payment process uses Stripe Checkout.
- A successful purchase is associated with the authenticated user.
- The purchased resource becomes available through the user's purchases.


### US8 – Register for an Account

**User Story:** As a student who has explored UniNotes, I want to register for an account so that I can access personalised features.

**Acceptance Criteria:**

- A registration option is available to unauthenticated users.
- The user can submit the required registration information.
- Valid registration information creates a user account.
- Invalid information should not create an account.
- The user receives appropriate feedback following registration.


### US9 – Create a Revision Note

**User Story:** As a registered student, I want to create my own revision notes.

**Acceptance Criteria:**

- Only authenticated users can access personal revision-note functionality.
- The user can create a new revision note.
- The note can contain a title.
- The note can be associated with a subject.
- The user can add written revision content.
- Successfully saved notes appear within the user's personal revision area.


### US10 – Access Personalised Features

**User Story:** As a student who has recently registered, I want personalised areas of the website to be easy to identify.

**Acceptance Criteria:**

- Authenticated users can access the Revision area.
- Authenticated users can access My Purchases.
- Account-specific areas are clearly labelled.
- Private functionality is not made available to unauthenticated users in the same way as public browsing content.


### US11 – Upload a Supporting File

**User Story:** As a registered student, I want to upload a supporting file to a revision note.

**Acceptance Criteria:**

- The revision-note form provides an option for adding a supporting file.
- The attachment is optional.
- A revision note can still be created without an attachment.
- When a valid attachment is supplied, it is associated with the relevant revision note.


### US12 – Protect Private Revision Notes

**User Story:** As a registered student, I want my personal revision notes to remain private.

**Acceptance Criteria:**

- Revision notes are associated with the user who created them.
- Authentication is required to access private revision-note functionality.
- Users can only edit revision notes that belong to their account.
- Users can only delete revision notes that belong to their account.
- Ownership is checked when accessing account-specific revision-note actions.


### US13 – View Previous Purchases

**User Story:** As a returning student, I want to view the study notes I have previously purchased.

**Acceptance Criteria:**

- Authenticated users can access My Purchases.
- Completed purchases belonging to the user are displayed.
- The purchases shown are associated with the currently authenticated account.
- Previously purchased resources can be accessed from this area.


### US14 – Return and Continue Browsing

**User Story:** As a returning visitor who has not registered, I want to browse and search the available resources again.

**Acceptance Criteria:**

- Returning visitors can access the public study-note library.
- Searching remains available without requiring the visitor to purchase a resource first.
- Subject browsing remains accessible.
- Visitors can continue viewing individual study-note information.


### US15 – Edit a Revision Note

**User Story:** As a returning registered student, I want to edit an existing revision note.

**Acceptance Criteria:**

- The user can select one of their existing revision notes.
- An edit option is available for revision notes owned by the authenticated user.
- Existing information is available to be updated.
- Valid changes can be saved.
- The updated information is displayed after the edit has been completed.
- A user cannot use the normal application routes to edit another user's revision note.


### US16 – Delete a Revision Note

**User Story:** As a returning registered student, I want to delete revision notes I no longer need.

**Acceptance Criteria:**

- A delete option is available for revision notes owned by the authenticated user.
- The selected note can be removed.
- The deleted note no longer appears in the user's revision-note collection.
- A user cannot use the normal application routes to delete another user's revision note.
- The application provides appropriate feedback after deletion.


### US17 – Consistent Experience for Returning Visitors

**User Story:** As a returning visitor, I want clear and consistent navigation so that I can quickly return to resources that interest me.

**Acceptance Criteria:**

- Navigation remains consistent between the main pages.
- Common navigation elements use understandable labels.
- The user can return to the Browse area without unnecessary steps.
- The interface remains usable on different screen sizes.


### US18 – Access a Previously Purchased Resource

**User Story:** As a returning registered student, I want to access and download a resource I have already purchased.

**Acceptance Criteria:**

- The user's completed purchase is visible within My Purchases.
- The purchased resource can be accessed from the user's account.
- The user can download the resource associated with their purchase.
- Access to the purchased resource is linked to the authenticated user's recorded purchase.
- A resource that has already been purchased does not need to be purchased again through the normal user journey.
