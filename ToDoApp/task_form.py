from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    title = forms.CharField(
        label='titulo',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        ),
        required=True
    )
    description = forms.CharField(
        label='descrição',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    status = forms.CharField(
        label='status',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    due_date = forms.DateTimeField(
        label='data vencimento',
        widget=forms.DateInput(
            attrs={
                'type':'date',
                'class': 'form-control'
            }
        )
    )

    class Meta: 
        model = Task
        fields = ['title', 'description', 'status', 'due_date']