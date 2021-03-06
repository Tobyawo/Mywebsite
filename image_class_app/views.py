from django.shortcuts import render
# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
import base64
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.conf import settings 
from tensorflow.python.keras.backend import set_session
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.imagenet_utils import decode_predictions
import matplotlib.pyplot as plt
import numpy as np
from keras.applications import vgg16
from tensorflow.keras.models import load_model, Model
import datetime
import traceback



def index(request):
    if  request.method == "POST":
        file = request.FILES['sentFile'] # here you get the files needed
        response = {}

        file_name = default_storage.save(file.name, file)
        file_url = default_storage.url(file_name)

        original = load_img(file_url, target_size=(224, 224))
        numpy_image = img_to_array(original)
        

        image_batch = np.expand_dims(numpy_image, axis=0)
        # prepare the image for the VGG model

        processed_image = vgg16.preprocess_input(image_batch.copy())
        
        # get the predicted probabilities for each class
        with settings.GRAPH1.as_default():
            set_session(settings.SESS)
            predictions=settings.VGG_MODEL.predict(processed_image)
       
        label = decode_predictions(predictions)
       #name = list(label)[0][0][1]
        label = list(label)[0][0][1]
        response['name'] = str(label)

        return render(request,"result.html",{"response": response})
    else:
        return render(request,"image_class.html")


