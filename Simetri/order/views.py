from django.shortcuts import render
from django import forms

class ProductSearchForm (forms.Form):
    product=forms.CharField(label="Search Product")

# Create your views here.
def index(request):
    if request.method=="POST":
        form=ProductSearchForm(request.POST)
        if form.is_valid:
            product=form.cleaned_data["product"]
            products=["tk3100","pk3010","mpc2503"]
            if product in products:
                return render(request, "order/index.html",{"product" :product})
            else:
                return render(request, "order/index.html",{"form" :form})
    return render(request, "order/index.html",{"product" :ProductSearchForm()})





    