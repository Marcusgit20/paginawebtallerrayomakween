from django.urls import path, include
from .views import home, administrador, galeria, login, contacto, escaneo, cambiofrenos, mantencion, mecanicos, listar_mecanico, modificar_mecanico, eliminar_mecanico, paginamecanico, user_login, listar_trabajo, postulacion, eliminar_postulacion

urlpatterns = [
    path('home/', home, name="home"),
    path('', home, name="home"),
    path('administrador/', administrador, name="administrador"),
    path('galeria/', galeria, name="galeria"),
    path('login/', login, name="login"),
    path('contacto/', contacto, name="contacto"),
    path('escaneo/', escaneo, name="escaneo"),
    path('cambiofrenos/', cambiofrenos, name="cambiofrenos"),
    path('mantencion/', mantencion, name="mantencion"),
    path('mecanicos/', mecanicos, name="mecanicos"),
    path('paginamecanico/', paginamecanico, name="paginamecanico"),
    path('mantenedor/mecanico/listar', listar_mecanico, name="listar_mecanico"),
    path('administrador/modificar/<rut>/', modificar_mecanico, name="modificar_mecanico"),
    path('mantenedor/mecanico/eliminar/<rut>/', eliminar_mecanico, name="eliminar_mecanico"),
    path('user_login/', user_login, name="user_login"),
    path('listar_trabajo/', listar_trabajo, name="listar_trabajo"),
    path('postulacion/', postulacion, name="postulacion"),
    path('eliminar_postulacion/<rut_postulante>/', eliminar_postulacion, name="eliminar_postulacion"),
]