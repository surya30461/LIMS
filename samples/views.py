from django.shortcuts import render, get_object_or_404, redirect
from django_otp.decorators import otp_required  # Import the MFA decorator
from .models import Sample
from .forms import SampleForm
from django.db.models import Q  # For advanced filtering

# View to list all samples
def sample_list(request):
    query = request.GET.get('q')  # Retrieve the 'q' parameter from the request
    if query:
        samples = Sample.objects.filter(
            Q(name__icontains=query) | Q(sample_type__icontains=query)  # Search by name or type
        )
    else:
        samples = Sample.objects.all()  # Show all samples if no query
    return render(request, 'samples/sample_list.html', {'samples': samples})

# View to see details of a specific sample
@otp_required  # Enforce MFA for viewing sample details
def sample_detail(request, pk):
    sample = get_object_or_404(Sample, pk=pk)
    return render(request, 'samples/sample_detail.html', {'sample': sample})

# View to create a new sample
@otp_required  # Enforce MFA for creating a new sample
def sample_create(request):
    if request.method == 'POST':
        form = SampleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sample_list')
    else:
        form = SampleForm()
    return render(request, 'samples/sample_form.html', {'form': form})

# View to update an existing sample
@otp_required  # Enforce MFA for updating a sample
def sample_update(request, pk):
    sample = get_object_or_404(Sample, pk=pk)
    if request.method == 'POST':
        form = SampleForm(request.POST, instance=sample)
        if form.is_valid():
            form.save()
            return redirect('sample_list')
    else:
        form = SampleForm(instance=sample)
    return render(request, 'samples/sample_form.html', {'form': form})

# View to delete a sample
@otp_required  # Enforce MFA for deleting a sample
def sample_delete(request, pk):
    sample = get_object_or_404(Sample, pk=pk)
    if request.method == 'POST':
        sample.delete()
        return redirect('sample_list')
    return render(request, 'samples/sample_confirm_delete.html', {'sample': sample})
