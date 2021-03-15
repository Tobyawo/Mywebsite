from django.shortcuts import render

# Create your views here.
from django import forms
from django.http import HttpResponseBadRequest, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
import numpy as np
#import sklearn
#from sklearn.preprocessing import MinMaxScaler

#from models import *
import pickle

# Create your views here.

def index(request): 
    return render(request, "sales_predict_app/sales_index.html")


def result(request):
	#lets import the model and normalizer
	model = pickle.load(open('sales_predict_app/sales_model.pkl', 'rb'))

	rate = int(request.GET['rate'])
	sales_in_first_month = int(request.GET['sales in first month'])
	sales_in_second_month = int(request.GET['sales in second month'])

	features = [rate, sales_in_first_month, sales_in_second_month]
	int_features = [x for x in features]
	final_features = [np.array(int_features)]
	prediction = model.predict(final_features)
	output = round(prediction[0], 2)
	return render(request, 'sales_predict_app/sales_index.html',{'prediction_text':'Sales should be ${}'.format(output)})
