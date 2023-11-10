from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Customer

GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
]

MATERIALS_PROVIDED_CHOICES = [
    ('Debit card', 'Debit card'),
    ('Credit card', 'Credit card'),
    ('Cheque book', 'Cheque book'),
]
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        # Username field
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields[
            'username'].help_text = '<span class="form-text text-muted"><small><li><strong>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</strong></li></small></span>'

        # Password1 field
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields[
            'password1'].help_text = '<ul class="form-text text-muted small"><li><strong>Your password can\'t be too similar to your other personal information.</strong></li><li><strong>Your password must contain at least 8 characters.</strong></li><li><strong>Your password can\'t be a commonly used password.</strong></li><li><strong>Your password can\'t be entirely numeric.</strong></li></ul>'

        # Password2 field
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields[
            'password2'].help_text = '<span class="form-text text-muted"><small><li><strong>Enter the same password as before, for verification.</strong></li></small></span>'


class CustomerForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    materials_provided = forms.MultipleChoiceField(choices=MATERIALS_PROVIDED_CHOICES, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Customer
        fields = ['id', 'name', 'dob', 'age', 'gender', 'phone_number', 'email', 'address', 'district', 'branch', 'account_type', 'materials_provided']
        labels = {
            'name': 'Full Name',
            'dob': 'Date of Birth',
            'age': 'Age',
            'gender': 'Gender',
            'phone_number': 'Phone Number',
            'email': 'Email ID',
            'address': 'Address',
            'district': 'District',
            'branch': 'Branch',
            'account_type': 'Account Type',
            'materials_provided': 'Materials Provided',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'dob': forms.DateInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'district': forms.Select(attrs={'class': 'form-control'}),
            'branch': forms.Select(attrs={'class': 'form-control'}),
            'account_type': forms.Select(attrs={'class': 'form-control'}),
        }