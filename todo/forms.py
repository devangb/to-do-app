from django import forms
from models import ToDoItem



class CreateToDoItemForm(forms.ModelForm):

    class Meta:
        model = ToDoItem
        fields = ('description','assigned_at',)
        widgets = {
            'assigned_at': forms.DateInput(attrs={'id':'id_assigned_at'}),
        }