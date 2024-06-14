from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def calculator(request):
    if request.method == 'POST':
        result = request.POST.get('result', '')
        
        return render(request, 'index.html', {'result': result})
    
    return render(request, 'index.html')



def string_manipulation(request):
  if request.method == 'POST':
    user_string = request.POST.get('user_string')
    
    # String manipulation operations
    concatenated_string = user_string + " - Manipulated"
    split_list = user_string.split()
    reversed_string = user_string[::-1]
    substring = request.POST.get('substring')
    substring_found = substring in user_string
  
    context = {
      'user_string': user_string,
      'concatenated_string': concatenated_string,
      'split_list': split_list,
      'reversed_string': reversed_string,
      'substring': substring,
      'substring_found': substring_found,
    }
    
    return render(request, 'strings.html', context)
  else:
    return render(request, 'strings.html')
