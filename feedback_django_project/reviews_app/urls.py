from django.urls import path
from . import views


urlpatterns = [
    path("", views.ReviewView.as_view(), name="review_home"),
    path("thank-you", views.ThankYouView.as_view(), name="thank-you-page"),
    path("reviews/", views.ReviewListView.as_view()),
    path("reviews/<int:pk>", views.SingleReviewView.as_view(), name="selected-review-details"),

]
