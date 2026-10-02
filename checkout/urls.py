from django.urls import path

from . import views


app_name = "checkout"

urlpatterns = [
    path("buy/<int:pk>/", views.create_checkout_session, name="buy"),
    path("success/", views.payment_success, name="success"),
    path("cancel/<int:pk>/", views.payment_cancel, name="cancel"),
]
