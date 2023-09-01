from django import forms
from .models import VideoText

class VideoTextForm(forms.ModelForm):
    class Meta:
        model = VideoText
        fields = ['text']
