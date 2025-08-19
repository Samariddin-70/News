from django.shortcuts import render

# Create your views here.

def index(request):
  ctx={

  }
  return render(request, 'site/index.html', ctx)

def category(request):
  ctx = {

  }
  return render(request, 'site/category.html', ctx)

def contact(request):
  ctx = {

  }
  return render(request, 'site/contact.html', ctx)

def search(request):
  ctx = {

  }
  return render(request, 'site/search.html', ctx)

def view(request):
  ctx = {

  }
  return render(request, 'site/view.html', ctx)
