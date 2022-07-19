from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    if request.method == "POST":
        t = request.POST['time']
        t_hr, t_mn = map(int,t.split(':'))
        distance = request.POST['distance']
        am_or_pm = request.POST['select']
        if(am_or_pm == "1"):
            time_24 = t_hr
        else:
            time_24 = t_hr + 12
    # If Post request is made by submitting all the information
        print("Time:", time_24,'Time of Day:',am_or_pm, 'Distance:', distance)
    return render(request,'home.html',{})