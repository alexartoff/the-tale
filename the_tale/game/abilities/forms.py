# coding: utf-8

from dext.forms import forms, fields

class AbilityForm(forms.Form):

    angel_id = fields.HiddenIntegerField()
    hero_id = fields.HiddenIntegerField()
