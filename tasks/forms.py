from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'priority', 'is_complete']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'due_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
            'is_complete': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class TaskSearchForm(forms.Form):
    q = forms.CharField(
        label='Search',
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Search tasks...',
            'class': 'form-control'
        })
    )
