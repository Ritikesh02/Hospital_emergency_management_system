


from django.shortcuts import render, get_object_or_404, redirect
from .models import MedicalRecord
from .forms import MedicalRecordForm

def view_records(request):
    records = MedicalRecord.objects.all()
    return render(request, 'medical_records/view_records.html', {'records': records})

def upload_record(request):
    if request.method == 'POST':
        form = MedicalRecordForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_records')
    else:
        form = MedicalRecordForm()
    
    return render(request, 'medical_records/upload_record.html', {'form': form})


def edit_record(request, record_id):
    template_name = 'medical_records/edit_record.html'
    record = get_object_or_404(MedicalRecord, id=record_id)

    # Check if the template exists
    try:
        return render(request, template_name)
    except:
        return render(request, 'medical_records/template_not_found.html', {'missing_template': template_name})

    if request.method == 'POST':
        form = MedicalRecordForm(request.POST, request.FILES, instance=record)
        if form.is_valid():
            form.save()
            return redirect('view_records')
    else:
        form = MedicalRecordForm(instance=record)
    return render(request, template_name, {'form': form, 'record': record})

from django.shortcuts import render, get_object_or_404, redirect
from .models import MedicalRecord

def delete_record(request, record_id):
    record = get_object_or_404(MedicalRecord, id=record_id)
    
    if request.method == "POST":
        record.delete()
        return redirect("view_records")  # Redirect after deleting
    
    return render(request, "medical_records/delete_record.html", {"record": record})
