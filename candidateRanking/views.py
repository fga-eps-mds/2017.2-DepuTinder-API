import json
import simplejson
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from votings.models import Votings
from parlamentarians.models import Parlamentarians
from candidateRanking.models import CandidateRanking
from django.http import JsonResponse

@api_view(['GET'])

# request parameter must be here
def rankingIndex(request):
    ranking = CandidateRanking.objects.all()[:1].get()
    print(ranking)
    response = simplejson.loads(ranking.ranking)
    low_match = simplejson.loads(response['10% - 30%'])
    medium_match = simplejson.loads(response['30% - 50%'])
    high_match = simplejson.loads(response['50% - 70%'])
    super_match = simplejson.loads(response['70% - 100%'])
    rankingResultData = {
     "rankingInfo": [
        {"groupID":"70-100","candidates": super_match},
        {"groupID":"50 - 70","candidates": high_match},
        {"groupID":"30-50","candidates": medium_match},
        {"groupID":"10 - 30","candidates": low_match},
        ],
    }
    return JsonResponse(rankingResultData, safe=False)

@api_view(['PUT'])
def answeredQuestions(request):
    if(request.data):
        answeredQuestions = request.data
        generate_ranking(answeredQuestions)
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


def generate_ranking(answeredQuestions):
    parlamentarians = Parlamentarians.objects.all()
    super_match = []
    high_match = []
    medium_match = []
    low_match = []
    generate_match(parlamentarians, answeredQuestions,
                   super_match, high_match, medium_match,
                   low_match)
    generate_results(super_match, high_match, medium_match, low_match)


def generate_match(parlamentarians, answeredQuestions, super_match, high_match, medium_match, low_match):
    for parlamentary in parlamentarians:
        count = 0
        votings = list(Votings.objects.filter(candidateID = parlamentary.id))
        for i in range(10):
            if answeredQuestions[i]['answer'] == votings[i].candidateVote:
                count += 1

        if count >= 7:
            super_match.append(parlamentary)
        elif count >= 5 and count < 7:
            high_match.append(parlamentary)
        elif count >= 3 and count < 5:
            medium_match.append(parlamentary)
        elif count >= 1 and count < 3:
            low_match.append(parlamentary)

def toJson(parlamentary):
    return json.dumps(parlamentary, default=lambda o: o.__dict__, sort_keys=True, indent=4)

def generate_results(super_match, high_match, medium_match, low_match):
    ranking_match = {
    "70% - 100%": toJson(super_match),
    "50% - 70%": toJson(high_match),
    "30% - 50%": toJson(medium_match),
    "10% - 30%": toJson(low_match),
    }
    results = json.dumps(ranking_match)
    CandidateRanking.objects.all().delete()
    ranking, created = CandidateRanking.objects.get_or_create(
        ranking = results
    )
    if (created):
        print("Ranking criado com sucesso " )
    else:
        print("Ranking não pôde ser criado " )
