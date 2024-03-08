from django.urls import path
from . import views

urlpatterns = [
    path("projects/", views.ProjectTable.as_view()),
    path("about/", views.AboutTable.as_view()),
    path("team/", views.TeamMemberTable.as_view()),
    path("contact/", views.ContactPost.as_view()),
]
