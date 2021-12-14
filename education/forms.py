import bootstrap_datepicker_plus as datepicker
from django import forms
from django_summernote.widgets import SummernoteWidget

from .models import Course


class CourseCreateEditForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = (
            'name',
            'image',
            'annotation',
            'text',
            'lectures_number',
            'start',
            'end',
        )
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'annotation': forms.Textarea(attrs={'class': 'form-control'}),
            'text': SummernoteWidget(attrs={'class': 'form-control'}),
            'lectures_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'start': datepicker.DateTimePickerInput(format='%Y-%m-%d %H:%M'),
            'end': datepicker.DateTimePickerInput(format='%Y-%m-%d %H:%M'),
        }
