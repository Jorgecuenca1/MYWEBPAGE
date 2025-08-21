from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import (
    Perfil, Educacion, CategoriaHabilidad, Habilidad, 
    Experiencia, Proyecto, Certificacion, RedSocial
)

def home(request):
    """Vista principal del portfolio"""
    try:
        perfil = Perfil.objects.first()
        if not perfil:
            # Si no hay perfil, mostrar página de configuración
            return render(request, 'portfolio/setup.html')
        
        # Obtener datos para la página principal
        educacion = Educacion.objects.filter(perfil=perfil)[:3]  # Últimas 3
        habilidades_destacadas = Habilidad.objects.filter(
            perfil=perfil, 
            porcentaje__gte=80
        ).select_related('categoria')[:8]
        
        experiencias_recientes = Experiencia.objects.filter(perfil=perfil)[:3]
        proyectos_destacados = Proyecto.objects.filter(
            perfil=perfil, 
            destacado=True
        )[:6]
        
        redes_sociales = RedSocial.objects.filter(perfil=perfil, activo=True)
        
        context = {
            'perfil': perfil,
            'educacion': educacion,
            'habilidades_destacadas': habilidades_destacadas,
            'experiencias_recientes': experiencias_recientes,
            'proyectos_destacados': proyectos_destacados,
            'redes_sociales': redes_sociales,
        }
        
        return render(request, 'portfolio/home.html', context)
    
    except Exception as e:
        return render(request, 'portfolio/error.html', {'error': str(e)})

def sobre_mi(request):
    """Vista detallada sobre mí"""
    try:
        perfil = get_object_or_404(Perfil)
        educacion = Educacion.objects.filter(perfil=perfil).order_by('-fecha_inicio')
        certificaciones = Certificacion.objects.filter(perfil=perfil).order_by('-fecha_obtencion')
        
        context = {
            'perfil': perfil,
            'educacion': educacion,
            'certificaciones': certificaciones,
        }
        
        return render(request, 'portfolio/sobre_mi.html', context)
    
    except Perfil.DoesNotExist:
        return render(request, 'portfolio/setup.html')

def habilidades(request):
    """Vista de habilidades organizadas por categorías"""
    try:
        perfil = Perfil.objects.first()
        if not perfil:
            return render(request, 'portfolio/setup.html')
        
        categorias = CategoriaHabilidad.objects.prefetch_related(
            'habilidades'
        ).filter(
            habilidades__perfil=perfil
        ).distinct().order_by('orden')
        
        context = {
            'perfil': perfil,
            'categorias': categorias,
        }
        
        return render(request, 'portfolio/habilidades.html', context)
    
    except Exception as e:
        return render(request, 'portfolio/error.html', {'error': str(e)})

def experiencia(request):
    """Vista de experiencia laboral y proyectos"""
    try:
        perfil = Perfil.objects.first()
        if not perfil:
            return render(request, 'portfolio/setup.html')
        
        experiencias = Experiencia.objects.filter(perfil=perfil).order_by('-fecha_inicio')
        
        context = {
            'perfil': perfil,
            'experiencias': experiencias,
        }
        
        return render(request, 'portfolio/experiencia.html', context)
    
    except Exception as e:
        return render(request, 'portfolio/error.html', {'error': str(e)})

def proyectos(request):
    """Vista de proyectos"""
    try:
        perfil = Perfil.objects.first()
        if not perfil:
            return render(request, 'portfolio/setup.html')
        
        proyectos_list = Proyecto.objects.filter(perfil=perfil).order_by('-destacado', '-fecha_inicio')
        
        context = {
            'perfil': perfil,
            'proyectos': proyectos_list,
        }
        
        return render(request, 'portfolio/proyectos.html', context)
    
    except Exception as e:
        return render(request, 'portfolio/error.html', {'error': str(e)})

def proyecto_detalle(request, proyecto_id):
    """Vista detallada de un proyecto específico"""
    try:
        perfil = Perfil.objects.first()
        proyecto = get_object_or_404(Proyecto, id=proyecto_id, perfil=perfil)
        
        # Proyectos relacionados (mismas tecnologías)
        proyectos_relacionados = Proyecto.objects.filter(
            perfil=perfil
        ).exclude(id=proyecto_id)[:3]
        
        context = {
            'perfil': perfil,
            'proyecto': proyecto,
            'proyectos_relacionados': proyectos_relacionados,
        }
        
        return render(request, 'portfolio/proyecto_detalle.html', context)
    
    except Exception as e:
        return render(request, 'portfolio/error.html', {'error': str(e)})

def contacto(request):
    """Vista de contacto"""
    try:
        perfil = Perfil.objects.first()
        if not perfil:
            return render(request, 'portfolio/setup.html')
        
        redes_sociales = RedSocial.objects.filter(perfil=perfil, activo=True)
        
        context = {
            'perfil': perfil,
            'redes_sociales': redes_sociales,
        }
        
        return render(request, 'portfolio/contacto.html', context)
    
    except Exception as e:
        return render(request, 'portfolio/error.html', {'error': str(e)})

def api_habilidades(request):
    """API JSON para obtener habilidades (para gráficos dinámicos)"""
    try:
        perfil = Perfil.objects.first()
        if not perfil:
            return JsonResponse({'error': 'No hay perfil configurado'}, status=404)
        
        habilidades = Habilidad.objects.filter(perfil=perfil).select_related('categoria')
        
        data = []
        for habilidad in habilidades:
            data.append({
                'nombre': habilidad.nombre,
                'categoria': habilidad.categoria.nombre,
                'nivel': habilidad.nivel,
                'porcentaje': habilidad.porcentaje,
                'años_experiencia': habilidad.años_experiencia,
            })
        
        return JsonResponse({'habilidades': data})
    
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)