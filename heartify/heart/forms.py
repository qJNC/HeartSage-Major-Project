from django import forms

class HeartDiseaseForm(forms.Form):
	# Define form fields for heart disease prediction

	age = forms.FloatField(label='Age', widget=forms.NumberInput(attrs={'class': 'box',"placeholder":"Enter your Age"}))
	# Field for age, represented as a float input widget

	sex = forms.FloatField(label='Gender', widget=forms.NumberInput(attrs={'class': 'box',"placeholder":"0=Female,1=Male"}))
	# Field for sex, represented as a float input widget

	cp = forms.FloatField(label='Chest Pain', widget=forms.NumberInput(attrs={'class': 'box',"placeholder":"0=typical 1=non-typical,2=non angina,3=asymptomatic"}))
	# Field for chest pain type (CP), represented as a float input widget

	trestbps = forms.FloatField(label='Resting BP', widget=forms.NumberInput(attrs={'class': 'box',"placeholder":"in mm Hg"}))
	# Field for resting blood pressure (TRESTBPS), represented as a float input widget

	chol = forms.FloatField(label='Cholestrol', widget=forms.NumberInput(attrs={'class': 'box',"placeholder":"in mg/dl"}))
	# Field for serum cholesterol level (CHOL), represented as a float input widget

	fbs = forms.FloatField(label='Blood Sugar', widget=forms.NumberInput(attrs={'class': 'box',"placeholder":"0=False,1=True"}))
	# Field for fasting blood sugar (FBS), represented as a float input widget

	restecg = forms.FloatField(label='RESTECG', widget=forms.NumberInput(attrs={'class': 'box',"placeholder":"0=normal,1=abnormal,2=Maybe"}))
	# Field for resting electrocardiographic results (RESTECG), represented as a float input widget

	thalach = forms.FloatField(label='Maximum Heart Rate', widget=forms.NumberInput(attrs={'class': 'box'}))
	# Field for maximum heart rate achieved (THALACH), represented as a float input widget

	exang = forms.FloatField(label='Exercise', widget=forms.NumberInput(attrs={'class': 'box',"placeholder":"0=yes,1=No"}))
	# Field for exercise-induced angina (EXANG), represented as a float input widget

	oldpeak = forms.FloatField(label='OLDPEAK', widget=forms.NumberInput(attrs={'class': 'box'}))
	# Field for ST depression induced by exercise relative to rest (OLDPEAK), represented as a float input widget

	slope = forms.FloatField(label='SLOPE ', widget=forms.NumberInput(attrs={'class': 'box',"placeholder":"0=upsloping,1=flat,2=downsloping"}))
	# Field for the slope of the peak exercise ST segment (SLOPE), represented as a float input widget

	ca = forms.FloatField(label='CA', widget=forms.NumberInput(attrs={'class': 'box'}))
	# Field for the number of major vessels colored by fluoroscopy (CA), represented as a float input widget

	thal = forms.FloatField(label='Genetic issues', widget=forms.NumberInput(attrs={'class': 'box',"placeholder":"0=error,1=fixed defects,2=normal,3=reversal defects"}))
	# Field for thalassemia (THAL), represented as a float input widget
