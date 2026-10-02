from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import include, path

from notes import views as notes_views


urlpatterns = [
    path("accounts/register/", notes_views.register, name="register"),
    path(
        "accounts/login/",
        auth_views.LoginView.as_view(redirect_authenticated_user=True),
        name="login",
    ),
    path(
        "accounts/logout/",
        auth_views.LogoutView.as_view(),
        name="logout",
    ),
    path("checkout/", include("checkout.urls")),
    path("", include("notes.urls")),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
