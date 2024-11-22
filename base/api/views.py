from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room
from .serializers import RoomSerializer
from base.api import serializers
import openai
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import os


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id'
    ]
    return Response(routes)


@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getRoom(request, pk):
    room = Room.objects.get(id=pk)
    serializer = RoomSerializer(room, many=False)
    return Response(serializer.data)



@csrf_exempt
def chatbot_reply(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_message = data.get("message", "")

        # Call OpenAI's API with the user's message
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",  # or use gpt-3.5-turbo for chat models if available
                prompt=user_message,
                max_tokens=100,
                temperature=0.7,
            )
            bot_reply = response.choices[0].text.strip()
        except Exception as e:
            bot_reply = "I'm having trouble processing your request."

        return JsonResponse({"reply": bot_reply})
    return JsoneResponse({"error": "Invalid request"}, status = 404)