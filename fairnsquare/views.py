# from django.shortcuts import render
# from django.http import HttpResponse
# from django.core.files.storage import FileSystemStorage
# from django.conf import settings
# from django.core.files.storage import default_storage
# from django.views.decorators.http import require_POST
# import os
# import sys


# # Create your views here.
# def index(request):
# 	return render(request,'upload.html',{'name':'Thi'})

# # def upload(request):
# # 	if request.method == 'POST' and request.FILES['myfile']:
# # 		myfile = request.FILES['myfile']
# # 		fs = FileSystemStorage()
# # 		filename = fs.save(myfile.name, myfile)
# # 		uploaded_file_url = fs.url(filename)
# # 		return render(request, 'upload.html', {'uploaded_file_url': uploaded_file_url,"fileupload":"File uploaded successfully"})
# # 	return render(request, 'upload.html')

# @require_POST
# def upload(request):
# 	if request.method == 'POST' and request.FILES['myfile']:
# 		save_path = os.path.join(settings.MEDIA_ROOT, 'uploads', request.FILES['myfile'])
# 		path = default_storage.save(save_path, request.FILES['myfile'])
# 		return render(request, 'upload.html', {'uploaded_file_url': default_storage.path(path),"fileupload":"File uploaded successfully"})
# 	return render(request, 'upload3.html')   
	
# def add(request):
# 	val1 = int(request.POST['num1'])
# 	val2 = int(request.POST['num2'])
# 	res = val1 + val2
# 	return render(request,'result.html', {'result':res, 'name':'Thi'})

from django.shortcuts import render  
from django.http import HttpResponse  
from fairnsquare.functions import handle_uploaded_file  
from fairnsquare.forms import UploadForm  
from fairnsquare.static.upload.file_read_display_features import load_preproc_data
def upload(request):  
    if request.method == 'POST':  
        fUpload = UploadForm(request.POST, request.FILES)  
        if fUpload.is_valid():  
            handle_uploaded_file(request.FILES['file']) 
            XD_features = load_preproc_data()
            return render(request,"selectFeatures.html", {'features': XD_features})  
    else:  
        fUpload = UploadForm()  
        return render(request,"upload.html",{'form':fUpload})  