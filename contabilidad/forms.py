from django import forms

from .models import Transaccion

class IntegerCurrencyInput(forms.TextInput):
    def render(self, name, value, attrs=None):
        from django.contrib.humanize.templatetags.humanize import intcomma
        if value:
            value = "$%s" % intcomma(value)
        return super(IntegerCurrencyInput, self).render(name, value, attrs)

class IntegerCurrencyField(forms.IntegerField):
    widget = IntegerCurrencyInput

    def clean(self, value):
        if value:
            if value[0] == "$": value = value[1:] # Cut off the dollar sign
            value = value.replace(',', '') # Remove Commas
        value = super(IntegerCurrencyField, self).clean(value)
        return int(value) if value else value


class TransaccionForm(forms.ModelForm):
    class Meta:
        model = Transaccion
        fields = ['tipo_transaccion','consumidor', 'monto', 'nombre_entrada', 'fecha', 'descripcion']
        widgets = {
            'tipo_transaccion': forms.Select(attrs={'class': 'form-control col-md-7 col-xs-12"'}),
            'consumidor': forms.Select(attrs={'class': 'form-control col-md-7 col-xs-12"'}),
            'monto': forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12', 'pattern': '[0-9]*'}),
            #'nombre_entrada': forms.Select(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'id': 'birthday', 'class': 'date-picker form-control col-md-7 col-xs-12"'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control col-md-7 col-xs-12"', 'style': 'height: 90px;'}),

        }


