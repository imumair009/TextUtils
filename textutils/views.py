# Main File
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def error(request):
    return render(request, 'error.html')
   

def analyze(request):
    
    djtext = request.POST.get('text', 'default')

    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    firstcap = request.POST.get('firstcap', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
  

    if removepunc == "on":
     pun = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
     ana = ""
     for char in djtext:
        if char not in pun:
            ana += char
     params = {'purpose':'Remove Punctuations', 'analyzed_text': ana}
     djtext = ana
     

    if fullcaps == "on":
       ana = ""
       for char in djtext:
          ana = ana + char.upper()
       params = {'purpose':'UpperCase', 'analyzed_text': ana}
       djtext = ana
  
    
    if firstcap == "on":
       ana = ""
       if djtext and not djtext[0].isupper():
         ana = djtext[0].upper() + djtext[1:]
       params = {'purpose':'Capital First Letter', 'analyzed_text': ana}
       djtext = ana

    
    if newlineremover == "on":
        ana = ""
        for char in djtext:
          if char != "/n" and char != "/r":
           ana = ana + char
          else:
             print("no")
        params = {'purpose':'New LineReomver', 'analyzed_text': ana}
        djtext = ana
        
    
    if spaceremover == "on":
       ana = ""
       for index, char in enumerate(djtext):
         if not (djtext[index] == " " and djtext[index+1] == " "):
            ana = ana + char
       params = {'purpose':'Extra Space Reomver', 'analyzed_text': ana}
       
    if (removepunc !="on") and (fullcaps !="on" ) and (firstcap !="on") and (newlineremover !="on") and (spaceremover !="on"):
       return render(request, "error.html")

    
    return render(request, 'analyze.html', params)
    
def aboutus(request):
   return render(request, 'aboutus.html')

def contactus(request):
   return render(request, 'contactus.html')

