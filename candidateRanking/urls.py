from django.conf.urls import url
from .views import RankingViewSet
from candidateRanking.views import (rankingIndex)

urlpatterns = [
    url(r'^ranking/', rankingIndex),
]
