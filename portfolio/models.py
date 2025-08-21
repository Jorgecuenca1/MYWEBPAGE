from django.db import models
from django.core.validators import RegexValidator

class Perfil(models.Model):
    nombre_completo = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField()
    lugar_nacimiento = models.CharField(max_length=100)
    cedula = models.CharField(max_length=20, unique=True)
    direccion = models.CharField(max_length=200)
    email = models.EmailField()
    telefono_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Número de teléfono debe estar en formato: '+999999999'. Hasta 15 dígitos permitidos.")
    telefono = models.CharField(validators=[telefono_regex], max_length=17)
    licencia_conduccion = models.CharField(max_length=50, blank=True)
    foto_perfil = models.ImageField(upload_to='perfil/', blank=True, null=True)
    descripcion_corta = models.TextField(max_length=300)
    biografia = models.TextField()
    
    def __str__(self):
        return self.nombre_completo
    
    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfiles"

class Educacion(models.Model):
    NIVEL_CHOICES = [
        ('pregrado', 'Pregrado'),
        ('especializacion', 'Especialización'),
        ('maestria', 'Maestría'),
        ('doctorado', 'Doctorado'),
        ('curso', 'Curso'),
        ('certificacion', 'Certificación'),
    ]
    
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='educacion')
    titulo = models.CharField(max_length=200)
    institucion = models.CharField(max_length=200)
    nivel = models.CharField(max_length=20, choices=NIVEL_CHOICES)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(blank=True, null=True)
    en_curso = models.BooleanField(default=False)
    descripcion = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.titulo} - {self.institucion}"
    
    class Meta:
        verbose_name = "Educación"
        verbose_name_plural = "Educación"
        ordering = ['-fecha_inicio']

class CategoriaHabilidad(models.Model):
    nombre = models.CharField(max_length=100)
    icono = models.CharField(max_length=50, blank=True)  # Para iconos CSS/FontAwesome
    orden = models.IntegerField(default=0)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Categoría de Habilidad"
        verbose_name_plural = "Categorías de Habilidades"
        ordering = ['orden']

class Habilidad(models.Model):
    NIVEL_CHOICES = [
        ('basico', 'Básico'),
        ('intermedio', 'Intermedio'),
        ('avanzado', 'Avanzado'),
        ('experto', 'Experto'),
    ]
    
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='habilidades')
    categoria = models.ForeignKey(CategoriaHabilidad, on_delete=models.CASCADE, related_name='habilidades')
    nombre = models.CharField(max_length=100)
    nivel = models.CharField(max_length=20, choices=NIVEL_CHOICES)
    porcentaje = models.IntegerField(default=0, help_text="Porcentaje de dominio (0-100)")
    descripcion = models.TextField(blank=True)
    años_experiencia = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.nombre} ({self.nivel})"
    
    class Meta:
        verbose_name = "Habilidad"
        verbose_name_plural = "Habilidades"
        ordering = ['categoria', '-porcentaje']

class Experiencia(models.Model):
    TIPO_CHOICES = [
        ('trabajo', 'Trabajo'),
        ('proyecto', 'Proyecto'),
        ('freelance', 'Freelance'),
        ('voluntariado', 'Voluntariado'),
    ]
    
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='experiencias')
    titulo = models.CharField(max_length=200)
    empresa = models.CharField(max_length=200)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(blank=True, null=True)
    actual = models.BooleanField(default=False)
    descripcion = models.TextField()
    tecnologias = models.TextField(help_text="Tecnologías utilizadas, separadas por comas")
    logros = models.TextField(blank=True, help_text="Logros principales del proyecto/trabajo")
    url_proyecto = models.URLField(blank=True)
    imagen = models.ImageField(upload_to='experiencia/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.titulo} - {self.empresa}"
    
    class Meta:
        verbose_name = "Experiencia"
        verbose_name_plural = "Experiencias"
        ordering = ['-fecha_inicio']

class Proyecto(models.Model):
    ESTADO_CHOICES = [
        ('planificacion', 'En Planificación'),
        ('desarrollo', 'En Desarrollo'),
        ('completado', 'Completado'),
        ('mantenimiento', 'En Mantenimiento'),
        ('pausado', 'Pausado'),
    ]
    
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='proyectos')
    nombre = models.CharField(max_length=200)
    descripcion_corta = models.CharField(max_length=300)
    descripcion = models.TextField()
    tecnologias = models.TextField(help_text="Tecnologías utilizadas, separadas por comas")
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(blank=True, null=True)
    url_demo = models.URLField(blank=True)
    url_codigo = models.URLField(blank=True)
    imagen_principal = models.ImageField(upload_to='proyectos/', blank=True, null=True)
    destacado = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        ordering = ['-destacado', '-fecha_inicio']

class Certificacion(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='certificaciones')
    nombre = models.CharField(max_length=200)
    organizacion = models.CharField(max_length=200)
    fecha_obtencion = models.DateField()
    fecha_expiracion = models.DateField(blank=True, null=True)
    url_verificacion = models.URLField(blank=True)
    imagen = models.ImageField(upload_to='certificaciones/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.nombre} - {self.organizacion}"
    
    class Meta:
        verbose_name = "Certificación"
        verbose_name_plural = "Certificaciones"
        ordering = ['-fecha_obtencion']

class RedSocial(models.Model):
    PLATAFORMA_CHOICES = [
        ('linkedin', 'LinkedIn'),
        ('github', 'GitHub'),
        ('twitter', 'Twitter'),
        ('instagram', 'Instagram'),
        ('facebook', 'Facebook'),
        ('youtube', 'YouTube'),
        ('website', 'Sitio Web Personal'),
        ('otro', 'Otro'),
    ]
    
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='redes_sociales')
    plataforma = models.CharField(max_length=20, choices=PLATAFORMA_CHOICES)
    url = models.URLField()
    usuario = models.CharField(max_length=100, blank=True)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.plataforma} - {self.usuario or self.url}"
    
    class Meta:
        verbose_name = "Red Social"
        verbose_name_plural = "Redes Sociales"
        unique_together = ['perfil', 'plataforma']