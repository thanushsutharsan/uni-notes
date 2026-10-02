from decimal import Decimal

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .forms import RevisionNoteForm
from .models import RevisionNote, StudyNote, Subject


class StudyNoteModelTests(TestCase):
    def setUp(self):
        self.subject = Subject.objects.create(
            name="Business",
            slug="business",
        )
        self.note = StudyNote.objects.create(
            subject=self.subject,
            title="Marketing Principles Revision Notes",
            description="A concise set of revision notes.",
            price=Decimal("5.00"),
            note_file="study_notes/marketing_principles.pdf",
        )

    def test_note_string_returns_title(self):
        self.assertEqual(str(self.note), self.note.title)

    def test_note_absolute_url(self):
        self.assertEqual(
            self.note.get_absolute_url(),
            reverse("notes:detail", args=[self.note.pk]),
        )


class RevisionNoteFormTests(TestCase):
    def test_form_accepts_revision_content(self):
        form = RevisionNoteForm(
            data={
                "title": "Python Functions",
                "subject": "Computer Science",
                "content": "Functions group reusable instructions.",
            }
        )
        self.assertTrue(form.is_valid())


class AuthenticationAndAccessTests(TestCase):
    def setUp(self):
        self.subject = Subject.objects.create(
            name="Computer Science",
            slug="computer-science",
        )
        self.note = StudyNote.objects.create(
            subject=self.subject,
            title="Data Structures Summary Notes",
            description="Core data structures revision.",
            price=Decimal("6.00"),
            note_file="study_notes/data_structures.pdf",
        )
        self.user = User.objects.create_user(
            username="student",
            password="TestPass123!",
        )

    def test_purchase_page_requires_login(self):
        response = self.client.get(reverse("notes:purchases"))
        self.assertEqual(response.status_code, 302)

    def test_revision_page_requires_login(self):
        response = self.client.get(reverse("notes:revision_list"))
        self.assertEqual(response.status_code, 302)

    def test_register_page_redirects_logged_in_user(self):
        self.client.login(username="student", password="TestPass123!")
        response = self.client.get(reverse("register"))
        self.assertRedirects(response, reverse("notes:home"))

    def test_login_page_redirects_logged_in_user(self):
        self.client.login(username="student", password="TestPass123!")
        response = self.client.get(reverse("login"))
        self.assertRedirects(response, reverse("notes:home"))

    def test_download_requires_purchase(self):
        self.client.login(username="student", password="TestPass123!")
        response = self.client.get(
            reverse("notes:download", args=[self.note.pk])
        )
        self.assertEqual(response.status_code, 404)


class RevisionCrudTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="student",
            password="TestPass123!",
        )
        self.other_user = User.objects.create_user(
            username="otherstudent",
            password="TestPass123!",
        )
        self.client.login(username="student", password="TestPass123!")

    def test_user_can_create_revision_note(self):
        response = self.client.post(
            reverse("notes:revision_create"),
            {
                "title": "Arrays",
                "subject": "Computer Science",
                "content": "Arrays store ordered values.",
            },
        )
        self.assertEqual(RevisionNote.objects.count(), 1)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(RevisionNote.objects.first().owner, self.user)

    def test_user_can_view_own_revision_note(self):
        note = RevisionNote.objects.create(
            owner=self.user,
            title="Contract Law",
            subject="Law",
            content="Offer plus acceptance forms an agreement.",
        )
        response = self.client.get(
            reverse("notes:revision_detail", args=[note.pk])
        )
        self.assertEqual(response.status_code, 200)

    def test_user_can_edit_own_revision_note(self):
        note = RevisionNote.objects.create(
            owner=self.user,
            title="Old title",
            subject="Law",
            content="Original content.",
        )
        response = self.client.post(
            reverse("notes:revision_edit", args=[note.pk]),
            {
                "title": "Updated title",
                "subject": "Law",
                "content": "Updated content.",
            },
        )
        note.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(note.title, "Updated title")

    def test_user_can_delete_own_revision_note(self):
        note = RevisionNote.objects.create(
            owner=self.user,
            title="Delete me",
            subject="Maths",
            content="Temporary note.",
        )
        response = self.client.post(
            reverse("notes:revision_delete", args=[note.pk])
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(RevisionNote.objects.filter(pk=note.pk).exists())

    def test_user_cannot_view_another_users_revision_note(self):
        note = RevisionNote.objects.create(
            owner=self.other_user,
            title="Private note",
            subject="Psychology",
            content="Private revision content.",
        )
        response = self.client.get(
            reverse("notes:revision_detail", args=[note.pk])
        )
        self.assertEqual(response.status_code, 404)
