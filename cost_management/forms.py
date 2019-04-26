from django import forms
from .models import Expense
#from .models import Expense2

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'
		
#class Expense2Form(forms.ModelForm):
 #   class Meta:
  #      model = Expense2
   #     fields = '__all__'