"""DepuTinder_API URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from propositions.views import PropositionsView
from votings.views import votings
from questionnaire.views import questionnaire
from parlamentarians.views import parlamentarians
from users.views import users
from candidateRanking.views import rankingIndex
from questionnaire.views import answeredQuestions

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^propositions/', PropositionsView),
    url(r'^votings/', votings),
    url(r'^ranking/', rankingIndex),
    url(r'^questionnaire/', questionnaire),
    url(r'^users/', users),
    url(r'^parlamentarians/', parlamentarians),
    url(r'^sendAnsweredQuestions/', answeredQuestions),
]
