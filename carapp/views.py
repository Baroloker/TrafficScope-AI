# carapp/views.py

from django.shortcuts import render,  redirect
from .forms import ImageUploadForm
from .model.car_detector import CarDetector
import os

model_path = os.path.join(os.path.dirname(__file__), 'model', 'car_detector.pth')
model = CarDetector(model_path)

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            image_path = os.path.join('media', image.name)
            with open(image_path, 'wb+') as destination:
                for chunk in image.chunks():
                    destination.write(chunk)

            prediction = model.predict(image_path)
            os.remove(image_path)

            return render(request, 'result.html', {'prediction': prediction})
    else:
        form = ImageUploadForm()
    return render(request, 'upload.html', {'form': form})

def index(request):
    return render(request, 'index.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def trace_car(request):
    return render(request, 'trace_car.html')

def home(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'admin' and password == 'password':  # 示例验证逻辑
            return redirect('home')
        else:
            return render(request, 'index.html', {'error': '用户名或密码错误'})
    return render(request, 'index.html')