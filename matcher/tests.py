import json

from django.test import TestCase
from django.urls import reverse

from matcher.models import Job, Candidate, CandidateSkill, Skill


# Create your tests here.

class MatcherTests(TestCase):
    def setUp(self):
        java_skill = Skill.objects.create(name="Java")
        kotlin_skill = Skill.objects.create(name="Kotlin")
        cad_skill = Skill.objects.create(name="CAD")

        candidate_sd = Candidate.objects.create(title="Software Developer")
        candidate_pm = Candidate.objects.create(title="Product Manager")

        CandidateSkill.objects.create(candidate=candidate_sd, skill=java_skill)
        CandidateSkill.objects.create(candidate=candidate_sd, skill=kotlin_skill)
        CandidateSkill.objects.create(candidate=candidate_pm, skill=cad_skill)

        Job.objects.create(title="Software Engineer", skill=java_skill)

    def test_get_all_candidate_skills(self):
        candidate_sd = Candidate.objects.get(title="Software Developer")
        url = reverse('matcher:candidateSkills', args=(candidate_sd.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'candidate_id': 1, 'skills': ['Java', 'Kotlin']}
        )

    def test_candidate_finder(self):
        se_job = Job.objects.get(title="Software Engineer")
        url = reverse('matcher:candidateFinder', args=(se_job.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            [{'candidate_id': 1, 'candidate_title': 'Software Developer', 'match_skill': 1}]
        )

    def test_get_non_exist_candidate(self):
        non_exist_id = 10
        url = reverse('matcher:candidate', args=(non_exist_id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
