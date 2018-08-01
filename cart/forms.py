from django import forms
from backend.models import Book


class CartAddBookForm(forms.Form):
    update=forms.BooleanField(required=False,initial=False,widget=forms.HiddenInput)

    def __init__(self,*args,**kwargs):
        id=kwargs.pop("id")
        super(CartAddBookForm,self).__init__(*args,**kwargs)
        self.fields['quantity']=forms.TypedChoiceField(choices=[(i,str(i)) for i in range(1,Book.objects.get(id=id).stock+1)],coerce=int)
