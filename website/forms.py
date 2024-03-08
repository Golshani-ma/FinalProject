<<<<<<< HEAD
from website.models import NewsLetter, Contact
from django import forms

=======
# from captcha.fields import CaptchaField
from django import forms

from website.models import NewsLetter, Contact

>>>>>>> origin/master

class ContactForm(forms.ModelForm):
    # captcha = CaptchaField()
    class Meta:
        model = Contact
        fields = '__all__'

<<<<<<< HEAD

=======
>>>>>>> origin/master
class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsLetter
        fields = '__all__'
