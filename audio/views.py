import json
from django.shortcuts import render
from django.conf import settings
import os

def flac_player_view(request):
    audio_dir = os.path.join(settings.MEDIA_ROOT, "audio")
    files = os.listdir(audio_dir)
    flac_files = [f"/media/audio/{f}" for f in files if f.lower().endswith((".flac", ".mp3"))]
    return render(request, "flac_player.html", {"flac_files": flac_files})
