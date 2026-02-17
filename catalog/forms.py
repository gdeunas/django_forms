from django import forms
from django.core.exceptions import ValidationError

from .models import Product


class ProductForm(forms.ModelForm):
    BANNED_WORDS = ['казино', 'биржа', 'обман', 'криптовалюта', 'дешево', 'полиция', 'крипта', 'бесплатно', 'радар']

    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'price', ]

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите название'})
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите описание'})
        self.fields['image'].widget.attrs.update({'class': 'form-control', })
        self.fields['category'].widget.attrs.update({'class': 'form-control'})
        self.fields['price'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите цену'})

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise ValidationError('Цена продукта не может быть отрицательной.')
        return price

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            max_size = 5 * 1024 * 1024
            if image.size > max_size:
                raise ValidationError('Размер файла не должен превышать 5 МБ.')

            allowed_extensions = ['jpeg', 'png']
            extension = image.name.split('.')[-1].lower()
            if extension not in allowed_extensions:
                raise ValidationError("Допустимые форматы файлов: JPEG, PNG.")
        return image

    def validate_banned_words(self, value):
        if value:
            lower_value = value.lower()
            for word in self.BANNED_WORDS:
                if word in lower_value:
                    raise ValidationError(f"Использование слова '{word}' запрещено.")

    def clean_name(self):
        name = self.cleaned_data.get('name')
        self.validate_banned_words(name)
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        self.validate_banned_words(description)
        return description
