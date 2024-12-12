from django import forms

from application.models import Customer, ContactRequest


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'phoneNumber': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'}),
            'gender': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Gender'}),
            'date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your preferred date'}),
            'location': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter your Current location'})
        }



class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactRequest
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Email'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control','placeholder': 'Enter your message','name':"message"}),
        }