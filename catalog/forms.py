from django import forms
from .models import Product
from django.core.exceptions import ValidationError

FORBIDDEN_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа',
                   'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Стилизация полей формы
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field_name == 'is_published':
                field.widget.attrs['class'] = 'form-check-input'

    def clean_name(self):
        name = self.cleaned_data['name'].lower()
        for word in FORBIDDEN_WORDS:
            if word in name:
                raise ValidationError(f'Название содержит запрещенное слово: {word}')
        return self.cleaned_data['name']

    def clean_description(self):
        description = self.cleaned_data['description'].lower()
        for word in FORBIDDEN_WORDS:
            if word in description:
                raise ValidationError(f'Описание содержит запрещенное слово: {word}')
        return self.cleaned_data['description']

    def clean_price(self):
        price = self.cleaned_data['price']
        if price < 0:
            raise ValidationError('Цена не может быть отрицательной')
        return price

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            if image.size > 5 * 1024 * 1024:  # 5MB
                raise ValidationError('Размер файла не должен превышать 5 МБ')
            if not image.name.lower().endswith(('.jpg', '.jpeg', '.png')):
                raise ValidationError('Поддерживаются только JPG/JPEG и PNG файлы')
        return image
