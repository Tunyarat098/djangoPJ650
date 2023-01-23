from django import forms
class ProductForm(forms.Form):
    BRAND_LIST = [('mama','mama thailand'),('yumyum','yumyum thailand')]
    id = forms.CharField(max_length=13, label=" product id", required=True, widget=forms.TextInput(attrs={'size':'15'}))
    name = forms.CharField(max_length=50, label=" product name", required=True,widget=forms.TextInput(attrs={'size': '55'}))
    brand = forms.CharField(max_length=30, label=" product brand", required=True,widget=forms.Select(choices=BRAND_LIST))
    price = forms.FloatField(min_value=1.00, max_value=100000.00, label="price",
                             required=True,widget=forms.NumberInput(attrs={'size': '10'}))
    net = forms.IntegerField(min_value=0, max_value=1000,label="net",
                             required=True,widget=forms.NumberInput(attrs={'size': '10'}))