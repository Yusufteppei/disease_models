from django.shortcuts import render, redirect
from .forms import *
import pickle
from .models import *


def index(request):

    outcome = 9
    template = 'diabetes/index.html'
    context = {
        'form': DiabetesTestForm,
        'outcome': outcome,
        'bmi_form': BMIForm
    }
    return render(request, template, context)


def diagnose(request):
    outcome = 9
    if request.method == 'POST':
        form = DiabetesTestForm(request.POST)
        if form.is_valid():
            report_dict = form.cleaned_data
            print(report_dict)
            outcome = predict(report_dict)
            model = form.save(commit=False)
            model.outcome = outcome
            model.save()

        else:
            print('Form Invalid')
    else:
        print("Wrong Request Method")

    if outcome == 0:
        report = "You shall not worry about diabetes."
    else:
        report = "You have been diagnosed positive for diabetes."
    context = {
        'form': DiabetesTestForm,
        'report': report,
        'outcome': outcome,
        'bmi_form': BMIForm
    }
    return render(request, 'diabetes/index.html', context)


def predict(result_dict):

    f = open('diabetes/diabetes_model1.pickle', 'rb')
    print(f)
    pkl = pickle.load(f)

    pregnancies = result_dict['pregnancies']
    glucose = result_dict['glucose']
    blood_pressure = result_dict['blood_pressure']
    skin_thickness = result_dict['skin_thickness']
    insulin = result_dict['insulin']
    BMI = result_dict['BMI']
    age = result_dict['age']

    result_list = [pregnancies, glucose, blood_pressure, skin_thickness, insulin, BMI, age]

    outcome = pkl.predict([result_list])[0]

    return outcome


def calculate_bmi(request):
    if request.method == 'POST':
        form = BMIForm(request.POST)
        if form.is_valid():
            h = form.cleaned_data['height']
            w = form.cleaned_data['weight']
            bmi = int((w/h**2) * 10000)
        else:
            bmi = 0
    else:
        bmi = 0

    context = {
        'form': DiabetesTestForm,
        'bmi': bmi,
        'bmi_form': BMIForm
    }
    return render(request, 'diabetes/index.html', context)


def convert_to_csv(model):
    pass
