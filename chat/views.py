from django.shortcuts import render

def doctor_chat(request):
    return render(request, 'chat/doctor_chat.html')

def video_consultation(request):
    return render(request, 'chat/video_consultation.html')

def chat_room(request, room_name):
    return render(request, 'chat/chat_room.html', {
        'room_name': room_name
    })
