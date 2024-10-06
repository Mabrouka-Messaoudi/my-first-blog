from django.shortcuts import render


def blog(request):
    print("View is being called")
    return render(request,'blog/blog.html')
