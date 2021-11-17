from django.db import models

# Create your models here.


class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Candidate(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title}"


class CandidateSkill(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}: {self.candidate} with skill: {self.skill}"


class Job(models.Model):
    title = models.CharField(max_length=100)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

    def __str__(self):
        return f"title: {self.title} job skill: {self.skill.name}"

