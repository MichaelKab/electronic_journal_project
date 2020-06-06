from django.urls import path, include
from .views import UsersListView, UsersDetailView
urlpatterns = [
    path('1', UsersListView.as_view()),
    path('<pk>', UsersDetailView.as_view()),
    
]