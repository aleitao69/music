@echo off
cd /d C:\Users\antonio\Dropbox\music

echo Adding new songs to Git...
git add media/audio

echo Committing changes...
git commit -m "🎵 Add new songs to playlist"

echo Pushing to GitHub...
git push origin main

pause
