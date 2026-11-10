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

UniNotes is deployed on Heroku. The production application uses PostgreSQL, while local development uses SQLite by default.

### Deploy to Heroku

1. Connect the UniNotes GitHub repository to your Heroku app and select the branch you want to deploy.
2. Attach a Heroku PostgreSQL database and confirm that `DATABASE_URL` is available in the app's Config Vars.
3. Set `DEBUG=False`, add the Heroku hostname to `ALLOWED_HOSTS`, and configure `SECRET_KEY` and the Stripe test keys in Config Vars.
4. Deploy the selected branch. The project's `Procfile` starts Django with Gunicorn.
5. Apply the database migrations from your terminal. Replace `YOUR_HEROKU_APP_NAME` with the app name shown in your Heroku dashboard.

   ```bash
   heroku run python manage.py migrate --app YOUR_HEROKU_APP_NAME
   ```

6. For a fresh database, load the demo subjects and study notes.

   ```bash
   heroku run python manage.py loaddata subjects studynotes --app YOUR_HEROKU_APP_NAME
   ```

7. Open the deployed app and check the homepage, browsing, registration, login, revision notes, and Stripe Checkout in test mode. Record the results and compare them with the same checks on your local version.

See [Heroku troubleshooting](docs/bug-fixes.md#jump-bugs-during-deployment) for the database, migration, and checkout issues encountered during deployment.

### Testing

The recorded full Django test run passed all 15 tests. See [Testing and evidence](docs/testing.md) for the automated results and manual checks.

From the project root, with the virtual environment activated, run:

```bash
python manage.py check
python manage.py test
```

For manual testing, use two test accounts and a signed-out browser window.

1. Check the homepage, navigation, search and subject filtering.
2. Register, sign out and sign back in.
3. Create, view, edit and delete a revision note.
4. Upload an attachment and download it as the owner.
5. Open the attachment URL using another account and confirm access is denied.
6. Complete a Stripe test payment and download the purchased resource.
7. Cancel a separate checkout and confirm that no purchase is added.
8. Repeat these checks locally and on Heroku to compare their behaviour.

Full test results, screenshots and deployment checks are documented in
[Testing and evidence](docs/testing.md).