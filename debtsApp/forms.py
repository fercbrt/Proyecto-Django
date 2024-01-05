from django import forms

from debtsApp.models import Debt, Debtor

class DebtorForm(forms.ModelForm):
    SEX_CHOICE = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    name = forms.CharField()
    surname = forms.CharField()
    sex = forms.ChoiceField(widget=forms.RadioSelect, choices=SEX_CHOICE)
    address = forms.CharField()

    class Meta:
        model = Debtor
        fields = ['name', 'surname', 'sex', 'address']

class DebtForm(forms.ModelForm):
    class Meta:
        model = Debt
        fields = ['reason', 'amount']
        widgets = {
            'debtor': forms.HiddenInput()
        }