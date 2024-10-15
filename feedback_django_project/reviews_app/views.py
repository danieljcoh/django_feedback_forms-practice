from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ReviewForm

# Create your views here.


def review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponseRedirect("/thank-you")

    else:
        form = ReviewForm()  # generating a brand new form

    return render(request, "reviews_app/review.html", {
        "form": form
    })


def thank_you(request):
    return render(request, "reviews_app/thank_you.html", {
        "has_error": False
    })
