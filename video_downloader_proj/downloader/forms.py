from django import forms


class LinkTitleForm(forms.Form):
    title = forms.URLField()
