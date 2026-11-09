# Research

[Back to UniNotes README](../README.md#documentation)

## Contents

- [User Research](#user-research)
- [Competitor Research](#jump-competitor-research)
  - [Studocu](#studocu)
  - [StudySmarter](#studysmarter)
  - [Quizlet](#quizlet)
- [Research Findings](#jump-research-findings)
- [How Research will Influence Development](#how-research-will-influence-development)
- [Research Sources](#research-sources)

---

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


<a name="jump-competitor-research"></a>

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


<a name="jump-research-findings"></a>

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
