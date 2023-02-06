from django import forms
from .models import *

class ProductForm(forms.Form): #ฟอร์มอิสระ
    # BRAND_LIST = [('mama','mama thailand'),('yumyum','yumyum thailand'),('samyang','samyang korean')]
    # TYPE_LIST = [('piece','per piece'),('pack','per pack'),('box','per box')]
    # FLAVOR_RADIO = [('spisy','spisy'),('cheesy','cheesy'),('original','original')]
    # MEM_RADIO = [('yes', 'yes'), ('no', 'no')]
    # id = forms.CharField(max_length=13, label="product id", required=True, widget=forms.TextInput(attrs={'size':'15'}))
    # name = forms.CharField(max_length=50, label="product name", required=True,widget=forms.TextInput(attrs={'size': '55'}))
    # brand = forms.CharField(max_length=30, label="product brand", required=True,widget=forms.Select(choices=BRAND_LIST))
    # type = forms.CharField(max_length=30, label="product type", required=True,widget=forms.Select(choices=TYPE_LIST))
    # flavor = forms.RadioSelect = forms.ChoiceField(widget=forms.RadioSelect, choices = FLAVOR_RADIO)
    # amount = forms.IntegerField(min_value=0, max_value=1000,label="net",
    #                          required=True,widget=forms.NumberInput(attrs={'size': '10'}))
    # price = forms.FloatField(min_value=1.00, max_value=100000.00, label="price",
    #                          required=True, widget=forms.TextInput(attrs={'size': '10'}))
    # # member = forms.RadioSelect = forms.ChoiceField(widget=forms.RadioSelect, choices = MEM_RADIO)
    # # member = forms.ChoiceField(widget=forms.RadioSelect, choices=MEM_RADIO)
    # discount = forms.FloatField(min_value=1.00, max_value=100000.00, label="price",
    #                          required=True, widget=forms.TextInput(attrs={'size': '10'}))
    # total = forms.FloatField(min_value=1.00, max_value=100000.00, label="price",
    #                          required=True, widget=forms.TextInput(attrs={'size': '10'}))

    BRAND_LIST = [('mama', 'mama thailand'), ('yumyum', 'yumyum thailand'), ('samyang', 'samyang korean')]
    MEMBER_LIST = (('yes', 'yes'), ('no', 'no'))
    TYPE_LIST = [('piece', 'per piece'), ('pack', 'per pack'), ('box', 'per box')]
    FLAVOR_RADIO = [('spisy', 'spisy'), ('cheesy', 'cheesy'), ('original', 'original')]

    id = forms.CharField()
    name = forms.CharField()
    brand = forms.ChoiceField(widget=forms.Select, choices=BRAND_LIST)
    type = forms.ChoiceField(widget=forms.Select, choices=TYPE_LIST)
    flavor = forms.ChoiceField(widget=forms.Select, choices=FLAVOR_RADIO)
    amount = forms.IntegerField(min_value=0)
    price = forms.IntegerField(min_value=0)
    member = forms.ChoiceField(widget=forms.RadioSelect, choices=MEMBER_LIST)

class ProductMForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('pid', 'name', 'brand', 'price', 'net', 'category')
        widgets = {
            'pid': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': 'required', 'max_length': 35}),
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'net': forms.NumberInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
        lables = {
            'pid': 'id',
            'name': 'name',
            'brand': 'brand',
            'price': 'price',
            'net': 'net',
            'category': 'category'
        }
    def updateForm(self):
        self.fields['pid'].widget.attrs['randonly'] = True
        self.fields['pid'].lable = 'รหัส [ไม่อนุญาตให้แก้ไข]'





class ProductUpdateMForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('pid', 'name', 'brand', 'price', 'net', 'category')
        widgets = {
            'pid': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': 'required', 'max_length': 35}),
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'net': forms.NumberInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
        lables = {
            'pid': 'id',
            'name': 'name',
            'brand': 'brand',
            'price': 'price',
            'net': 'net',
            'category': 'category'
        }


class EmployeeForm(forms.ModelForm): #ฟอมที่มาจากคลาสโมเดล
    class Meta:
        model = testEmployee
        fields = ('empid', 'name', 'address', 'status', 'email', 'salary', 'gender', 'birthday', 'born', 'marries')
        GENDER_CHOICES = [('M', 'Male'), ('F', 'Female')]
        STATUS_CHOICES = [('Administrator', 'Administrator'), ('Manager', 'Manager'), ('Staff', 'Staff'), ('Sale Rep','Sale Rep')]
        BORN_CHOICE = [('North', 'ภาคเหนือ'), ('Middle', 'ภาคกลาง'), ('ภาคอีสาน', 'Northeast'), ('ภาคใต้', 'South'),('ภาคตะวันออก', 'East')]
        widgets = {
            'empid': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'status': forms.Select(attrs={'class': 'form-control'}, choices=STATUS_CHOICES),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control', 'Min': '5000'}),
            'gender': forms.RadioSelect(attrs={'class': 'form-control form-inline'}, choices=GENDER_CHOICES, ),
            'birthday': forms.NumberInput(attrs={'class': 'form-control', 'type': 'date'}),
            'born': forms.RadioSelect(attrs={'class': 'form-control form-inline'}, choices=BORN_CHOICE),
            'marries': forms.CheckboxInput(attrs={'checked': 'checked'})
        }