from django.shortcuts import render

# Get Chat Room name from user ...
def index(request):
    return render(request, 'chat/index.html')