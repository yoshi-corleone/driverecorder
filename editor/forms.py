from django import forms
from .models import Course
from recorder.models import Point


class CourseForm(forms.ModelForm):
    name = forms.CharField(max_length=255)
    points = forms.ModelMultipleChoiceField(queryset=Point.objects.all(),
                                            widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Course
        fields = ('name', 'points')
