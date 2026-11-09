# UniNotes

## Introduction

UniNotes is a full-stack Django web application designed for university students who want a simple and organised way to access revision resources and manage their own study notes.

The application combines a study-note marketplace with a personal revision area. Students can register for an account, browse available study notes, search for resources, filter notes by subject, view individual note details and purchase resources through Stripe Checkout. Once a payment has been successfully confirmed, the purchased resource is added to the student's account and can be accessed through their personal purchase library.

Registered users can also create and manage their own private revision notes. These notes can be created, viewed, edited and deleted by their owner, providing full CRUD functionality while ensuring that users cannot access or modify another student's private revision content.

UniNotes uses Django, Python, HTML, CSS and JavaScript together with a relational database, Django authentication and Stripe payment processing to provide a complete full-stack application.

[Open the live UniNotes app](https://uni-notes-09bbb519e883.herokuapp.com/)

## Contents

- [Documentation](#documentation)
- [Deployment notes](#deployment-notes)

## Documentation

| # | Document | What it covers |
| --- | --- | --- |
| 1 | [Project background](docs/project-background.md) | Description, purpose, rationale and technologies used |
| 2 | [Users and user stories](docs/user-stories.md) | UX goals, target users, user stories and acceptance criteria |
| 3 | [Research](docs/research.md) | User research, competitor research and findings |
| 4 | [Project planning](docs/planning.md) | Strategy, scope and structure |
| 5 | [UX and interface design](docs/design.md) | Wireframes, interface planning and visual design |
| 6 | [Architecture and data model](docs/architecture.md) | Django apps, MVT, URLs and database design |
| 7 | [Features and implementation](docs/features.md) | CRUD, forms, authentication, checkout and API integration |
| 8 | [Security and code quality](docs/code-quality.md) | Security, defensive programming and code organisation |
| 9 | [Testing and evidence](docs/testing.md) | Testing strategy and automated Django tests |
| 10 | [Bug fixes and deployment](docs/bug-fixes.md) | Development fixes and Heroku deployment troubleshooting |

## Deployment notes

[Heroku deployment and troubleshooting](docs/bug-fixes.md#jump-bugs-during-deployment)
