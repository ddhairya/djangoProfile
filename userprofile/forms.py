from django.forms import ModelForm
from .models import userprofile


# Create the form class.
class ProfileForm(ModelForm):
    class Meta:
        model = userprofile
        fields = '__all__'

