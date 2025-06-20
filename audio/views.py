from django.shortcuts import render
def flac_player_view(request):
    # These URLs could be local/static or remote
    flac_files = [
        '/media/audio/200moremiles.flac',
        '/media/audio/hob.mp3',
    
    ]
    return render(request, 'audio/player.html', {'flac_files': flac_files})

