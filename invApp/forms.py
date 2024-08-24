from django import forms
from .models import Product


#create the form
class ProductForm(forms.ModelForm):
  class Meta:
    model = Product
    fields ='__all__'
    lables = {
      'product_id':'Product ID',
      'product_name':'Product Name',
      'sku':'SKU',
      'price':'Price',
      'quantity':'Quantity',
      'supplier':'Supplier',
    }
    widgets = {
      'product_id':forms.NumberInput(attrs={'placeholder':'eg. 1', 'class':'form-control'}),
      'product_name':forms.TextInput(attrs={'placeholder':'eg. Shirt', 'class':'form-control'}),
      'sku':forms.TextInput(attrs={'placeholder':'eg. W1234', 'class':'form-control'}),
      'price':forms.NumberInput(attrs={'placeholder':'eg. 25.45', 'class':'form-control'}),
      'quantity':forms.NumberInput(attrs={'placeholder':'eg. 25', 'class':'form-control'}),
      'supplier':forms.TextInput(attrs={'placeholder':'eg. Soko LTD', 'class':'form-control'}),

    }