from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import InputForm
from .models import CSVStore
import csv
# Create your views here.
def home_view(request):
    context = {}
    return render(request, 'form_to_csv/index_page.html', context)
    
def download_csv(request):
    query_set = CSVStore.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data.csv"'
    writer = csv.writer(response)
    writer.writerow(['username', 'message', 'message_time'])
    for item in query_set:
        writer.writerow([item.user_name, item.user_text, item.time.strftime('%m/%d/%Y')])
    return response
    

def add_data(request):
    if request.method == 'GET':
        context = {}
        context['form'] = InputForm()
        return render(request, 'form_to_csv/add_data.html', context)
    elif request.method == 'POST':
        context = {}
        form = InputForm(request.POST)
        if form.is_valid(): form.save()
        else: return HttpResponse('Error in form',status=400)
        context['saved_data'] = request.POST
        return render(request, 'form_to_csv/response.html', context)
    
def wipe_database(request):
    CSVStore.objects.all().delete()
    return HttpResponse('All Objects have been deleted. <a href="/">Back<a>')