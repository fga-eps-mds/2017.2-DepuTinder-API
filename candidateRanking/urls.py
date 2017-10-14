from django.conf.urls import url
from .views import RankingViewSet

urlpatterns = [
    url(r'^ranking/$', RankingViewSet.as_view())
]
