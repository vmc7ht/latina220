#Form for making Application
from django import forms
from .models import Route

#class ApplicationForm(forms.Form):
#class ApplicationForm(forms.Form):
    #school_name = forms.CharField(label='School Name', max_length=100)
    #request_amount = forms.CharField(label = "Amount Requested for funding",max_length = 100)

class RouteModelForm(forms.ModelForm):
	class Meta:
		model = Route 
		exclude = ["current_route_ns","route_carrier_first_name","T6_carrier_zone","T6_carrier_last_name","T6_id","T6_type"] #hide this on form