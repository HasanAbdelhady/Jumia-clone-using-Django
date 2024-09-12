from django import forms
from products.models import Product

class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg'
            })
    class Meta:
        model = Product
        fields = '__all__'


    def clean_name(self):
        name = self.cleaned_data["name"]
        if len(name) < 3:
            raise forms.ValidationError("Name must be at least 3 characters")
        return name
    
    # name = forms.CharField(label="Name", max_length=100, required=True)
    # category = forms.ModelChoiceField(
    #     queryset=Category.objects.all(),
    #     widget=forms.Select(attrs={"class": "form-control"}),
    # )
    # price = forms.IntegerField(label="Price")
    # description = forms.CharField(label="Description", required=False, max_length=300)
    # image=  forms.ImageField(label="Image", required=False)
    # rating = forms.FloatField(label="Rating", min_value=0, max_value=5)
    # in_stock = forms.BooleanField(required=False)
