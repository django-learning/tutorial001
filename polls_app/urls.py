from django.urls import path
from .views import index, detail, results, vote

app_name = "polls"

urlpatterns = [
    path("", index, name="index"),
    path("<int:question_pk>/", detail, name="detail"),
    path("<int:question_pk>/results/", results, name="results"),
    path("<int:question_pk>/vote/", vote, name="vote"),
]
