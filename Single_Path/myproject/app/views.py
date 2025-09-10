from django.shortcuts import render
from .models import Student
import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict


@csrf_exempt
def student_view(req):
    try:
        if req.method == 'POST':
            data = json.loads(req.body)
            Student.objects.create(
                name=data['name'],
                email=data['email'],
                contact=data['contact']
            )
            return JsonResponse({'msg': "Student created successfully"}, status=201)

        elif req.method == 'GET':
            if 'id' in req.GET:
                pk = req.GET.get('id')
                stu = Student.objects.get(id=pk)
                return JsonResponse(model_to_dict(stu), safe=False)
            else:
                all_students = Student.objects.all().values()
                return JsonResponse(list(all_students), safe=False)

        elif req.method == 'PUT':
            data = json.loads(req.body)
            pk = data['id']
            obj = Student.objects.get(id=pk)
            obj.name = data['name']
            obj.email = data['email']
            obj.contact = data['contact']
            obj.save()
            return JsonResponse({'msg': 'Updated', 'new_data': model_to_dict(obj)})

        elif req.method == 'PATCH':
            data = json.loads(req.body)
            pk = data['id']
            obj = Student.objects.get(id=pk)
            if 'name' in data:
                obj.name = data['name']
            if 'email' in data:
                obj.email = data['email']
            if 'contact' in data:
                obj.contact = data['contact']
            obj.save()
            return JsonResponse({'msg': 'Partially updated', 'new_data': model_to_dict(obj)})

        elif req.method == 'DELETE':
            data = json.loads(req.body)
            pk = data['id']
            obj = Student.objects.get(id=pk)
            obj.delete()
            return JsonResponse({'msg': 'Deleted successfully'})

        else:
            return JsonResponse({'error': 'Method not allowed'}, status=405)

    except Student.DoesNotExist:
        return JsonResponse({'error': 'Student not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
