# forms.py
from django import forms
from .models import Category
from .models import Expense
from .models import RecurringExpense
from .models import Income
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['amount', 'category', 'content']

    widgets = {
        'amount': forms.NumberInput(attrs={'step': '0.01'}),
        'category': forms.Select(attrs={'class': 'form-control'}),
        'content': forms.Textarea(attrs={'rows': 4, 'cols': 50}),
    }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'budget_limit']


class RecurringExpenseForm(forms.ModelForm):
    class Meta:
        model = RecurringExpense
        fields = ['name', 'amount', 'frequency', 'start_date', 'next_due_date']




class ImageUploadForm(forms.Form):
    image = forms.ImageField()



class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['amount', 'source'] 