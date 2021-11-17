import json
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render

# Create your views here.
from matcher.models import Job, Candidate, CandidateSkill, Skill


def skill(request, skill_id):
    skill = get_object_or_404(Skill, pk=skill_id)
    skill_data = {"skill_id": skill_id, "skill_name": skill.name}
    return HttpResponse(json.dumps(skill_data))


def candidate(request, candidate_id):
    candidate = get_object_or_404(Candidate, pk=candidate_id)
    candidate_data = {"candidate_id": candidate_id, "title": candidate.title}
    return HttpResponse(json.dumps(candidate_data))


def job(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    job_data = {"job_id": job_id, "title": job.title, "skill": job.skill.name}
    return HttpResponse(json.dumps(job_data))


def candidate_skills(request, candidate_id):
    try:
        candidate_skills = CandidateSkill.objects.all().filter(candidate_id=candidate_id)
        skills = []
        for candidate_skill in candidate_skills:
            skills.append(candidate_skill.skill.name)

        candidate_skills_data = {"candidate_id": candidate_id, "skills": skills}
    except CandidateSkill.DoesNotExist:
        raise Http404("Candidate id: {} does not exist" % candidate_id)
    return HttpResponse(json.dumps(candidate_skills_data))


def candidate_finder(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    match_candidates = []
    relevant_candidates_by_title = Candidate.objects.filter(title__startswith=job.title[0:5])

    for candidate in relevant_candidates_by_title:
        candidate_skills = []
        skills = CandidateSkill.objects.filter(candidate__id=candidate.id).values_list('skill', flat=True)
        for skill in skills:
            candidate_skills.append(skill)

        match_skill = list({job.skill.id} & set(candidate_skills))
        match_skills_num = len(match_skill)
        match_candidates.append({"candidate_id": candidate.id, "candidate_title":candidate.title, "match_skill":match_skills_num})

    match_candidates = sorted(match_candidates, key=lambda d: d['match_skill'], reverse=True)
    match_candidates = match_candidates[:5]
    return HttpResponse(json.dumps(match_candidates))
