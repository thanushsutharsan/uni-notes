from decimal import Decimal

from django.conf import settings
from django.core.validators import FileExtensionValidator, MinValueValidator
from django.db import models
from django.urls import reverse


class Subject(models.Model):
    name = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=90, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class StudyNote(models.Model):
    subject = models.ForeignKey(
        Subject,
        on_delete=models.PROTECT,
        related_name="notes",
    )
    title = models.CharField(max_length=120)
    description = models.TextField(max_length=1200)
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("0.50"))],
    )
    cover_url = models.URLField(blank=True)
    note_file = models.FileField(
        upload_to="study_notes/",
        blank=True,
        validators=[
            FileExtensionValidator(
                allowed_extensions=["pdf"]
            )
        ],
    )
    download_url = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("notes:detail", args=[self.pk])


class RevisionNote(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="revision_notes",
    )
    title = models.CharField(max_length=120)
    subject = models.CharField(max_length=100)
    content = models.TextField(max_length=5000)
    attachment = models.FileField(
        upload_to="revision_notes/%Y/%m/",
        blank=True,
        validators=[
            FileExtensionValidator(
                allowed_extensions=["pdf", "doc", "docx", "txt"]
            )
        ],
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_at"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("notes:revision_detail", args=[self.pk])


class Purchase(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="note_purchases",
    )
    note = models.ForeignKey(
        StudyNote,
        on_delete=models.CASCADE,
        related_name="purchases",
    )
    stripe_session_id = models.CharField(max_length=255, unique=True)
    amount_paid = models.DecimalField(max_digits=6, decimal_places=2)
    purchased_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-purchased_at"]
        constraints = [
            models.UniqueConstraint(
                fields=["user", "note"],
                name="unique_user_note_purchase",
            )
        ]

    def __str__(self):
        return f"{self.user} - {self.note}"
