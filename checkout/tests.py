from decimal import Decimal
from unittest.mock import MagicMock, patch

from django.contrib.auth.models import User
from django.test import TestCase, override_settings
from django.urls import reverse

from notes.models import Purchase, StudyNote, Subject


class CheckoutTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="buyer",
            email="buyer@example.com",
            password="TestPass123!",
        )
        self.subject = Subject.objects.create(name="Business", slug="business")
        self.note = StudyNote.objects.create(
            subject=self.subject,
            title="Marketing Notes",
            description="Revision notes.",
            price=Decimal("5.00"),
            note_file="study_notes/marketing_principles.txt",
        )
        self.client.login(username="buyer", password="TestPass123!")

    @override_settings(STRIPE_SECRET_KEY="sk_test_example")
    @patch("checkout.views.stripe.checkout.Session.create")
    def test_checkout_session_redirects_to_stripe(self, mock_create):
        mock_create.return_value = MagicMock(
            url="https://checkout.stripe.com/test"
        )
        response = self.client.post(
            reverse("checkout:buy", args=[self.note.pk])
        )
        self.assertEqual(response.status_code, 303)
        self.assertEqual(response.url, "https://checkout.stripe.com/test")

    @override_settings(STRIPE_SECRET_KEY="sk_test_example")
    @patch("checkout.views.stripe.checkout.Session.retrieve")
    def test_success_creates_purchase(self, mock_retrieve):
        session = MagicMock()
        session.id = "cs_test_paid"
        session.payment_status = "paid"
        session.amount_total = 500
        session.metadata = {
            "user_id": str(self.user.pk),
            "note_id": str(self.note.pk),
        }
        mock_retrieve.return_value = session

        response = self.client.get(
            reverse("checkout:success"),
            {"session_id": session.id},
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            Purchase.objects.filter(user=self.user, note=self.note).exists()
        )
