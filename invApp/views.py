from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product


# Create your views here.
#this application is applying CRUD, Create, Read/View, Update, Delete product
#Home View
def home_view(request):
  return render(request, 'invApp/home.html')

#Create View
def product_create_view(request):
  form = ProductForm()
  if request.method == 'POST':
    form = ProductForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('invApp:product_list')
    # else:
    #   form = ProductForm()
  return render(request, 'invApp/product_form.html', { 'form':form })

#Read/View View
def product_list_view(request):
  products = Product.objects.all()
  return render(request, 'invApp/product_list.html', { 'products':products })

def update_confirm_view(request, product_id):
  # product_id = request.GET.get('id')
  product = Product.objects.get(product_id=product_id)
  return render(request, 'invApp/update_confirm.html', { 'product':product })

#Update View
def product_update_view(request, product_id):
  product = Product.objects.get(product_id=product_id)
  form = ProductForm()
  if request.method == "POST":
    form = ProductForm(request.POST, instance=product)
    if form.is_valid():
      form.save()
      return redirect('invApp:product_list')
  return render(request, 'invApp/product_form.html', {'form':form})

#Delete View
def product_delete_view(request, product_id):
  product = Product.objects.get(product_id=product_id)
  if request.method == "POST":
    product.delete()
    return redirect('invApp:delete_success')
  return render(request, 'invApp/product_confirm_delete.html', { 'product':product })
# Delete success
def delete_success_view(request, product_id):
  product = Product.objects.get(product_id=product_id)
  return render(request, 'invApp/delete_success.html', { 'product':product })
