from django.urls import path

from . import views


app_name = "notes"

urlpatterns = [
    path("", views.home, name="home"),
    path("notes/", views.browse_notes, name="browse"),
    path("notes/<int:pk>/", views.note_detail, name="detail"),
    path("revision/", views.revision_notes, name="revision_list"),
    path("revision/add/", views.revision_create, name="revision_create"),
    path(
        "revision/<int:pk>/",
        views.revision_detail,
        name="revision_detail",
    ),
    path(
        "revision/<int:pk>/edit/",
        views.revision_edit,
        name="revision_edit",
    ),
    path(
        "revision/<int:pk>/delete/",
        views.revision_delete,
        name="revision_delete",
    ),
    path("purchases/", views.my_purchases, name="purchases"),
    path("download/<int:pk>/", views.download_note, name="download"),
]
