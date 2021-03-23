from django.shortcuts import render

def test(request):
    text = {'test':'test'}
    return render(request, "test.html", text)