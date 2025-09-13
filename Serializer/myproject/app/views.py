from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from app.models import Student
from app.serializers import StudentSerializer
import io
from rest_framework.parsers import JSONParser

@csrf_exempt

def stu_list(req):
    if req.method=='POST':
        data=req.body
        stream=io.BytesIO(data)
        p_data=JSONParser().parse(stream)
        serializer=StudentSerializer(data=p_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'mag':'data created'})
        return JsonResponse({'error':serializer.errors})
    
    elif req.method=='DELETE':
        data=req.body
        stream=io.BytesIO(data)
        p_data=JSONParser().parse(stream)
        id=p_data.get('id')
        stu=Student.objects.get(id=id)
        stu.delete()
        return JsonResponse({'msg':'data deleted'})
    
    elif req.method=='GET':
        all_stu = Student.objects.all()
        serializer = StudentSerializer(all_stu, many=True)  
        return JsonResponse(serializer.data, safe=False)
    

@csrf_exempt
def stu_detail(req,pk):
    data=Student.objects.filter(id=pk)
    if data:
        if req.method=='GET':
            data=Student.objects.get(id=pk)
            serializer=StudentSerializer(data)
            return JsonResponse(serializer.data)
        elif req.method=='PUT':
            old_data=Student.objects.get(id=pk)
            data=req.body
            stream=io.BytesIO(data)
            new_p_data=JSONParser().parse(stream)
            serializer=StudentSerializer(old_data,data=new_p_data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'msg':'Data updated'})
            return JsonResponse({'error':serializer.errors})
        
        elif req.method=='PATCH':
            old_data=Student.objects.get(id=pk)
            data=req.body
            stream=io.BytesIO(data)
            new_p_data=JSONParser().parse(stream)
            serializer=StudentSerializer(old_data,data=new_p_data,parsial=True)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'msg':'Data updated'})
            return JsonResponse({'error':serializer.errors})
        

        elif req.method=='DELETE':
            data=Student.objects.get(id=pk)
            data.delete()
            return JsonResponse({'msg':'Data deleted'})
    return JsonResponse({'msg':"id is not exist"})