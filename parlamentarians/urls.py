from django.conf.urls import url
from .views import parlamentarians
from .requestData import parlamentariansData

urlpatterns = [
    url(r'^upload/(?P<parlamentariansData>[^/]+)$', FileUploadView.as_view())
]
