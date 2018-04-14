from django import forms


class AsinForm(forms.Form):	
	asin_number = forms.CharField(
	    label = "Asin Form",
	    required=False,
	    widget=forms.TextInput(attrs={'class': "form-control", 
	        "placeholder":"Please enter your phone number"}),
	    )


