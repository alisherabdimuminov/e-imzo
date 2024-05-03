from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import login, signup, download, profile


urlpatterns = [
    path('login/', login, name="login"),
    path('signup/', signup, name="signup"),
    path('logout/', LogoutView.as_view(next_page="login"), name="logout"),
    path('download/<str:filename>/', download, name="download"),
    path('', profile, name="profile"),
]
