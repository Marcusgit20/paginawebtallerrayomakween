from django.db import models

# Create your models here.
class Cargo(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
	    return self.nombre;
    

class Mecanico(models.Model):
    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=100)
    correo = models.CharField(max_length=20)
    passwd = models.CharField(max_length=20)
    edad = models.IntegerField()
    cargo = models.ForeignKey(Cargo, on_delete=models.PROTECT)
    fecha_nacimiento = models.DateField()
    foto = models.ImageField(upload_to="mecanico", null=True)

    def __str__(self):
        return self.rut;

lista_estado =[
    ["P", "Pendiente"],
    ["A", "Aprobado"],
    ["R", "Rechazado"]
]

class Trabajo(models.Model):
    id_trabajo = models.IntegerField()
    rut_mecanico = models.CharField(max_length=10)
    nombre_trabajo = models.CharField(max_length=70)
    fecha_trabajo = models.DateField()
    desc_trabajo = models.CharField(max_length=350)
    diagnostico = models.CharField(max_length=50)
    materiales_usados = models.CharField(max_length=100)
    herr_usadas = models.CharField(max_length=100)
    foto = models.ImageField(upload_to="trabajos", null=True)
    estado = models.CharField(max_length=1, choices=lista_estado)
    motivo_desaprobacion = models.CharField(max_length=250, default='none')
    
    def __str__(self):
        return self.nombre_trabajo;

lista_tipo_contacto = [
     [0, "Sugerencia"],
     [1, "Reclamo"],
     [2, "Felicitaciones"]
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    telefono = models.IntegerField()
    tipo_contacto = models.IntegerField(choices=lista_tipo_contacto)
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre + "" + self.email
    
class Postulacion(models.Model):
    rut_postulante = models.CharField(max_length=10)
    nombres = models.CharField(max_length=80)
    apellidos = models.CharField(max_length=20)
    numero_telefono = models.IntegerField()
    correo = models.CharField(max_length=20)
    experiencia = models.CharField(max_length=200)
    curriculum = models.ImageField(upload_to="curriculums", null=True)

    def __str__(self):
        return self.rut_postulante