from django import forms
from .models import *

class contactForm(forms.Form):
    name=forms.CharField(required=True)
    email=forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea,required=True)
    
    
class ordersform(forms.Form):
    name = forms.CharField(required=True)
    phone_no = forms.IntegerField(required=True)
    address = forms.CharField(required=True)
    m_name = forms.CharField(required=True)
    qty = forms.IntegerField(required=True)
    
# class medicinefrom(forms.models):
#     # id=forms.AutoField(primary_key=True)
#     name=forms.CharField(max_length=50)
#     brand=forms.CharField(max_length=60)
#     pic=forms.ImageField(upload_to='upload',default=None,blank=True,null=True)
#     price=forms.IntegerField()
#     discount=forms.IntegerField()
#     finalprice=forms.IntegerField()
#     quantity=forms.IntegerField()

class MedicineForm(forms.ModelForm):
    class Meta:
        model = medicine
        fields = ['name', 'brand', 'pic', 'price', 'discount', 'quantity','finalprice']
        
    def clean_finalprice(self):
        price = self.cleaned_data.get('price')
        discount = self.cleaned_data.get('discount')
        if price is not None and discount is not None:
            return price - (price * discount / 100)
        return None