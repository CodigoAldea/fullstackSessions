from django.shortcuts import render, redirect
from exptracker.models import expense

def home(request):
    data = expense.objects.all()
   
    total = sum(i.amount for i in data)
    
    cat = expense.CATEGORY_CHOICES
    if request.method == 'POST':
        category = request.POST.get('category')
        description = request.POST.get('description')
        amount = request.POST.get('amount')
        
        expense.objects.create(
            category= category,
            description = description,
            amount= amount
        )
        return render(request, 'home.html', {'data' : data, 'total': total, 'cat': cat})
    return render(request, 'home.html', {'data' : data, 'total': total, 'cat': cat})


# view for deletion 
def deleteexp(request, id):
    data = expense.objects.get(id=id)
    data.delete()
    return redirect('home')