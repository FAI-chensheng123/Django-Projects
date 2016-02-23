from django import forms

from django.forms import modelformset_factory

from .models import Variation


class VariationInventoryForm(forms.ModelForm):
	class Mata:
		model = Variation
		fields = [
			"price",
			"sale_price",
			"inventory"
		]
#VariationInventoryFormSet = modelformset_factory(Variation, form=VariationInventoryForm, extra = 2)		