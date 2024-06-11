from django.shortcuts import render
from datetime import datetime  # 导入datetime模块
from .models import Channel, Video
from .models import Channel


def index(request, tvno=None):
    # 获取当前时间
    current_time = datetime.now()
    
    channels = Channel.objects.all()

    if tvno is None or tvno >= len(channels):
        channel = channels[0]
    else:
        channel = channels[tvno]

    videos = Video.objects.filter(channel=channel)

    # 将当前时间添加到上下文变量中
    return render(request, 'index.html', {'channels': channels, 'videos': videos, 'current_time': current_time})

