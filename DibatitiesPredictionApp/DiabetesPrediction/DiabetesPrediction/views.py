from django.contrib import admin
from django.urls import path
from django.shortcuts import render

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn  import svm
from sklearn.model_selection import train_test_split


def home(request):
    return render(request, 'home.html')

def predict(request):
    return render(request, 'predict.html')

def result(request):
    data = pd.read_csv(r'C:\Users\Kumar Abhinav\Desktop\Codings\Dibatics Prj\diabetes.csv')
    X = data.drop('Outcome', axis = 1)
    Y = data['Outcome']
    scalr = StandardScaler()
    scalr.fit(X)
    Stand_data = scalr.transform(X)
    X = Stand_data
    Y = data['Outcome']
    x_train, x_test, y_train, y_test = train_test_split(X,Y, test_size = 0.2, random_state = 2)
    model2 = svm.SVC(kernel='linear')
    model2.fit(x_train, y_train)

    val1 = float(request.GET['n1'] )
    val2 = float(request.GET['n2'] )
    val3 = float(request.GET['n3'] )
    val4 = float(request.GET['n4'] )
    val5 = float(request.GET['n5'] )
    val6 = float(request.GET['n6'] )
    val7 = float(request.GET['n7'] )
    val8 = float(request.GET['n8'] )

    pred = model2.predict([[val1,val2,val3,val4,val5,val6,val7,val8]])

    result1 = ''.isupper()

    if pred==[1]:
        result1 = 'You have high chance of being positive'

    else:
        result1 = 'You are negative'

    
    return render(request, 'predict.html', {'result2':result1})