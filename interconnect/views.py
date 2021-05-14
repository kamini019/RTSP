from django.http import StreamingHttpResponse
from django.shortcuts import render
from interconnect.helper.rtsp_opencv import DataFeed, gen
from interconnect.models import AddUserInput
from datetime import date

today = date.today()


def index(request):
    arg = {'camera_count': range(4)}
    if request.method == "POST":
        num = request.POST.get('search')
        try:
            userDetails = AddUserInput(user_input=int(num), date=today)
            userDetails.save()
            print('Saved Successfully!!')
        except:
            print('Error!!')
        arg = {
            'camera_count': range(int(num))
        }
        return render(request, 'index.html', arg)
    return render(request, 'index.html', arg)


def rtsp_feed(request):
    return StreamingHttpResponse(gen(DataFeed()),
                                 content_type='multipart/x-mixed-replace; boundary=frame')
