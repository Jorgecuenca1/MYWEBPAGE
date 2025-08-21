from django.contrib import admin
from .models import (
    Perfil, Educacion, CategoriaHabilidad, Habilidad, 
    Experiencia, Proyecto, Certificacion, RedSocial
)

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ['nombre_completo', 'email', 'telefono']
    search_fields = ['nombre_completo', 'email']
    fieldsets = (
        ('Información Personal', {
            'fields': ('nombre_completo', 'fecha_nacimiento', 'lugar_nacimiento', 'cedula')
        }),
        ('Contacto', {
            'fields': ('email', 'telefono', 'direccion', 'licencia_conduccion')
        }),
        ('Perfil', {
            'fields': ('foto_perfil', 'descripcion_corta', 'biografia')
        }),
    )

class EducacionInline(admin.TabularInline):
    model = Educacion
    extra = 1

class HabilidadInline(admin.TabularInline):
    model = Habilidad
    extra = 1

class ExperienciaInline(admin.StackedInline):
    model = Experiencia
    extra = 1

class ProyectoInline(admin.StackedInline):
    model = Proyecto
    extra = 1

class CertificacionInline(admin.TabularInline):
    model = Certificacion
    extra = 1

class RedSocialInline(admin.TabularInline):
    model = RedSocial
    extra = 1

@admin.register(Educacion)
class EducacionAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'institucion', 'nivel', 'fecha_inicio', 'fecha_fin']
    list_filter = ['nivel', 'en_curso']
    search_fields = ['titulo', 'institucion']
    date_hierarchy = 'fecha_inicio'

@admin.register(CategoriaHabilidad)
class CategoriaHabilidadAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'orden']
    list_editable = ['orden']
    ordering = ['orden']

@admin.register(Habilidad)
class HabilidadAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'categoria', 'nivel', 'porcentaje', 'años_experiencia']
    list_filter = ['categoria', 'nivel']
    search_fields = ['nombre']
    list_editable = ['porcentaje']

@admin.register(Experiencia)
class ExperienciaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'empresa', 'tipo', 'fecha_inicio', 'fecha_fin', 'actual']
    list_filter = ['tipo', 'actual']
    search_fields = ['titulo', 'empresa']
    date_hierarchy = 'fecha_inicio'

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'estado', 'fecha_inicio', 'fecha_fin', 'destacado']
    list_filter = ['estado', 'destacado']
    search_fields = ['nombre', 'descripcion_corta']
    list_editable = ['destacado']
    date_hierarchy = 'fecha_inicio'

@admin.register(Certificacion)
class CertificacionAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'organizacion', 'fecha_obtencion', 'fecha_expiracion']
    search_fields = ['nombre', 'organizacion']
    date_hierarchy = 'fecha_obtencion'

@admin.register(RedSocial)
class RedSocialAdmin(admin.ModelAdmin):
    list_display = ['plataforma', 'usuario', 'url', 'activo']
    list_filter = ['plataforma', 'activo']
    list_editable = ['activo']