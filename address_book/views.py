from django.contrib.auth import login
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .forms import AddressForm
from core.models import Address
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def index(request):
    return render(request, "address_book/index.html")

@login_required
def add_address(request):
    if request.method != 'POST':
        form = AddressForm()
    else:
        form = AddressForm(data=request.POST)

        if form.is_valid():
            new_address = form.save(commit=False)
            new_address.owner = request.user
            new_address.save()
            return HttpResponseRedirect(reverse("address_book:show-addresses"))


    context = {"form": form}
    return render(request, 'address_book/add_address.html', context)

@login_required
def show_addresses(request):
    addresses = Address.objects.all()
    context = {'addresses': addresses}
    return render(request, 'address_book/show_addresses.html', context)

@login_required
def update_address(request, address_id):
    address = Address.objects.get(id=address_id)
    if request.method != "POST":
        form = AddressForm(instance=address)
    else:
        form = AddressForm(instance=address, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('address_book:show-addresses'))

    context = {'form': form, 'address':address}
    return render(request, 'address_book/update_address.html', context)

@login_required
def delete_address(request, address_id):
    address = Address.objects.get(id=address_id)
    address.delete()
    return HttpResponseRedirect(reverse('address_book:show-addresses'))