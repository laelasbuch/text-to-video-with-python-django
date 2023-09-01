from django.shortcuts import render, redirect
from .forms import VideoTextForm
from .models import VideoText
from moviepy.editor import TextClip

def generate_video(request):
    if request.method == 'POST':
        form = VideoTextForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']

            # Create a text clip with the provided text
            clip = TextClip(text, fontsize=70, color='white', bg_color='black')

            # Set the duration of the clip (5 minutes)
            clip = clip.set_duration(300)

            # Generate the video file
            video_path = 'media/generated_video.mp4'
            clip.write_videofile(video_path, codec='libx264')

            return render(request, 'video_generator/display_video.html', {'video_path': video_path})
    else:
        form = VideoTextForm()
    
    return render(request, 'video_generator/generate_video.html', {'form': form})
