from django.urls import path
from users import views as user_views


urlpatterns = [
    path('profile/', user_views.profile, name='profile'),
]