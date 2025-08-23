from django.shortcuts import render


def register(request):
  ctx={
  }
  return render(request, "user/register.html", ctx)

def login(request):
  ctx={
  }
  return render(request, "user/login.html", ctx)

def logout(request):
  pass


