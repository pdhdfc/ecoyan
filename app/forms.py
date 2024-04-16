from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)
    email = forms.EmailField(label='Your Email')
    phone = forms.CharField(label='Your Phone', max_length=20)
    message = forms.CharField(label='Your Message', widget=forms.Textarea)
