from django.urls import path
from . import views


urlpatterns = [
    path("", views.review, name="review_home"),
    path("thank-you", views.thank_you)
]
