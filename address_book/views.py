from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .forms import AddressForm
from core.models import Address
from django.urls import reverse
# Create your views here.
def index(request):
    return render(request, "address_book/index.html")

def add_address(request):
    if request.method != 'POST':
        form = AddressForm()
    else:
        form = AddressForm(data=request.POST)

        if form.is_valid():
            form.save()
            form = AddressForm()

    context = {"form": form}
    return render(request, 'address_book/add_address.html', context)

def show_addresses(request):
    addresses = Address.objects.all()
    context = {'addresses': addresses}
    return render(request, 'address_book/show_addresses.html', context)


def update_address(request, address_id):
    address = Address.objects.get(id=address_id)
    if request != "POST":
        form = AddressForm(instance=address)
    else:
        form = AddressForm(instance=address, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('address_book:show-addresses', args=[address.id]))

    context = {'form': form}
    return render(request, 'address_book/update_address.html', context)


def delete_address(request, address_id):
    address = Address.objects.get(id=address_id)
    address.delete()
    return HttpResponseRedirect(reverse('address_book:show-addresses'))