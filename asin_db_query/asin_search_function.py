from django.conf import settings

import requests
from amazon.api import AmazonAPI

def asin_search_api(asin_number):
	amazon = AmazonAPI(settings.AMAZON_ACCESS_KEY, 
					settings.AMAZON_SECRET_KEY, 
					settings.AMAZON_ASSOC_TAG)
	product = amazon.lookup(ItemId=asin_number)	
	return product