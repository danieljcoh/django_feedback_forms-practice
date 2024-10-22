from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView

from .forms import ReviewForm
from .models import Review

# Create your views here.

class ReviewView(CreateView):
    model = Review
    fields = ""
    template_name = "reviews_app/review.html"
    success_url = /"thank-you" #for the POST request

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ThankYouView(TemplateView):
    template_name = "reviews_app/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This works!"
        return context
    

class ReviewListView(ListView):
    template_name = "reviews_app/review_list.html"
    model = Review
    context_object_name = "reviews" #instead of using object_list
    

class SingleReviewView(DetailView):
    template_name = "reviews_app/single_review.html"
    model = Review

    