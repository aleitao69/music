import json
from django.shortcuts import render
from django.conf import settings
import os


def flac_player_view(request):
    audio_folder = os.path.join('media', 'audio')
    audio_files = []

    for file in os.listdir(audio_folder):
        if file.endswith(('.flac', '.mp3', '.mp4')):
            audio_files.append(f"/media/audio/{file}")

    context = {
        "flac_files": audio_files
    }

    return render(request, "flac_player.html", context)



def flac_player_view_audio(request):
    audio_folder = os.path.join('media', 'audio2')
    audio_files = []

    for file in os.listdir(audio_folder):
        if file.endswith(('.flac', '.mp3')):
            audio_files.append(f"/media/audio2/{file}")

    context = {
        "flac_files": audio_files
    }

    return render(request, "flac_player_audio.html", context)