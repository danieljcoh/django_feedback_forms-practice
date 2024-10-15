from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from .forms import ReviewForm
from .models import Review

# Create your views here.

class ReviewView(View):

    def get(self, request):
        form = ReviewForm()  # generating a brand new form

        return render(request, "reviews_app/review.html", {
            "form": form,
    })

    def post(self, request):
         form = ReviewForm(request.POST, instance=existing_model)

        if form.is_valid():
            form.save() # because of the ModelForm
            return HttpResponseRedirect("/thank-you")

        return render(request, "reviews_app/review.html", {
            "form": form,
    })


def thank_you(request):
    return render(request, "reviews_app/thank_you.html", {
        "has_error": False
    })
