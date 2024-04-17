from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuarios 
from django.http import Http404
# Create your views here.


# Create your views here.
def index(request):                    #  <<==========
    return render(request,"index.html")      #  <<==========

def listar(request):
    users = Usuarios.objects.all()
    datos = {'usuarios' : users }
    return render(request, "usuarios/listar.html", datos)

def agregar(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        correo = request.POST.get('correo')
        telefono = request.POST.get('telefono')
        
        if nombre and apellido and correo and telefono:
            # Tạo một đối tượng Usuarios và lưu vào cơ sở dữ liệu
            u = Usuarios(nombre=nombre, apellido=apellido, correo=correo, telefono=telefono)
            u.save()
            # Sau khi lưu, chuyển hướng người dùng đến trang danh sách (listar)
            return redirect('listar')
        else:
            # Nếu dữ liệu không hợp lệ, có thể thực hiện các xử lý khác tùy thuộc vào yêu cầu của bạn
            # Ví dụ: hiển thị thông báo lỗi cho người dùng
            return HttpResponse("Dữ liệu không hợp lệ!")
    else:
        # Nếu phương thức không phải là POST, render template agregar.html để hiển thị biểu mẫu
        return render(request, "usuarios/agregar.html")

def actualizar(request):
    if request.method == 'POST':
        id_usuario = request.POST.get('id')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        correo = request.POST.get('correo')
        telefono = request.POST.get('telefono')
        
        if nombre and apellido and correo and telefono:
            
                # Tìm người dùng cần cập nhật
                usuario = Usuarios.objects.get(id=id_usuario)
                
                # Cập nhật thông tin người dùng
                usuario.nombre = nombre
                usuario.apellido = apellido
                usuario.correo = correo
                usuario.telefono = telefono
                usuario.save()
                
                # Sau khi cập nhật, chuyển hướng người dùng đến trang danh sách
                return redirect('listar')
            
        else:
            # Trả về HttpResponse nếu dữ liệu không hợp lệ
            return HttpResponse("Dữ liệu không hợp lệ!")
    else:
        # Trả về template nếu request method không phải là POST
        users = Usuarios.objects.all()
        datos = {'usuarios': users}
        return render(request, "usuarios/actualizar.html", datos)



def eliminar(request):
    datos = {}
    if request.method == 'POST':
        if request.POST.get('id'):
            id_a_borrar = request.POST.get('id')
            registro = Usuarios.objects.get(id=id_a_borrar)
            registro.delete()
            return redirect('listar')
    else:
        users = Usuarios.objects.all()
        datos = {'usuarios': users}
    return render(request, "usuarios/eliminar.html", datos)
