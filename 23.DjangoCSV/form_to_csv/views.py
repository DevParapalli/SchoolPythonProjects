from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import InputForm
# Create your views here.
def home_view(request):
    if request.method == 'GET':
        context = {}
        context['form'] = InputForm()
        return render(request, 'form_to_csv/home.html', context)
    elif request.method == 'POST':
        # Custom logic for writing 2 columns to CSV file.
        with open('./output.csv', 'a') as outfile:
            for key in request.POST:
                print(request.POST[key] + ',', end='', file=outfile)
            print("", file=outfile)
            context = {}
            context['saved_data'] = request.POST
        return render(request, 'form_to_csv/response.html', context)