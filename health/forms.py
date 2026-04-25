from django import forms

class MentalHealthForm(forms.Form):


    feature_1 = forms.FloatField(
        label='Вопрос 1: Ваш возраст',
        widget=forms.NumberInput(attrs={
            'placeholder': 'Введите число от 0 до 100',
            'class': 'form-control',
            'step': '0.1'
        })
    )
    
    # Признак 2
    GENDER_CHOICES = [
        ('male', 'Мужчина'),
        ('female', 'Женщина'),
    ]
    
    feature_2 = forms.ChoiceField(
        label='Ваш пол:',
        choices=GENDER_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'gender-radio'}),
        required=True
    )
    
    # Признак 3
    feature_3 = forms.FloatField(
        label='Вопрос 3: Время проведенное в соц сетях за день',
        widget=forms.NumberInput(attrs={
            'placeholder': 'Введите число от 0 до 10',
            'class': 'form-control',
            'step': '0.1'
        })
    )
    
    SOCIAL_CHOICES = [
        ('TikTok', 'TikTok'),
        ('Instagram', 'Instagram'),
        ('Both', 'Оба'),
    ]
    
    feature_4 = forms.ChoiceField(
        label='Какой соцсетью вы пользуетесь чаще?',
        choices=SOCIAL_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'social-radio'}),
        required=True
    )
    
    # Признак 5
    feature_5 = forms.FloatField(
        label='Вопрос 5: Сколько вы спите в часах?',
        widget=forms.NumberInput(attrs={
            'placeholder': 'Введите число от 0 до 10',
            'class': 'form-control',
            'step': '0.1'
        })
    )
    
    # Признак 6
    feature_6 = forms.FloatField(
        label='Вопрос 6: Сколько часов вы проводите за телефоном перед сном?',
        widget=forms.NumberInput(attrs={
            'placeholder': 'Введите число от 0 до 10',
            'class': 'form-control',
            'step': '0.1'
        })
    )
    
    # Признак 7
    feature_7 = forms.FloatField(
        label='Вопрос 7: Ваша средняя оценка в школе:',
        widget=forms.NumberInput(attrs={
            'placeholder': 'Введите число от 0 до 5',
            'class': 'form-control',
            'step': '0.1'
        })
    )
    
    # Признак 8
    feature_8 = forms.FloatField(
        label='Вопрос 8: Оцените Вашу физическую активность',
        widget=forms.NumberInput(attrs={
            'placeholder': 'Введите число от 0 до 10',
            'class': 'form-control',
            'step': '0.1'
        })
    )
    
    # Признак 9
    LONELINESS_CHOICES = [
        ('low', 'Слабое'),
        ('medium', 'Среднее'),
        ('high', 'Сильное'),
    ]
    
    feature_9 = forms.ChoiceField(
        label='Какой уровень одиночества вы испытываете?',
        choices=LONELINESS_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'loneliness-radio'}),
        required=True
    )
    
    # Признак 10
    feature_10 = forms.FloatField(
        label='Вопрос 10: Оцените ваш уровень стресса',
        widget=forms.NumberInput(attrs={
            'placeholder': 'Введите число от 0 до 10',
            'class': 'form-control',
            'step': '0.1'
        })
    )
    
    # Признак 11
    feature_11 = forms.FloatField(
        label='Вопрос 11: Anxient level',
        widget=forms.NumberInput(attrs={
            'placeholder': 'Введите число от 0 до 10',
            'class': 'form-control',
            'step': '0.1'
        })
    )
    
    # Признак 12
    feature_12 = forms.FloatField(
        label='Вопрос 12: Оцените вашу зависимость от телефона',
        widget=forms.NumberInput(attrs={
            'placeholder': 'Введите число от 0 до 10',
            'class': 'form-control',
            'step': '0.1'
        })
    )