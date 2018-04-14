from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def get_asin(request):
	if request.method == "POST":
		asin_number = request.POST.get('asin_number')
		print (asin_number)
	return render (request, 'asin_db_query/query_db_with_asin.html')