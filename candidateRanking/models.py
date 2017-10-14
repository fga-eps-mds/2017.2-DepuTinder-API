from django.db import models

CANDIDATE_NAME_LENGHT = 150
CANDITATE_DESCRIPTION_LENGHT = 500
PARTYCANDIDATE_LENGHT = 5

class Ranking(models.Model):
    userID = models.OneToOneField(UserID, on_delete=models.CASCADE,)
    candidateGroup = models.ForeignKey(CandidateGroup, on_delete=models.CASCADE,)

class CandidateList(models.Model):
    candidate = models.ForeignKey(
    'Candidate', on_delete=models.CASCADE,
    )

class CandidateGroup(models.Model):
    groupPercentage: models.PositiveIntergerField(blank = False)
    candidateList = models.OneToOneField(CandidateList, on_delete=models.CASCADE,)

class Candidate(models.Model):
    candidateName = models.CharField(max_leght=CANDIDATE_NAME_LENGHT, blank=True)
    candidateDescripition = models.CharField(max_lenght=CANDIDATE_DESCRIPTION_LENGHT,
    blank=True)
    partyCandidate = models.CharField(max_lenght=PARTYCANDIDATE_LENGHT, blank=True)

class UserID(models.Model):
    userID = models.PositiveIntergerField(blank = False)
