
from django.shortcuts import render

def process_form(request):
    if request.method == 'POST':
        field1 = request.POST.get('field1')
        field2 = request.POST.get('field2')
        field3 = request.POST.get('field3')
        return render(request, 'result_template.html', {'field1': field1, 'field2': field2, 'field3': field3})

    
    return render(request, 'index.html')

