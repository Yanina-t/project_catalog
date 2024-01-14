from django import forms
from django.core.exceptions import ValidationError

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                       'радар']

    class Meta:
        model = Product
        fields = ('name', 'description', 'image_preview', 'purchase_price', 'date_of_creation', 'parent_category')

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        if not self.request.user.is_staff:
            self.fields['parent_category'].widget = forms.HiddenInput()

    def clean_name(self):
        name = self.cleaned_data.get('name', '')
        for word in self.forbidden_words:
            if word.lower() in name.lower():
                raise ValidationError(f'Слово «{word}» не допускается в наименовании товара.')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description', '')
        for word in self.forbidden_words:
            if word.lower() in description.lower():
                raise ValidationError(f'Слово «{word}» не допускается в описании товара.')
        return description


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = ('name', 'version_number', 'version_name', 'is_current',)
