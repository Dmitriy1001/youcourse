from django import forms 
from .models import Course

from bootstrap_datepicker_plus import *
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class CourseCreateEditForm(forms.ModelForm):
	class Meta:
		model = Course
		fields = ('name', 'image', 'annotation', 'text', 'lectures_number',
				  'start', 'end')
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control'}),
			'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
			'annotation': forms.Textarea(attrs={'class': 'form-control'}),
			'text': SummernoteWidget(attrs={'class': 'form-control'}),
			'lectures_number': forms.NumberInput(attrs={'class': 'form-control'}),
			'start': DateTimePickerInput(format='%Y-%m-%d %H:%M'),
			'end': DatePickerInput(format='%Y-%m-%d'),
		}