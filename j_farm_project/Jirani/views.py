from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import UserForm, FarmerForm, TractorForm, LeaseForm
from .models import Tractor, Lease


# Create your views here.

def index(request):
    return render(request, 'jirani/templates/index.html')


def register(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        farmer_form = FarmerForm(request.POST)
        if user_form.is_valid() and farmer_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            farmer = farmer_form.save(commit=False)
            farmer.user = user
            farmer.save()
            messages.success(request, 'Registration successful.')
            return redirect('jirani:login')
        else:
            messages.error(request, 'Registration failed.')
            return render(request, 'jirani/templates/register.html', {'user_form': user_form, 'farmer_form': farmer_form})
    else:
        user_form = UserForm()
        farmer_form = FarmerForm()
        return render(request, 'jirani/templates/register.html', {'user_form': user_form, 'farmer_form': farmer_form})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('jirani:index')
        else:
            messages.error(request, 'Login failed.')
            return render(request, 'jirani/templates/login.html')
    else:
        return render(request, 'jirani/templates/login.html')


@login_required
def logout_user(request):
    logout(request)
    messages.success(request, 'Logout successful.')
    return redirect('jirani:index')


@login_required
def profile(request):
    farmer = request.user.farmer
    return render(request, 'jirani/templates/profile.html', {'farmer': farmer})


@login_required
def tractors(request):
    query = request.GET.get('q')
    if query:
        tractors = Tractor.objects.filter(model__icontains=query, available=True)
    else:
        tractors = Tractor.objects.filter(available=True)
    return render(request, 'jirani/templates/tractors.html', {'tractors': tractors})


@login_required
def tractor_detail(request, tractor_id):
    tractor = get_object_or_404(Tractor, id=tractor_id)
    return render(request, 'jirani/templates/tractor_detail.html', {'tractor': tractor})


@login_required
def add_tractor(request):
    if request.method == 'POST':
        tractor_form = TractorForm(request.POST)
        if tractor_form.is_valid():
            tractor = tractor_form.save(commit=False)
            tractor.owner = request.user.farmer
            tractor.save()
            messages.success(request, 'Tractor added.')
            return redirect('jirani:tractors')
        else:
            messages.error(request, 'Tractor not added.')
            return render(request, 'jirani/templates/add_tractor.html', {'tractor_form': tractor_form})
    else:
        tractor_form = TractorForm()
        return render(request, 'jirani/templates/add_tractor.html', {'tractor_form': tractor_form})


@login_required
def edit_tractor(request, tractor_id):
    tractor = get_object_or_404(Tractor, id=tractor_id)
    if request.user.farmer == tractor.owner:
        if request.method == 'POST':
            tractor_form = TractorForm(request.POST, instance=tractor)
            if tractor_form.is_valid():
                tractor_form.save()
                messages.success(request, 'Tractor updated.')
                return redirect('jirani:tractors')
            else:
                messages.error(request, 'Tractor not updated.')
                return render(request, 'jirani/templates/edit_tractor.html', {'tractor_form': tractor_form})
        else:
            tractor_form = TractorForm(instance=tractor)
            return render(request, 'jirani/templates/edit_tractor.html', {'tractor_form': tractor_form})
    else:
        messages.error(request, 'You are not authorized to edit this tractor.')
        return redirect('jirani:tractors')


@login_required
def delete_tractor(request, tractor_id):
    tractor = get_object_or_404(Tractor, id=tractor_id)
    if request.user.farmer == tractor.owner:
        if request.method == 'POST':
            tractor.delete()
            messages.success(request, 'Tractor deleted.')
            return redirect('jirani:tractors')
        else:
            return render(request, 'jirani/templates/delete_tractor.html', {'tractor': tractor})
    else:
        messages.error(request, 'You are not authorized to delete this tractor.')
        return redirect('jirani:tractors')


@login_required
def leases(request):
    leases = Lease.objects.filter(renter=request.user.farmer) | Lease.objects.filter(tractor__owner=request.user.farmer)
    return render(request, 'jirani/templates/leases.html', {'leases': leases})


@login_required
def lease_detail(request, lease_id):
    lease = get_object_or_404(Lease, id=lease_id)
    if request.user.farmer == lease.renter or request.user.farmer == lease.tractor.owner:
        return render(request, 'jirani/templates/lease_detail.html', {'lease': lease})
    else:
        messages.error(request, 'You are not authorized to view this lease.')
        return redirect('jirani:leases')


@login_required
def create_lease(request, tractor_id):
    tractor = get_object_or_404(Tractor, id=tractor_id)
    if request.user.farmer != tractor.owner and tractor.available:
        if request.method == 'POST':
            lease_form = LeaseForm(request.POST)
            if lease_form.is_valid():
                lease = lease_form.save(commit=False)
                lease.tractor = tractor
                lease.renter = request.user.farmer
                lease.save()
                messages.success(request, 'Lease created.')
                return redirect('jirani:leases')
            else:
                messages.error(request, 'Lease not created.')
                return render(request, 'jirani/templates/create_lease.html', {'lease_form': lease_form})
        else:
            lease_form = LeaseForm()
            return render(request, 'jirani/templates/create_lease.html', {'lease_form': lease_form})
    else:
        messages.error(request, 'You cannot lease this tractor.')
        return redirect('jirani:tractors')


@login_required
def cancel_lease(request, lease_id):
    lease = get_object_or_404(Lease, id=lease_id)
    if request.user.farmer == lease.renter and lease.status == 'pending':
        if request.method == 'POST':
            lease.status = 'cancelled'
            lease.save()
            messages.success(request, 'Lease cancelled.')
            return redirect('jirani:leases')
        else:
            return render(request, 'jirani/templates/cancel_lease.html', {'lease': lease})
    else:
        messages.error(request, 'You cannot cancel this lease.')
        return redirect('jirani:leases')


@login_required
def confirm_lease(request, lease_id):
    lease = get_object_or_404(Lease, id=lease_id)
    if request.user.farmer == lease.tractor.owner and lease.status == 'pending':
        if request.method == 'POST':
            lease.status = 'confirmed'
            lease.tractor.available = False
            lease.save()
            lease.tractor.save()
            messages.success(request, 'Lease confirmed.')
            return redirect('jirani:leases')
        else:
            return render(request, 'jirani/templates/confirm_lease.html', {'lease': lease})
    else:
        messages.error(request, 'You cannot confirm this lease.')
        return redirect('jirani:leases')


@login_required
def complete_lease(request, lease_id):
    lease = get_object_or_404(Lease, id=lease_id)
    if request.user.farmer == lease.tractor.owner and lease.status == 'confirmed':
        if request.method == 'POST':
            lease.status = 'completed'
            lease.tractor.available = True
            lease.save()
            lease.tractor.save()
            messages.success(request, 'Lease completed.')
            return redirect('jirani:leases')
        else:
            return render(request, 'jirani/templates/complete_lease.html', {'lease': lease})
    else:
        messages.error(request, 'You cannot complete this lease.')
        return redirect('jirani:leases')
