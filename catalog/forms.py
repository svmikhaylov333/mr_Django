from django.forms import ModelForm
from django.core.exceptions import ValidationError
from catalog.models import Product

FORBIDDEN_WORDS = ["казино", "криптовалюта",
                   "крипта", "биржа", "дешево",
                   "бесплатно", "обман", "полиция", "радар",]
class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['description', 'price', 'category', 'image']

        # fields = "__all__"
        # exclude = ('name',)

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Заполните описание'
        })
        self.fields['price'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Укажите цену',
        })

        self.fields['category'].widget.attrs.update({
            'class': 'form-select',
        })

        self.fields['image'].widget.attrs.update({
            'class': 'form-control',
        })
        # Добавление красной рамки при ошибке
        for field_name, field in self.fields.items():
            if self.errors.get(field_name):
                field.widget.attrs['class'] += ' is-invalid'

    def clean_description(self):
        description = self.cleaned_data.get('description')
        found = [w for w in FORBIDDEN_WORDS if w.lower() in description.lower()]
        if found:
            raise ValidationError(f'Описание содержит запрещенные слова: {",".join(found)}')
        return description

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise ValidationError('Цена не может быть отрицательной.')
        return price