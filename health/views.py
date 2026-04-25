
from django.shortcuts import render
from .test import predict
import pandas as pd
from django.shortcuts import render
from .forms import MentalHealthForm

columns_test = ['age', 'gender', 'daily_social_media_hours', 'platform_usage',
       'sleep_hours', 'screen_time_before_sleep', 'academic_performance',
       'physical_activity', 'social_interaction_level', 'stress_level',
       'anxiety_level', 'addiction_level']



def my_view(request):
    result = None
    
    if request.method == 'POST':
        form = MentalHealthForm(request.POST)
        if form.is_valid():
            features = pd.DataFrame([[
                form.cleaned_data['feature_1'],
                form.cleaned_data['feature_2'],
                form.cleaned_data['feature_3'],
                form.cleaned_data['feature_4'],
                form.cleaned_data['feature_5'],
                form.cleaned_data['feature_6'],
                form.cleaned_data['feature_7'],
                form.cleaned_data['feature_8'],
                form.cleaned_data['feature_9'],
                form.cleaned_data['feature_10'],
                form.cleaned_data['feature_11'],
                form.cleaned_data['feature_12'],
            ]], columns=columns_test)
            
            # Делаем предсказание
            result = predict(features)
            if result == 0:
                new_res = 'Нет депрессии'
            else:
                new_res = 'Есть депрессия'
            

    else:
        form = MentalHealthForm()
        new_res = None
    
    return render(request, 'home.html', {
        'form': form,
        'result': new_res
    })