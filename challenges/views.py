from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "january": "Eat no meat for the entire month",
    "february": "Walk for atleast 20 minutes every day",
    "march": "Learn Django everyday",
    "april": "Eat no meat for the entire month",
    "may": "Walk for atleast 20 minutes every day",
    "june": "Learn Django everyday",
    "july": "Eat no meat for the entire month",
    "august": "Walk for atleast 20 minutes every day",
    "september": "Learn Django everyday",
    "october": "Eat no meat for the entire month",
    "november": "Walk for atleast 20 minutes every day",
    "december": None
}

# Create your views here.

def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months_list": months  #passing the 'months' list as a parameter to the index.html
    })

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("<h1>Invalid Month!</h1>")
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) #/challenge/january
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request,month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "month_name": month,
            "text": challenge_text            #passing 2 parameters - months,challenge_text - to challenge.html
        })
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
    except:
        raise Http404()