from django.shortcuts import render

# Get Chat Room name from user ...
def index(request):
    return render(request, 'chat/index.html')


# Show a Particular Chat Room name  ...
def room(request, room_name):
    context ={
        'room_name': room_name
    }
    return render(request, 'chat/room.html',context)