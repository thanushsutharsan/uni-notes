from django.core.management.base import BaseCommand

from notes.models import StudyNote, Subject


SUBJECTS = [
    ("Business", "business"),
    ("Computer Science", "computer-science"),
    ("Law", "law"),
    ("Mathematics", "mathematics"),
    ("Psychology", "psychology"),
    ("Economics", "economics"),
]

NOTES = [
    (
        "Business",
        "Marketing Principles Revision Notes",
        "Key marketing models, definitions and exam-focused summaries.",
        "5.00",
        "study_notes/marketing_principles.pdf",
    ),
    (
        "Computer Science",
        "Data Structures Summary Notes",
        "Arrays, stacks, queues, linked lists and trees explained clearly.",
        "6.00",
        "study_notes/data_structures.pdf",
    ),
    (
        "Law",
        "Contract Law Complete Notes",
        "A concise overview of core contract law principles.",
        "7.00",
        "study_notes/contract_law.pdf",
    ),
    (
        "Mathematics",
        "Calculus Fundamentals",
        "Differentiation and integration rules with revision reminders.",
        "5.50",
        "study_notes/calculus_fundamentals.pdf",
    ),
    (
        "Psychology",
        "Cognitive Psychology Revision Guide",
        "Memory, attention and research evaluation in concise sections.",
        "5.50",
        "study_notes/cognitive_psychology.pdf",
    ),
    (
        "Economics",
        "Microeconomics Exam Notes",
        "Demand, supply, equilibrium and elasticity for exam revision.",
        "6.00",
        "study_notes/microeconomics.pdf",
    ),
    (
        "Computer Science",
        "Database Systems Revision Notes",
        "Relational databases, keys, normalisation and SQL fundamentals.",
        "6.50",
        "study_notes/database_systems.pdf",
    ),
    (
        "Business",
        "Business Finance Essentials",
        "Revenue, costs, profit and break-even explained for revision.",
        "5.00",
        "study_notes/business_finance.pdf",
    ),
]


class Command(BaseCommand):
    help = "Create Uni Notes demo subjects and downloadable marketplace notes."

    def handle(self, *args, **options):
        subject_map = {}
        for name, slug in SUBJECTS:
            subject, _ = Subject.objects.get_or_create(
                name=name,
                defaults={"slug": slug},
            )
            if subject.slug != slug:
                subject.slug = slug
                subject.save(update_fields=["slug"])
            subject_map[name] = subject

        for subject_name, title, description, price, note_file in NOTES:
            note, _ = StudyNote.objects.update_or_create(
                title=title,
                defaults={
                    "subject": subject_map[subject_name],
                    "description": description,
                    "price": price,
                    "note_file": note_file,
                    "download_url": "",
                    "is_active": True,
                },
            )
            self.stdout.write(f"Ready: {note.title}")

        self.stdout.write(
            self.style.SUCCESS(
                "Demo subjects and downloadable Uni Notes created."
            )
        )
