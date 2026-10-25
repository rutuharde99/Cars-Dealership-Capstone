from django.urls import path
from .views import login_user, logout_user, get_dealer_reviews

urlpatterns = [
    path("login/", login_user, name="login_user"),
    path("logout/", logout_user, name="logout_user"),
    path(
        "getdealerreviews/<int:dealer_id>/",
        get_dealer_reviews,
        name="get_dealer_reviews",
    ),
]
