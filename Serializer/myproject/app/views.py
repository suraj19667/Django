from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from app.models import Student
from app.serializers import StudentSerializer
import io
from rest_framework.parsers import JSONParser

# @csrf_exempt

# def stu_list(req):
#     if req.method=='POST':
#         data=req.body
#         stream=io.BytesIO(data)
#         p_data=JSONParser().parse(stream)
#         serializer=StudentSerializer(data=p_data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse({'mag':'data created'})
#         return JsonResponse({'error':serializer.errors})
    
#     elif req.method=='DELETE':
#         data=req.body
#         stream=io.BytesIO(data)
#         p_data=JSONParser().parse(stream)
#         id=p_data.get('id')
#         stu=Student.objects.get(id=id)
#         stu.delete()
#         return JsonResponse({'msg':'data deleted'})
    
#     elif req.method=='GET':
#         all_stu = Student.objects.all()
#         serializer = StudentSerializer(all_stu, many=True)  
#         return JsonResponse(serializer.data, safe=False)
    

# @csrf_exempt
# def stu_detail(req,pk):
#     data=Student.objects.filter(id=pk)
#     if data:
#         if req.method=='GET':
#             data=Student.objects.get(id=pk)
#             serializer=StudentSerializer(data)
#             return JsonResponse(serializer.data)
#         elif req.method=='PUT':
#             old_data=Student.objects.get(id=pk)
#             data=req.body
#             stream=io.BytesIO(data)
#             new_p_data=JSONParser().parse(stream)
#             serializer=StudentSerializer(old_data,data=new_p_data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return JsonResponse({'msg':'Data updated'})
#             return JsonResponse({'error':serializer.errors})
        
#         elif req.method=='PATCH':
#             old_data=Student.objects.get(id=pk)
#             data=req.body
#             stream=io.BytesIO(data)
#             new_p_data=JSONParser().parse(stream)
#             serializer=StudentSerializer(old_data,data=new_p_data,parsial=True)
#             if serializer.is_valid():
#                 serializer.save()
#                 return JsonResponse({'msg':'Data updated'})
#             return JsonResponse({'error':serializer.errors})
        

#         elif req.method=='DELETE':
#             data=Student.objects.get(id=pk)
#             data.delete()
#             return JsonResponse({'msg':'Data deleted'})
#     return JsonResponse({'msg':"id is not exist"})



from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view



@api_view(["GET","POST"])
def stu_list(req):
    if req.method == "GET":
        snippets = Student.objects.all()
        serializer = StudentSerializer(snippets, many=True)
        return Response(serializer.data)
    elif req.method == "POST":
        serializer = StudentSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET","PUT","PATCH","DELETE"])
def stu_detail(req,pk):
    if req.method=="GET":
        snippet = Student.objects.get(id=pk)
        serializer = StudentSerializer(snippet)
        return Response(serializer.data)

    elif req.method=="PUT":
        snippet = Student.objects.get(id=pk)
        serializer = StudentSerializer(snippet, data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif req.method=="PATCH":
        snippet = Student.objects.get(id=pk)
        serializer = StudentSerializer(snippet, data=req.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif req.method=="DELETE":
        snippet = Student.objects.get(id=pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)