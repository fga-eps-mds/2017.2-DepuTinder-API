import json
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from votings.models import Votings
from parlamentarians.models import Parlamentarians

@api_view(['GET'])

# request parameter must be here
def rankingIndex(request):
    rankingResultData = {
     "rankingInfo": [
        {"groupID":90,"candidates":["Armando"]},
        {"groupID":80,"candidates":["Donelle","Sammy","Thor"]},
        {"groupID":70,"candidates":["Loise","Burtie"]},
        {"groupID":60,"candidates":["Alejandrina","Cleveland","Ronda"]}
     ],
    }
    return Response(rankingResultData, status=status.HTTP_200_OK)

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
    generate_match(parlamentarians, answeredQuestions, super_match, high_match, medium_match, low_match)
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




def generate_results(super_match, high_match, medium_match, low_match):
    results = {
    "70% - 100%": super_match,
    "50% - 70%": high_match,
    "30% - 50%": medium_match,
    "10% - 30%": low_match,
    }
    print(results)
    return results
