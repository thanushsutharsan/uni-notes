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

# Planning Phase
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

## Research

Research was carried out during the planning of **UniNotes** to understand the needs of potential users and to identify common features used by existing educational and revision platforms.

The research focused on two areas:

- **User Research** – identifying what the primary and secondary target audiences would need from the application.
- **Competitor Research** – reviewing existing study platforms to identify useful features, common design approaches and opportunities that could influence UniNotes.

The purpose of this research was not to copy existing applications, but to understand how established study platforms support students and use the findings to make informed development decisions.


### User Research

The user research focused on the two target audiences identified during the UX planning stage.

The **primary users** are university students actively looking for revision resources and wanting to organise their own study material.

The **secondary users** are students who are exploring the platform before deciding whether to register or purchase a resource.

The needs of both groups were considered when planning the functionality of UniNotes.

| User Type | User Need | Planned Solution |
|---|---|---|
| **Primary User** | Find revision resources quickly | Provide a searchable study-note library |
| **Primary User** | Find resources for a particular subject | Allow resources to be filtered by subject |
| **Primary User** | Understand what a resource contains before purchasing | Provide individual study-note pages containing the title, subject, description and price |
| **Primary User** | Purchase revision material online | Integrate Stripe Checkout |
| **Primary User** | Access previously purchased resources | Provide a personalised **My Purchases** section |
| **Primary User** | Organise personal revision material | Provide a private Revision area |
| **Primary User** | Update revision material | Allow users to edit existing revision notes |
| **Primary User** | Remove material they no longer need | Allow users to delete their own revision notes |
| **Primary User** | Store supporting revision material | Allow an optional file to be attached to revision notes |
| **Primary User** | Keep personal revision notes private | Associate notes with the authenticated user and apply ownership checks |
| **Secondary User** | Understand what UniNotes offers before registering | Allow visitors to browse available study resources |
| **Secondary User** | Check whether relevant subjects are available | Allow visitors to explore and filter subjects |
| **Secondary User** | Search before creating an account | Provide keyword searching within the study-note library |
| **Secondary User** | Understand a resource before deciding whether to use the platform | Allow individual study-note information to be viewed |
| **Secondary User** | Navigate without previous experience | Use clear and consistent navigation |
| **Secondary User** | Understand the benefits of registration | Clearly separate public browsing from personalised account features |

The user research showed that **speed, organisation, clarity and personalisation** should be important priorities within UniNotes.


### Competitor Research

Competitor research was carried out by examining [**Studocu**](https://www.studocu.com/), [**StudySmarter**](https://www.studysmarter.co.uk/) and [**Quizlet**](https://quizlet.com/).

These platforms were selected because they provide functionality related to digital study resources, revision material and personal study organisation.

Researching existing platforms helped identify successful approaches that could influence UniNotes while still allowing the project to maintain its own purpose and feature set.

| Competitor | Research Findings | Strengths Identified | Influence on UniNotes |
|---|---|---|---|
| [**Studocu**](https://www.studocu.com/) | Studocu provides a large collection of study materials including lecture notes, summaries, past exams and practice resources. Resources can also be searched based on areas of study. | Provides students with a central location for finding relevant academic resources. | Supported the decision to create a centralised study-note library and provide search functionality. |
| [**StudySmarter**](https://www.studysmarter.co.uk/) | StudySmarter provides study materials and tools for organising learning content, including personal notes and study sets. | Combines learning resources with personal study organisation within one platform. | Influenced the decision to provide a personal Revision area alongside prepared study resources. |
| [**Quizlet**](https://quizlet.com/) | Quizlet allows users to create study materials and discover existing learning resources. | Gives students control over their own learning content while providing access to existing study material. | Reinforced the decision to allow users to create and manage their own revision notes while also browsing prepared resources. |


#### Studocu

[**Studocu**](https://www.studocu.com/) was researched because it provides a large online collection of educational resources.

The research showed that the platform provides different types of academic study materials, including:

- Lecture notes
- Summaries
- Past exams
- Practice resources
- Other student study materials

A useful aspect of Studocu is the way resources are organised around courses and areas of study.

This influenced UniNotes by supporting the decision to organise study notes using **subjects** and provide **search functionality** so that users can find relevant resources without browsing the entire library.

**Official Research Source:**
[Studocu Official Website](https://www.studocu.com/)


#### StudySmarter

[**StudySmarter**](https://www.studysmarter.co.uk/) was researched because it combines learning resources with tools for creating and organising personal study material.

Features identified during the research included:

- Personal notes
- Study sets
- Learning resources
- Study organisation
- Personal study material

One particularly relevant feature was the ability for users to create and organise their own study content.

This influenced the development of the **UniNotes Revision area**, where registered users can create, view, edit and delete their own revision notes.

StudySmarter also demonstrates the value of keeping different types of revision material in a central location rather than requiring students to manage resources across several different applications.

**Official Research Sources:**

- [StudySmarter Official Website](https://www.studysmarter.co.uk/)
- [StudySmarter Notes](https://www.studysmarter.co.uk/features/notes/)
- [StudySmarter Study Sets](https://www.studysmarter.co.uk/features/study-sets/)


#### Quizlet

[**Quizlet**](https://quizlet.com/) was researched because it focuses heavily on allowing students to create and interact with learning content.

The research identified features including:

- Creating study material
- Searching existing study material
- Flashcards
- Study guides
- Practice activities
- Different study modes

Quizlet demonstrates how allowing users to create their own content can encourage them to return to a study platform regularly.

This supported the decision to make UniNotes more than simply a marketplace for purchasing digital notes.

The **Revision** functionality allows registered users to create and maintain their own study material, providing an additional reason to return to the application after purchasing a resource.

**Official Research Sources:**

- [Quizlet Official Website](https://quizlet.com/)
- [Quizlet Flashcards](https://quizlet.com/features/flashcards)
- [Quizlet Study Modes](https://quizlet.com/gb/features/study-modes)


### Research Findings

The combined user and competitor research produced several findings that were used to guide the development of UniNotes.

| Research Finding | Evidence from Research | UniNotes Response |
|---|---|---|
| Students need to find resources quickly | [Studocu](https://www.studocu.com/) provides searchable academic resources | Keyword searching is included |
| Resources should be organised logically | Competitor platforms organise material around courses, subjects or study sets | UniNotes organises resources by subject |
| Students need information before choosing a resource | Educational platforms provide information about available study materials | Individual study-note pages provide details before purchase |
| Users benefit from a central study location | [StudySmarter](https://www.studysmarter.co.uk/) combines multiple study tools within one platform | UniNotes combines purchased resources and personal revision functionality |
| Students create their own study content | [StudySmarter](https://www.studysmarter.co.uk/) and [Quizlet](https://quizlet.com/) provide tools for personal study material | UniNotes provides personal revision notes |
| Personal content needs to be editable | Study platforms allow users to maintain their own learning content | UniNotes provides CRUD functionality for revision notes |
| Returning users need continued access to content | Study platforms retain account-based study materials | UniNotes provides **My Purchases** and personal Revision areas |
| Users benefit from personalised accounts | Competitor platforms provide account-based functionality | Purchases and personal revision notes are linked to authenticated users |
| Students may access study resources on different devices | Modern study platforms are designed for digital access | UniNotes uses responsive layouts and navigation |
| New visitors should understand the platform easily | Competitor platforms clearly communicate their study functionality | UniNotes uses clear navigation and allows resources to be explored before account-specific actions |


### How Research will Influence Development

The research findings will influence the development of UniNotes by helping prioritise features that provide clear value to the identified target audiences.

| Research Finding | Development Decision |
|---|---|
| Students need fast access to relevant resources | Develop a searchable study-note library |
| Students need resources relevant to their area of study | Include subject-based filtering |
| Users need information before purchasing | Provide individual study-note detail pages |
| Visitors may want to explore before registering | Keep browsing functionality available to unauthenticated visitors |
| Students benefit from organised study environments | Create clearly separated Browse, Revision and My Purchases areas |
| Users create their own learning material | Provide personal revision-note functionality |
| Revision material changes over time | Implement Create, Read, Update and Delete functionality |
| Supporting material may accompany revision notes | Support optional file attachments |
| Personal study content requires privacy | Apply authentication and ownership checks |
| Returning users require continued access | Store previous purchases within My Purchases |
| Online purchases require a secure process | Integrate Stripe Checkout |
| Users need a consistent experience across devices | Implement responsive page layouts and navigation |
| Users need confirmation after actions | Provide appropriate success and feedback messages |
| Empty results should be understandable | Display useful empty-state messages when content cannot be found |


### Research Sources

The following official websites were used during competitor research:

| Source | Official Link | Research Used For |
|---|---|---|
| **Studocu** | [Visit Studocu](https://www.studocu.com/) | Study-note libraries, searching, course-specific resources and academic study material |
| **StudySmarter** | [Visit StudySmarter](https://www.studysmarter.co.uk/) | Overall study-platform structure and organisation of study resources |
| **StudySmarter Notes** | [View Notes Feature](https://www.studysmarter.co.uk/features/notes/) | Creating and managing personal study notes |
| **StudySmarter Study Sets** | [View Study Sets](https://www.studysmarter.co.uk/features/study-sets/) | Organisation of revision material |
| **Quizlet** | [Visit Quizlet](https://quizlet.com/) | Creating, discovering and studying learning material |
| **Quizlet Flashcards** | [View Flashcards](https://quizlet.com/features/flashcards) | User-created study material and flashcard functionality |
| **Quizlet Study Modes** | [View Study Modes](https://quizlet.com/gb/features/study-modes) | Different approaches to interacting with revision resources |

These sources were used to identify common approaches within existing educational platforms. The findings were then evaluated against the requirements and scope of UniNotes rather than copying competitor functionality directly.

Including the original research sources also provides evidence of where the findings came from and allows the research to be independently checked.

This research-driven approach helps demonstrate that the features within UniNotes were selected based on **target-user requirements, competitor analysis and evidence from existing educational platforms**.

## I. Strategy

The strategy for **UniNotes** focuses on creating a clear and useful university revision platform that combines access to digital study resources with personal revision management.

The project strategy was developed from the identified user needs, business goals, user stories and research findings. The aim is to ensure that each feature included within the application has a clear purpose and solves a genuine problem for the target audience.

The strategy prioritises the most important functionality first, including resource discovery, user authentication, purchasing, access to purchased material and personal revision-note management.

Rather than trying to include too many features in the first version of the application, development focuses on a realistic **Minimum Viable Product (MVP)** that provides the core functionality required for UniNotes to operate successfully.


### Project Goals

The main goal of UniNotes is to create a reliable and easy-to-use platform where university students can find revision resources, purchase study notes and organise their own revision material.

The project goals are:

| Project Goal | Purpose |
|---|---|
| **Provide easy access to study resources** | Allow students to browse a centralised collection of university revision notes without needing to search across several different websites or folders. |
| **Improve resource discovery** | Use keyword searching and subject filtering to help students find relevant revision material more efficiently. |
| **Provide clear resource information** | Give users enough information about each study note before they decide whether it is relevant or worth purchasing. |
| **Support secure online purchasing** | Allow authenticated users to purchase digital study resources using Stripe Checkout. |
| **Provide persistent access to purchases** | Allow users to return to resources they have already purchased through My Purchases. |
| **Support personal revision** | Give registered users a private area where they can create and manage their own revision notes. |
| **Provide meaningful CRUD functionality** | Allow users to create, read, update and delete their personal revision notes. |
| **Protect user-specific content** | Ensure personal revision notes and purchases remain associated with the correct authenticated user. |
| **Provide responsive usability** | Make the application usable across different screen sizes and devices. |
| **Provide clear user feedback** | Inform users when important actions such as registration, saving, editing or deleting content have been completed. |
| **Maintain a scalable structure** | Organise study notes by subject so additional resources can be introduced without changing the overall structure of the website. |
| **Create a realistic full-stack application** | Combine a database, authentication, CRUD functionality, external payment processing, file handling and responsive front-end design within one project. |

These goals support both the needs of the users and the potential business purpose of UniNotes as a digital study-resource platform.


### User Problems and Solutions

The development strategy is based around solving specific problems experienced by the target users.

| User Problem | UniNotes Solution |
|---|---|
| Students may store revision resources across several different locations | UniNotes provides a centralised platform for accessing study resources and personal revision material. |
| Students may find it difficult to locate resources relevant to a specific topic | Keyword searching allows users to search the study-note library. |
| Users may only want resources relating to a particular subject | Subject filtering allows the available notes to be narrowed down. |
| Users need to understand a resource before purchasing it | Individual study-note pages provide details including the title, subject, description and price. |
| New visitors may not want to register immediately | Visitors can explore public areas of the platform before using account-specific features. |
| Students need a secure way of purchasing digital resources | Stripe Checkout is used to handle the payment process. |
| Students may need purchased resources more than once | Completed purchases are stored against the user's account and made available through My Purchases. |
| Users may accidentally attempt to purchase the same resource again | The application checks existing purchase records within the normal purchase journey. |
| Students create their own revision material as well as using prepared resources | Registered users are provided with a private Revision area. |
| Revision notes may need to be changed as the student learns more | Users can edit previously created revision notes. |
| Old revision material may no longer be useful | Users can delete their own revision notes. |
| Students may need to store supporting documents with their notes | Revision notes support optional file attachments. |
| Personal revision material should not be accessible to other users | Authentication and ownership checks are used when accessing account-specific revision-note functionality. |
| Users may not know whether an action has completed successfully | Feedback messages are provided following important actions. |
| Students may access the platform from different screen sizes | Responsive layouts and navigation are used within the interface. |

By linking development decisions directly to user problems, the features within UniNotes have a clear reason for being included rather than being added only to increase the size of the project.


### Minimum Viable Product (MVP)

The **Minimum Viable Product (MVP)** represents the minimum set of features required for UniNotes to fulfil its main purpose.

The MVP focuses on the complete user journey rather than including advanced functionality that is not essential to the first working version of the platform.

The core MVP requirements are:

| MVP Requirement | Reason Required |
|---|---|
| **Homepage and navigation** | Users need a clear entry point and a way of moving between the main areas of the application. |
| **User registration** | Users need accounts before personalised features can be associated with them. |
| **User login and logout** | Users need a secure way to access and leave their personal account. |
| **Study-note library** | The application requires a central area where available digital resources can be browsed. |
| **Subject organisation** | Study resources need to be grouped logically so users can locate relevant content. |
| **Keyword search** | Users need a faster method of finding relevant study notes. |
| **Subject filtering** | Users need to narrow the available study notes by subject. |
| **Individual study-note pages** | Users need information about a resource before purchasing it. |
| **Stripe Checkout integration** | The application needs a realistic way for registered users to purchase digital study resources. |
| **Purchase recording** | Successful purchases need to be stored against the correct authenticated user. |
| **My Purchases** | Users need a way to return to resources they have already purchased. |
| **Purchased-file access** | Users need to be able to access and download resources they own. |
| **Personal revision area** | Registered users need a location for managing their own revision material. |
| **Create revision note** | Users need to add new revision material. |
| **Read revision note** | Users need to view saved revision content. |
| **Update revision note** | Users need to modify revision material as their knowledge develops. |
| **Delete revision note** | Users need control over removing content they no longer require. |
| **Optional revision attachment** | Users may need to keep supporting files alongside their revision notes. |
| **Authentication and ownership protection** | Private and account-specific functionality needs to remain associated with the correct user. |
| **Responsive design** | The application needs to remain usable across different screen sizes. |
| **User feedback messages** | Users need confirmation after completing important actions. |

The MVP therefore provides a complete basic journey where a user can:

1. Visit UniNotes.
2. Browse available study notes.
3. Search or filter resources.
4. View the details of a study note.
5. Register or log into an account.
6. Purchase a resource through Stripe Checkout.
7. Access the purchased resource through My Purchases.
8. Create their own personal revision notes.
9. Edit or delete their personal revision material.
10. Return later and continue using their saved content.

This ensures that the first working version of UniNotes already provides meaningful functionality before additional features are considered.


### Features

The features implemented within UniNotes support the goals of the MVP and the requirements identified during UX planning and research.

| Feature | Description | User Benefit |
|---|---|---|
| **User Registration** | Allows new users to create an account. | Provides access to personalised features. |
| **Login and Logout** | Allows registered users to securely access and leave their account. | Protects user-specific functionality. |
| **Study-Note Library** | Displays the available revision resources. | Gives students a central location for finding study material. |
| **Keyword Search** | Allows users to search for study notes using text. | Reduces the time required to find relevant resources. |
| **Subject Filtering** | Allows the study-note library to be filtered by subject. | Helps users focus on resources relevant to their studies. |
| **Study-Note Detail Pages** | Displays information about an individual study note. | Helps users decide whether the resource is suitable before purchasing. |
| **Stripe Checkout** | Provides the hosted payment process for study-note purchases. | Allows users to purchase resources without UniNotes directly handling payment-card information. |
| **Purchase Verification** | Checks completed Stripe Checkout information before storing the purchase. | Helps ensure purchases are only recorded after successful payment. |
| **My Purchases** | Displays resources previously purchased by the authenticated user. | Gives users a convenient location for returning to purchased material. |
| **Purchased Resource Download** | Allows eligible users to access the file associated with a completed purchase. | Provides continued access to purchased digital resources. |
| **Personal Revision Area** | Provides authenticated users with their own revision-note section. | Gives students a private space for managing revision material. |
| **Create Revision Note** | Allows users to create a new revision note. | Enables users to add their own study content. |
| **View Revision Note** | Allows users to access previously created revision notes. | Makes personal revision material reusable. |
| **Edit Revision Note** | Allows users to update revision-note content. | Supports ongoing learning and corrections. |
| **Delete Revision Note** | Allows users to remove revision notes they no longer need. | Helps keep the revision area organised. |
| **Revision Attachments** | Allows an optional supporting file to be added to a revision note. | Helps users keep related revision resources together. |
| **Ownership Checks** | Ensures users can only modify personal revision notes belonging to their own account. | Protects private user content. |
| **Responsive Navigation** | Adjusts navigation behaviour for smaller screens. | Improves usability across different devices. |
| **Accessibility Features** | Includes features such as labels, alternative text, skip links and accessible navigation attributes. | Makes the interface easier to understand and interact with. |
| **Feedback Messages** | Provides confirmation following important actions. | Reassures users that their action has been completed. |
| **Empty-State Messages** | Explains when no content or matching search result is available. | Prevents users from being confused by an empty page. |


### Future Features

The first version of UniNotes focuses on the functionality required for the MVP. Additional features could be introduced in future development if the platform were expanded.

Future features would only be added where they provide clear value to users and do not unnecessarily complicate the existing experience.

| Future Feature | Description | Potential Benefit |
|---|---|---|
| **Ratings and Reviews** | Allow users who have purchased a study note to leave a rating or written review. | Could help other students decide whether a resource is useful. |
| **Wish List / Saved Resources** | Allow users to save study notes they are interested in purchasing later. | Would make it easier for users to return to resources they have discovered. |
| **Advanced Search** | Add additional filters such as price range, topic or recently added resources. | Would improve resource discovery if the study-note library becomes larger. |
| **Recently Viewed Resources** | Show study notes that a logged-in user has recently viewed. | Would make it easier to return to previously explored resources. |
| **Revision Categories or Tags** | Allow users to add additional categories or tags to personal revision notes. | Would make larger collections of personal notes easier to organise. |
| **Revision Search** | Allow users to search within their own personal revision notes. | Would help users find specific revision content as their collection grows. |
| **Favourites** | Allow users to mark important revision notes or purchased resources as favourites. | Would provide faster access to frequently used material. |
| **Study Progress Tracking** | Allow users to mark topics or revision notes as complete or still requiring revision. | Could help students manage their revision progress. |
| **Resource Preview** | Provide a limited preview of a study resource before purchase where appropriate. | Could give users additional information before deciding to purchase. |
| **Email Purchase Confirmation** | Send users an email confirming a successful purchase. | Would provide an additional record of completed transactions. |
| **Password Reset by Email** | Allow users to securely recover access to their account through an email-based password reset. | Would improve account recovery and usability. |
| **User Profile Settings** | Allow users to manage additional account preferences. | Would provide greater personalisation. |
| **Improved Resource Recommendations** | Suggest resources based on subjects previously viewed or purchased. | Could help users discover relevant study material more quickly. |
| **Additional Accessibility Improvements** | Continue testing and improving keyboard navigation, contrast and screen-reader support. | Would make UniNotes more accessible to a wider range of users. |
| **Expanded Automated Testing** | Add further automated tests covering edge cases and additional user journeys. | Would help improve reliability as the application grows. |

These features are considered **future developments rather than MVP requirements** because the existing application can fulfil its main purpose without them.

Prioritising the MVP first helps keep development manageable and ensures that the most important user journeys are completed and tested before more advanced functionality is introduced.


### User Problems and Solutions

The development of **UniNotes** is based on solving clear problems faced by the target audience. Each feature within the application has been designed to address a specific user need identified during the UX and research stages.

The table below shows the main problems identified and how UniNotes provides a practical solution.

| User Problem | UniNotes Solution | Benefit to the User |
|---|---|---|
| Students may store revision resources across different websites, folders and devices | UniNotes provides one central platform for accessing study resources and personal revision notes | Makes revision material easier to organise and reduces the need to search across multiple locations |
| Students may struggle to find resources related to a specific topic | Keyword search allows users to search the study-note library | Helps users locate relevant resources more quickly |
| Users may only want revision material for a particular subject | Subject filtering allows users to narrow the available resources | Reduces irrelevant results and improves resource discovery |
| A large study-note library could become difficult to navigate | Resources are organised by subject and displayed in a structured format | Makes the library easier to browse as more resources are added |
| Students need to understand a resource before purchasing it | Individual study-note pages display information such as the title, subject, description and price | Allows users to make a more informed decision before purchasing |
| First-time visitors may not want to create an account immediately | Visitors can browse study resources and explore the platform before using account-specific features | Reduces barriers for new users and allows them to understand the value of the platform first |
| Students need a secure way to purchase digital revision resources | Stripe Checkout is used to handle the payment process | Provides a recognised external payment process without UniNotes directly handling card details |
| Users may accidentally attempt to purchase the same resource again | Existing purchases are checked during the normal purchasing process | Reduces unnecessary repeat purchases |
| Students need continued access to resources after buying them | Purchased resources are stored against the user's account and displayed in **My Purchases** | Allows users to return to purchased material during future revision sessions |
| Students may forget where they downloaded purchased resources | My Purchases provides a central location for previously purchased study notes | Keeps purchased materials organised and easy to access |
| Students create their own revision material as well as using prepared resources | Registered users have access to a private Revision area | Allows students to manage personal study material within the same application |
| Students need to create new revision content | Users can create their own revision notes | Allows revision material to be tailored to the student's own studies |
| Revision material may need to change as the student learns more | Existing revision notes can be edited | Allows users to correct, expand or update their notes without creating a new note |
| Old revision material may become unnecessary | Users can delete revision notes they no longer require | Helps keep the personal revision area organised |
| Students may have supporting documents linked to their revision | Revision notes support optional file attachments | Allows related revision materials to be stored together |
| Personal revision notes should remain private | Revision notes are associated with the authenticated user and ownership checks are applied | Helps prevent users from editing or deleting another user's private content |
| Users need to know whether actions have been completed successfully | Feedback messages are displayed after important actions | Gives users confirmation and reduces uncertainty |
| Users may become confused when a search returns no results | Clear empty-state messages explain when no matching content is available | Prevents users from assuming the website has failed |
| Students may use UniNotes on different screen sizes | Responsive layouts and navigation are used throughout the interface | Improves usability across desktop, tablet and mobile-sized screens |
| First-time users may not understand how to move around the website | Clear and consistent navigation is used across the main pages | Makes the application easier to learn and reduces confusion |
| Users need personalised areas to be clearly separated from public content | Features such as **Revision** and **My Purchases** are linked to authenticated users | Makes it clear which features belong to the user's account |
| Users may try to access protected features without being logged in | Authentication is required for account-specific functionality | Protects private data and ensures personalised actions are linked to the correct account |

These solutions demonstrate that the functionality within UniNotes has been developed around identified user needs rather than being added without purpose.

By connecting each problem to a specific solution, the project can demonstrate a clear relationship between **research, user requirements, UX planning and technical implementation**.

