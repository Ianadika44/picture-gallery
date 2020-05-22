from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
import datetime as dt
from .models import Article

# Create your views here.


def welcome(request):
    return render(request, 'welcome.html')


def gallery_today(request):
    date = dt.date.today()
    return render(request, 'all-gallery/today-gallery.html', {"date": date, })


def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday', "Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day


def past_days_gallery(request, past_date):
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(gallery_of_day)

    gallery = Article.days_gallery(date)
    return render(request, 'gallery/past-gallery.html', {"date": date, "gallery": gallery})


def gallery_today(request):
    date = dt.date.today()
    gallery = Article.todays_gallery()
    return render(request, 'gallery/today-gallery.html', {"date": date, "gallery": gallery})

def search_results(request):
    
    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Article.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'gallery/search.html', {"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'gallery/search.html',{"message":message})