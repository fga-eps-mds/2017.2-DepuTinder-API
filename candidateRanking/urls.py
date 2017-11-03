from django.conf.urls import url
from .views import RankingViewSet
from candidateRanking.views import (rankingIndex)
from candidateRanking.views import (answeredQuestions)

urlpatterns = [
    url(r'^ranking/', rankingIndex),
    url(r'^answeredQuestions/', answeredQuestions),
]
