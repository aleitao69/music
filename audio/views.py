import json
from django.shortcuts import render
from django.conf import settings
import os

def flac_player_view(request):
    audio_folder = os.path.join(settings.MEDIA_ROOT, 'audio')
    flac_files = [f for f in os.listdir(audio_folder) if f.endswith(('.flac', '.mp3'))]
    flac_urls = [f"/media/audio/{file}" for file in flac_files]
    return render(request, 'flac_player.html', {
        'flac_urls': json.dumps(flac_urls)  # 🔥 necessário para JSON no template
    })
