from django import forms
from test_captcha.models import Submission
from puzzle_captcha.fields import PuzzleCaptchaField


class SubmissionForm(forms.ModelForm):
    captcha = PuzzleCaptchaField()

    class Meta:
        model = Submission
        fields = '__all__'
