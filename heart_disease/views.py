from django.shortcuts import render

# Create your views here.
from django import forms
from django.http import HttpResponseBadRequest, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
#import sklearn
#from sklearn.preprocessing import MinMaxScaler

#from models import *
import pickle

# Create your views here.

def index(request): 
    return render(request, "heart_disease/heart_index.html")

def getPredictions(age, sex, cp, trestbps, chol, fbs, restecg, thalach,exang, oldpeak, slope, ca, thal):
	model = pickle.load(open('heart_disease/heart_disease_model.pkl', 'rb'))
	scaler = pickle.load(open('heart_disease/normalizer.pkl', 'rb'))
	final_features = scaler.fit_transform([age, sex, cp, trestbps, chol, fbs, restecg, thalach,exang, oldpeak, slope, ca, thal])
	prediction = model.predict(final_features)
	#print("prediction:",prediction)
	if prediction == 0:
		return "No Heart Disease"
	elif prediction == 1:
		return "Heart Disease present"
	else:
		return "error"

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

	result = getPredictions(age, sex, cp, trestbps, chol, fbs, restecg, thalach,exang, oldpeak, slope, ca, thal)
	return render(request, 'heart_index.html',{'prediction_text':result})
	#return render(request, 'result.html',{'result':result})
