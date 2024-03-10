
from website.models import NewsLetter, Contact
from django import forms


# from captcha.fields import CaptchaField
from django import forms

from website.models import NewsLetter, Contact



class ContactForm(forms.ModelForm):
    # captcha = CaptchaField()
    class Meta:
        model = Contact
        fields = '__all__'


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsLetter
        fields = '__all__'
