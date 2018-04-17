from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.conf import settings

import requests
from amazon.api import AmazonAPI
from .forms import AsinForm
# Create your views here.




def asin_search_api(asin_number):
	amazon = AmazonAPI(settings.AMAZON_ACCESS_KEY, 
					settings.AMAZON_SECRET_KEY, 
					settings.AMAZON_ASSOC_TAG)
	product = amazon.lookup(ItemId=asin_number)	
	return product


def get_asin(request):
	if request.method == "POST":
		asin_number = request.POST.get('asin_number')
		print (asin_number)
		product = asin_search_api(asin_number)
		print (product)
	return render (request, 'asin_db_query/query_db_with_asin.html')