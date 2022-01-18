from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Drug, Order
from .forms import DrugForm, OrderForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import auth_users, allowed_users
# Create your views here.


@login_required(login_url='user-login')
def index(request):
    drug = Drug.objects.all()
    drug_count = drug.count()
    order = Order.objects.all()
    order_count = order.count()
    customer = User.objects.filter(groups=2)
    customer_count = customer.count()

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.customer = request.user
            obj.save()
            return redirect('pharm-index')
    else:
        form = OrderForm()
    context = {
        'form': form,
        'order': order,
        'drug': drug,
        'drug_count': drug_count,
        'order_count': order_count,
        'customer_count': customer_count,
    }
    return render(request, 'pharm/index.html', context)


@login_required(login_url='user-login')
def drugs(request):
    drug = Drug.objects.all()
    drug_count = drug.count()
    customer = User.objects.filter(groups=2)
    customer_count = customer.count()
    order = Order.objects.all()
    order_count = order.count()
    drug_quantity = Drug.objects.filter(name='')
    if request.method == 'POST':
        form = DrugForm(request.POST)
        if form.is_valid():
            form.save()
            drug_name = form.cleaned_data.get('name')
            messages.success(request, f'{drug_name} has been added')
            return redirect('pharm-drugs')
    else:
        form = DrugForm()
    context = {
        'drug': drug,
        'form': form,
        'customer_count': customer_count,
        'drug_count': drug_count,
        'order_count': order_count,
    }
    return render(request, 'pharm/drugs.html', context)


@login_required(login_url='user-login')
def drug_detail(request, pk):
    context = {

    }
    return render(request, 'pharm/drugs_detail.html', context)


@login_required(login_url='user-login')
@allowed_users(allowed_roles=['Admin'])
def customers(request):
    customer = User.objects.filter(groups=2)
    customer_count = customer.count()
    drug = Drug.objects.all()
    drug_count = drug.count()
    order = Order.objects.all()
    order_count = order.count()
    context = {
        'customer': customer,
        'customer_count': customer_count,
        'drug_count': drug_count,
        'order_count': order_count,
    }
    return render(request, 'pharm/customers.html', context)


@login_required(login_url='user-login')
@allowed_users(allowed_roles=['Admin'])
def customer_detail(request, pk):
    customer = User.objects.filter(groups=2)
    customer_count = customer.count()
    drug = Drug.objects.all()
    drug_count = drug.count()
    order = Order.objects.all()
    order_count = order.count()
    customers = User.objects.get(id=pk)
    context = {
        'customers': customers,
        'customer_count': customer_count,
        'drug_count': drug_count,
        'order_count': order_count,

    }
    return render(request, 'pharm/customers_detail.html', context)


@login_required(login_url='user-login')
@allowed_users(allowed_roles=['Admin'])
def drug_edit(request, pk):
    item = Drug.objects.get(id=pk)
    if request.method == 'POST':
        form = DrugForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('pharm-drugs')
    else:
        form = DrugForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'pharm/drugs_edit.html', context)


@login_required(login_url='user-login')
@allowed_users(allowed_roles=['Admin'])
def drug_delete(request, pk):
    item = Drug.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('pharm-drugs')
    context = {
        'item': item
    }
    return render(request, 'pharm/drugs_delete.html', context)


@login_required(login_url='user-login')
def order(request):
    order = Order.objects.all()
    order_count = order.count()
    customer = User.objects.filter(groups=2)
    customer_count = customer.count()
    drug = Drug.objects.all()
    drug_count = drug.count()

    context = {
        'order': order,
        'customer_count': customer_count,
        'drug_count': drug_count,
        'order_count': order_count,
    }
    return render(request, 'pharm/order.html', context)
