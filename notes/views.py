from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import FileResponse, Http404
from django.shortcuts import get_object_or_404, redirect, render

from .decorators import anonymous_required
from .forms import RegisterForm, RevisionNoteForm
from .models import Purchase, RevisionNote, StudyNote, Subject


def home(request):
    featured_notes = StudyNote.objects.filter(is_active=True)[:3]
    subjects = Subject.objects.all()[:6]
    return render(
        request,
        "notes/home.html",
        {"featured_notes": featured_notes, "subjects": subjects},
    )


def browse_notes(request):
    notes = StudyNote.objects.filter(is_active=True).select_related("subject")
    subjects = Subject.objects.all()
    query = request.GET.get("q", "").strip()
    subject_slug = request.GET.get("subject", "").strip()

    if query:
        notes = notes.filter(
            Q(title__icontains=query)
            | Q(description__icontains=query)
            | Q(subject__name__icontains=query)
        )

    if subject_slug:
        notes = notes.filter(subject__slug=subject_slug)

    return render(
        request,
        "notes/browse.html",
        {
            "notes": notes,
            "subjects": subjects,
            "query": query,
            "selected_subject": subject_slug,
        },
    )


def note_detail(request, pk):
    note = get_object_or_404(StudyNote, pk=pk, is_active=True)
    purchased = False
    if request.user.is_authenticated:
        purchased = Purchase.objects.filter(
            user=request.user,
            note=note,
        ).exists()

    return render(
        request,
        "notes/detail.html",
        {"note": note, "purchased": purchased},
    )


@anonymous_required
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created successfully.")
            return redirect("notes:home")
    else:
        form = RegisterForm()

    return render(request, "registration/register.html", {"form": form})


@login_required
def my_purchases(request):
    purchases = Purchase.objects.filter(user=request.user).select_related(
        "note",
        "note__subject",
    )
    return render(
        request,
        "notes/my_purchases.html",
        {"purchases": purchases},
    )


@login_required
def download_note(request, pk):
    purchase = get_object_or_404(
        Purchase.objects.select_related("note"),
        user=request.user,
        note_id=pk,
    )
    note = purchase.note

    if note.note_file:
        try:
            return FileResponse(
                note.note_file.open("rb"),
                as_attachment=True,
                filename=note.note_file.name.rsplit("/", 1)[-1],
            )
        except (FileNotFoundError, OSError):
            raise Http404("The purchased note file is unavailable.")

    if note.download_url:
        return redirect(note.download_url)

    raise Http404("No download is available for this note.")


@login_required
def revision_notes(request):
    notes = RevisionNote.objects.filter(owner=request.user)
    return render(
        request,
        "notes/revision_list.html",
        {"revision_notes": notes},
    )


@login_required
def revision_detail(request, pk):
    note = get_object_or_404(
        RevisionNote,
        pk=pk,
        owner=request.user,
    )
    return render(
        request,
        "notes/revision_detail.html",
        {"revision_note": note},
    )


@login_required
def revision_create(request):
    if request.method == "POST":
        form = RevisionNoteForm(request.POST, request.FILES)
        if form.is_valid():
            note = form.save(commit=False)
            note.owner = request.user
            note.save()
            messages.success(request, "Revision note saved to your account.")
            return redirect(note.get_absolute_url())
    else:
        form = RevisionNoteForm()

    return render(
        request,
        "notes/revision_form.html",
        {"form": form, "page_title": "Add revision note"},
    )


@login_required
def revision_edit(request, pk):
    note = get_object_or_404(
        RevisionNote,
        pk=pk,
        owner=request.user,
    )
    if request.method == "POST":
        form = RevisionNoteForm(
            request.POST,
            request.FILES,
            instance=note,
        )
        if form.is_valid():
            form.save()
            messages.success(request, "Revision note updated.")
            return redirect(note.get_absolute_url())
    else:
        form = RevisionNoteForm(instance=note)

    return render(
        request,
        "notes/revision_form.html",
        {
            "form": form,
            "page_title": "Edit revision note",
            "revision_note": note,
        },
    )


@login_required
def revision_delete(request, pk):
    note = get_object_or_404(
        RevisionNote,
        pk=pk,
        owner=request.user,
    )
    if request.method == "POST":
        note.delete()
        messages.success(request, "Revision note deleted.")
        return redirect("notes:revision_list")

    return render(
        request,
        "notes/revision_confirm_delete.html",
        {"revision_note": note},
    )
