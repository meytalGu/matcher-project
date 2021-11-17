from django.urls import path
from . import views

app_name = 'matcher'

urlpatterns = [
    path('<int:skill_id>/skill/', views.skill, name='skill'),
    path('<int:job_id>/job/', views.job, name='job'),
    path('<int:candidate_id>/candidate/', views.candidate, name='candidate'),
    path('<int:candidate_id>/candidateSkills/', views.candidate_skills, name='candidateSkills'),
    path('<int:job_id>/candidateFinder/', views.candidate_finder, name='candidateFinder'),
]