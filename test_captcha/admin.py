from django.contrib import admin
from test_captcha.models import Submission


class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'comments', 'submission_date')

    class Meta:
        model = Submission


admin.site.register(Submission, SubmissionAdmin)