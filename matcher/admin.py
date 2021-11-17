from django.contrib import admin

# Register your models here.
from .models import Skill, Candidate, Job, CandidateSkill

admin.site.register(Skill)
admin.site.register(Candidate)
admin.site.register(Job)
admin.site.register(CandidateSkill)