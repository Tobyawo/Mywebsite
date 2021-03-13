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
    return render(request, "heart_disease/heart_index.html")


def result(request):
	age = int(request.GET['age'])
	sex = int(request.GET['sex'])
	cp = int(request.GET['cp'])
	trestbps = int(request.GET['trestbps'])
	chol = int(request.GET['chol'])
	fbs = int(request.GET['fbs'])
	restecg = int(request.GET['restecg'])
	thalach = int(request.GET['thalach'])
	exang = int(request.GET['exang'])
	oldpeak = int(request.GET['oldpeak'])
	slope = int(request.GET['slope'])
	ca = int(request.GET['ca'])
	thal = int(request.GET['thal'])
	#####

	model = pickle.load(open('heart_disease/heart_disease_model.pkl', 'rb'))
	scaler = pickle.load(open('heart_disease/normalizer.pkl', 'rb'))

	features = [age, sex, cp, trestbps, chol, fbs, restecg, thalach,exang, oldpeak, slope, ca, thal]
	int_features = [x for x in features]
	final_features = [np.array(int_features)]
	final_features = scaler.fit_transform(final_features)
	prediction = model.predict(final_features)
	output = round(prediction[0], 2)
	if output == 0:
		return render(request, 'heart_disease/heart_index.html',{'prediction_text':"This Patient Has No Heart Disease"})
	elif output == 1:
		return render(request, 'heart_disease/heart_index.html',{'prediction_text':"Heart Disease Detected"})
	else:
		return render(request, 'heart_disease/heart_index.html',{'prediction_text':"Error"})
	


	
