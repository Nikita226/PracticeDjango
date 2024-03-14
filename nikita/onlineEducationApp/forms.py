from django.forms import ModelForm
from .models import Data, Subject

class DataForm(ModelForm):
    class Meta:
        model = Data
        fields = "__all__"


class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = "__all__"
