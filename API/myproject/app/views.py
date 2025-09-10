from django.shortcuts import render
from app.models import Student
import json
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict

@csrf_exempt
def stu_list(req):

    if req.method == 'POST':
        data=req.body
        print(data)
        p_data=json.loads(data)
        print(p_data)
        print(type(data))
        Student.objects.create(name=p_data['name'],
                               email=p_data['email'],
                               contact=p_data['contact'])
        return JsonResponse({'msg':'Save Successfully'})


    all_data=Student.objects.all()
    # print(all_data)
    # print(type(all_data))
    # print(all_data.values())
    # print(type(all_data.values()))
    py_data=list(all_data.values())
    # print(type(py_data))
    # print(py_data)

    j_data=json.dumps(py_data)
    # print(type(j_data))
    # print(j_data)

    return HttpResponse(j_data, content_type='application/json')

@csrf_exempt
def stu_detail(req, pk):

    if req.method=='DELETE':
        stu_data=Student.objects.get(id=pk)
        stu_data.delete()
        return JsonResponse({'msg':'Deleted Successfully'})
    if req.method=='PUT':
            old_data=Student.objects.get(id=pk)
            row_data=req.body
            new_data=json.loads(row_data)
            old_data.name=new_data['name']
            old_data.email=new_data['email']
            old_data.contact=new_data['contact']
            old_data.save()
            updated_data=Student.objects.get(id=pk)
            return JsonResponse({'msg':'Updated Successfully',
                                 'data':model_to_dict(updated_data)})
        
    if req.method=='PATCH':
        print("PATCH method Called")
        old_data=Student.objects.get(id=pk)
        row_data=req.body
        new_data=json.loads(row_data)
        print("data comming from POSTman",new_data)
        if 'name' in new_data:
            old_data.name=new_data['name']
        if 'email' in new_data:
            old_data.email=new_data['email']
        if 'contact' in new_data:
            old_data.contact=new_data['contact']
        old_data.save()
        updated_data=Student.objects.get(id=pk)
        return JsonResponse({'msg':'Updated ',
                                'data':model_to_dict(updated_data)})
        

    stu_data=Student.objects.get(id=pk)
    p_data=model_to_dict(stu_data)
    j_data=json.dumps(p_data)
    return HttpResponse(j_data, content_type='application/json')
