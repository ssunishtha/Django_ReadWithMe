#i have made this file
from django.http import HttpResponse
from django.shortcuts import  render
def index(request):
   return render(request, 'index.html')

def politics(request):
    s=''' <a href="https://en.wikipedia.org/wiki/Akshay_Kumar"></a>
      <a href="https://en.wikipedia.org/wiki/Amitabh_Bachchan"</a>
      <a href="https://en.wikipedia.org/wiki/Priyanka_Chopra"</a>'''
    return HttpResponse(s)
def bolywood(request):
    r=''' <a href="https:en.wikipedia.org/wiki/Akshay_Kumar"</a>
      <a href="https://en.wikipedia.org/wiki/Amitabh_Bachchan"</a>
      <a href="https://en.wikipedia.org/wiki/Priyanka_Chopra"</a>'''
    return HttpResponse(r)
def sports(request):
    t='''  <a href="https://en.wikipedia.org/wiki/Cristiano_Ronaldo">Cristiano Ronaldo</a>
      <a href="https://en.wikipedia.org/wiki/MS_Dhoni">MS Dhoni</a>
      <a href="https://en.wikipedia.org/wiki/Jack_Ma">Jack  Ma</a>'''
    return HttpResponse(t)