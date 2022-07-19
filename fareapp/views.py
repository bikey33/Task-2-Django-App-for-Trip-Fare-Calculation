from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Faredata

# Create your views here.
def home(request):
    context = {}
    error_message = None
    if request.method == "POST":
        t = request.POST['time']
        am_or_pm = request.POST['select']
        distance = request.POST['distance']
        # Validating if each field has valid data or not
        # Validating whether each field is empty or not
        if (not t):
            # If field empty throw error message
            error_message = "Time is required in HH:MM format"
        elif t:
            try:
                # Try to  split the Hr and Min parts of data
                t_hr, t_mn = map(int, t.split(':'))
                # Converting Hr in 12 Hour Format to 24 hour format
                if (am_or_pm == "1"):
                    time_24 = t_hr
                    am = 'AM'
                else:
                    am = 'PM'
                    time_24 = t_hr + 12

            except:
                error_message = "Please Provide Time in HH:MM Format"


        if not distance:
            error_message = "Please Provide a valid distance in Km"
        else:
            try:
                dist_float = float(distance) # Try converting data to float
            except:
                error_message = "Enter Valid distance"

        if not am_or_pm:
            error_message = "Please Select either AM or PM"



        # Read Data  for fare calculation  from database
        if not error_message:
            try:
                data = Faredata.objects.get(time=time_24)
                Initial_rate = data.initial_fare
                km_rate = data.km_rate
                surge_rate = data.surge_charge
                service_charge = data.service_charge
                print(km_rate)
                distance_fare = dist_float* km_rate
                # Calculating Fares both variable and fixed
                trip_fare = Initial_rate + dist_float* km_rate
                service_inccur = (trip_fare*service_charge/100)
                surge_inccur = (trip_fare*surge_rate/100)
                # Calculating Total fares
                total_fare = trip_fare +(trip_fare*surge_rate/100) +(trip_fare*service_charge/100)

                print("Total fare inaccured is:",total_fare)
                # If Post request is made by submitting all the information
                print("Time:", time_24,'Time of Day:',am_or_pm, 'Distance:', distance)
                # Bundle all the fare data to be shown on the table and show total table in a dictionary
                context = {'total':total_fare, 'km_rate':km_rate,'surge_rate':surge_rate,'service_charge':service_charge,'initial_fare': Initial_rate,'distance_fare': distance_fare,'service_incurr':service_inccur,'surge_incurr':surge_inccur,'error_message':error_message,'time': t,'am':am,'distance':distance}
                # Pass context to HTML template side
                return render(request, 'home.html', context)

            except:
                error_message = " Enter HH:MM in 12 Hour Format"
                print(error_message)
                context= {'error_message':error_message}
                return render(request, 'home.html', context)


        else:
            print(error_message)
            context = {'error_message':error_message}
            return render(request,'home.html',context)
    return render(request, 'home.html', context)
