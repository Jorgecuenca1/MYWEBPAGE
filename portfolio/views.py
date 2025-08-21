from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from .models import (
    Perfil, Educacion, CategoriaHabilidad, Habilidad, 
    Experiencia, Proyecto, Certificacion, RedSocial
)

# Diccionario de traducciones COMPLETO
TRANSLATIONS = {
    'es': {
        # Navegación
        'home': 'Inicio',
        'about': 'Sobre Mí',
        'skills': 'Habilidades',
        'experience': 'Experiencia',
        'projects': 'Proyectos',
        'contact': 'Contacto',
        
        # Hero Section
        'engineer_title': 'Ingeniero Electrónico | Especialista en Inteligencia Artificial',
        'hero_description': 'Experto en desarrollo de software con IA, Machine Learning y más de 6 años de experiencia en Django. Especialista en crear soluciones tecnológicas innovadoras que transforman procesos empresariales y optimizan la eficiencia organizacional mediante inteligencia artificial avanzada.',
        'view_projects': 'Ver Proyectos',
        'contact_me': 'Contactar',
        
        # Secciones principales
        'about_me': 'Sobre Mí',
        'academic_formation': 'Formación Académica',
        'main_skills': 'Habilidades Principales',
        'recent_experience': 'Experiencia Reciente',
        'featured_projects': 'Proyectos Destacados',
        'specialties': 'Especialidades',
        'technical_skills': 'Habilidades Técnicas',
        'professional_experience': 'Experiencia Profesional',
        'my_projects': 'Mis Proyectos',
        
        # Información personal
        'age': 'Edad',
        'location': 'Ubicación',
        'email': 'Email',
        'phone': 'Teléfono',
        'years': 'años',
        'years_experience': 'años de experiencia',
        'birth_place': 'Lugar de Nacimiento',
        'id_number': 'Cédula',
        'license': 'Licencia de Conducción',
        'personal_info': 'Información Personal',
        'biography': 'Biografía',
        
        # Habilidades y experiencia
        'level': 'Nivel',
        'technologies': 'Tecnologías',
        'status': 'Estado',
        'completed': 'Completado',
        'in_development': 'En desarrollo',
        'active': 'Activo',
        'experience_years': 'Años de Experiencia',
        'ai_technologies': 'Tecnologías de IA',
        'completed_projects': 'Proyectos Completados',
        'cloud_platforms': 'Plataformas Cloud',
        'main_achievements': 'Logros Principales',
        'technologies_used': 'Tecnologías utilizadas',
        'experience_summary': 'Resumen de Experiencia',
        'skill_level': 'Nivel de Habilidad',
        
        # Proyectos
        'see_site': 'Ver Sitio',
        'see_code': 'Ver Código',
        'details': 'Detalles',
        'demo': 'Demo',
        'code': 'Código',
        'project_info': 'Información del Proyecto',
        'development_period': 'Período de Desarrollo',
        'project_description': 'Descripción del Proyecto',
        'related_projects': 'Otros Proyectos',
        'back_to_projects': 'Volver a Proyectos',
        'similar_project': 'Contactar para Proyecto Similar',
        'project_stats': 'Estadísticas de Proyectos',
        'public_entities': 'Entidades Públicas',
        'ai_projects': 'Proyectos con IA',
        'active_websites': 'Sitios Web Activos',
        'featured_project': 'Proyecto Destacado',
        'solutions_developed': 'Soluciones tecnológicas que he desarrollado',
        
        # Botones y acciones
        'all_skills': 'Ver Todas las Habilidades',
        'full_experience': 'Ver Experiencia Completa',
        'all_projects': 'Ver Todos los Proyectos',
        'contact_now': 'Contactar Ahora',
        'know_more': 'Conocer Más',
        'send_message': 'Enviar Mensaje',
        'learn_more': 'Conocer Más',
        
        # Contacto
        'interested_collaborate': '¿Interesado en Colaborar?',
        'available_projects': 'Estoy disponible para proyectos de desarrollo de software, consultoría en IA y colaboraciones tecnológicas.',
        'follow_me': 'Sígueme en:',
        'services': 'Servicios',
        'contact_info': 'Información de Contacto',
        'availability': 'Disponibilidad',
        'schedule': 'Horario',
        'timezone': 'Zona Horaria',
        'response': 'Respuesta',
        'weekdays': 'Lunes a Viernes',
        'hours': '8:00 AM - 6:00 PM',
        'bogota_time': 'GMT-5<br>Bogotá, Colombia',
        'within_24h': 'Dentro de 24 horas<br>en días hábiles',
        
        # Formulario
        'name': 'Nombre',
        'subject': 'Asunto',
        'message': 'Mensaje',
        'required': 'requerido',
        
        # Educación
        'education_highlighted': 'Educación Destacada:',
        'coming_soon': 'próximamente...',
        'certifications': 'Certificaciones',
        'verify': 'Verificar',
        
        # Footer
        'rights_reserved': 'Todos los derechos reservados.',
        'developed_with': 'Desarrollado con',
        'django_passion': 'usando Django y mucha pasión por la tecnología.',
        
        # Servicios específicos
        'ai_software_dev': 'Desarrollo de Software con IA',
        'ml_consulting': 'Consultoría en Machine Learning',
        'django_web_dev': 'Desarrollo Web con Django',
        'flutter_mobile': 'Aplicaciones Móviles con Flutter',
        'process_automation': 'Automatización de Procesos',
        'cloud_architecture': 'Arquitectura Cloud',
        'ar_vr_dev': 'Realidad Aumentada/Virtual',
        'llm_training': 'Entrenamiento de Modelos LLM',
        
        # Páginas específicas
        'my_trajectory': 'Conoce mi trayectoria profesional y académica',
        'tech_tools': 'Tecnologías y herramientas que domino',
        'work_experience': 'Mi trayectoria en desarrollo de software e IA',
        'have_project': '¿Tienes un proyecto en mente? ¡Hablemos!',
    },
    'en': {
        # Navigation
        'home': 'Home',
        'about': 'About Me',
        'skills': 'Skills',
        'experience': 'Experience',
        'projects': 'Projects',
        'contact': 'Contact',
        
        # Hero Section
        'engineer_title': 'Electronic Engineer | Artificial Intelligence Specialist',
        'hero_description': 'Expert in AI software development, Machine Learning and 6+ years of Django experience. Specialist in creating innovative technological solutions that transform business processes and optimize organizational efficiency through advanced artificial intelligence.',
        'view_projects': 'View Projects',
        'contact_me': 'Contact',
        
        # Main sections
        'about_me': 'About Me',
        'academic_formation': 'Academic Background',
        'main_skills': 'Main Skills',
        'recent_experience': 'Recent Experience',
        'featured_projects': 'Featured Projects',
        'specialties': 'Specialties',
        'technical_skills': 'Technical Skills',
        'professional_experience': 'Professional Experience',
        'my_projects': 'My Projects',
        
        # Personal information
        'age': 'Age',
        'location': 'Location',
        'email': 'Email',
        'phone': 'Phone',
        'years': 'years old',
        'years_experience': 'years experience',
        'birth_place': 'Place of Birth',
        'id_number': 'ID Number',
        'license': 'Driver\'s License',
        'personal_info': 'Personal Information',
        'biography': 'Biography',
        
        # Skills and experience
        'level': 'Level',
        'technologies': 'Technologies',
        'status': 'Status',
        'completed': 'Completed',
        'in_development': 'In development',
        'active': 'Active',
        'experience_years': 'Years of Experience',
        'ai_technologies': 'AI Technologies',
        'completed_projects': 'Completed Projects',
        'cloud_platforms': 'Cloud Platforms',
        'main_achievements': 'Main Achievements',
        'technologies_used': 'Technologies used',
        'experience_summary': 'Experience Summary',
        'skill_level': 'Skill Level',
        
        # Projects
        'see_site': 'View Site',
        'see_code': 'View Code',
        'details': 'Details',
        'demo': 'Demo',
        'code': 'Code',
        'project_info': 'Project Information',
        'development_period': 'Development Period',
        'project_description': 'Project Description',
        'related_projects': 'Other Projects',
        'back_to_projects': 'Back to Projects',
        'similar_project': 'Contact for Similar Project',
        'project_stats': 'Project Statistics',
        'public_entities': 'Public Entities',
        'ai_projects': 'AI Projects',
        'active_websites': 'Active Websites',
        'featured_project': 'Featured Project',
        'solutions_developed': 'Technological solutions I have developed',
        
        # Buttons and actions
        'all_skills': 'View All Skills',
        'full_experience': 'View Full Experience',
        'all_projects': 'View All Projects',
        'contact_now': 'Contact Now',
        'know_more': 'Learn More',
        'send_message': 'Send Message',
        'learn_more': 'Learn More',
        
        # Contact
        'interested_collaborate': 'Interested in Collaborating?',
        'available_projects': 'I am available for software development projects, AI consulting and technological collaborations.',
        'follow_me': 'Follow me on:',
        'services': 'Services',
        'contact_info': 'Contact Information',
        'availability': 'Availability',
        'schedule': 'Schedule',
        'timezone': 'Time Zone',
        'response': 'Response',
        'weekdays': 'Monday to Friday',
        'hours': '8:00 AM - 6:00 PM',
        'bogota_time': 'GMT-5<br>Bogotá, Colombia',
        'within_24h': 'Within 24 hours<br>on business days',
        
        # Form
        'name': 'Name',
        'subject': 'Subject',
        'message': 'Message',
        'required': 'required',
        
        # Education
        'education_highlighted': 'Featured Education:',
        'coming_soon': 'coming soon...',
        'certifications': 'Certifications',
        'verify': 'Verify',
        
        # Footer
        'rights_reserved': 'All rights reserved.',
        'developed_with': 'Developed with',
        'django_passion': 'using Django and lots of passion for technology.',
        
        # Specific services
        'ai_software_dev': 'AI Software Development',
        'ml_consulting': 'Machine Learning Consulting',
        'django_web_dev': 'Django Web Development',
        'flutter_mobile': 'Flutter Mobile Applications',
        'process_automation': 'Process Automation',
        'cloud_architecture': 'Cloud Architecture',
        'ar_vr_dev': 'Augmented/Virtual Reality',
        'llm_training': 'LLM Model Training',
        
        # Specific pages
        'my_trajectory': 'Learn about my professional and academic background',
        'tech_tools': 'Technologies and tools I master',
        'work_experience': 'My journey in software development and AI',
        'have_project': 'Have a project in mind? Let\'s talk!',
    }
}

def get_language_from_request(request):
    """Obtener idioma de la sesión o usar español por defecto"""
    return request.session.get('language', 'es')

def set_language(request):
    """Cambiar idioma"""
    if request.method == 'POST':
        language = request.POST.get('language', 'es')
        if language in ['es', 'en']:
            request.session['language'] = language
    
    # Redirigir a la página anterior o al home
    next_url = request.META.get('HTTP_REFERER', '/')
    return HttpResponseRedirect(next_url)

def home(request):
    """Vista principal del portfolio"""
    try:
        perfil = Perfil.objects.first()
        if not perfil:
            return render(request, 'portfolio/setup.html')
        
        # Obtener idioma
        language = get_language_from_request(request)
        translations = TRANSLATIONS.get(language, TRANSLATIONS['es'])
        
        # Obtener datos para la página principal
        educacion = Educacion.objects.filter(perfil=perfil)[:3]
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
            'language': language,
            'translations': translations,
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
        
        # Obtener idioma
        language = get_language_from_request(request)
        translations = TRANSLATIONS.get(language, TRANSLATIONS['es'])
        
        context = {
            'perfil': perfil,
            'educacion': educacion,
            'certificaciones': certificaciones,
            'language': language,
            'translations': translations,
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
        
        # Obtener idioma
        language = get_language_from_request(request)
        translations = TRANSLATIONS.get(language, TRANSLATIONS['es'])
        
        categorias = CategoriaHabilidad.objects.prefetch_related(
            'habilidades'
        ).filter(
            habilidades__perfil=perfil
        ).distinct().order_by('orden')
        
        context = {
            'perfil': perfil,
            'categorias': categorias,
            'language': language,
            'translations': translations,
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
        
        # Obtener idioma
        language = get_language_from_request(request)
        translations = TRANSLATIONS.get(language, TRANSLATIONS['es'])
        
        experiencias = Experiencia.objects.filter(perfil=perfil).order_by('-fecha_inicio')
        
        context = {
            'perfil': perfil,
            'experiencias': experiencias,
            'language': language,
            'translations': translations,
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
        
        # Obtener idioma
        language = get_language_from_request(request)
        translations = TRANSLATIONS.get(language, TRANSLATIONS['es'])
        
        proyectos_list = Proyecto.objects.filter(perfil=perfil).order_by('-destacado', '-fecha_inicio')
        
        context = {
            'perfil': perfil,
            'proyectos': proyectos_list,
            'language': language,
            'translations': translations,
        }
        
        return render(request, 'portfolio/proyectos.html', context)
    
    except Exception as e:
        return render(request, 'portfolio/error.html', {'error': str(e)})

def proyecto_detalle(request, proyecto_id):
    """Vista detallada de un proyecto específico"""
    try:
        perfil = Perfil.objects.first()
        proyecto = get_object_or_404(Proyecto, id=proyecto_id, perfil=perfil)
        
        # Obtener idioma
        language = get_language_from_request(request)
        translations = TRANSLATIONS.get(language, TRANSLATIONS['es'])
        
        # Proyectos relacionados
        proyectos_relacionados = Proyecto.objects.filter(
            perfil=perfil
        ).exclude(id=proyecto_id)[:3]
        
        context = {
            'perfil': perfil,
            'proyecto': proyecto,
            'proyectos_relacionados': proyectos_relacionados,
            'language': language,
            'translations': translations,
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
        
        # Obtener idioma
        language = get_language_from_request(request)
        translations = TRANSLATIONS.get(language, TRANSLATIONS['es'])
        
        redes_sociales = RedSocial.objects.filter(perfil=perfil, activo=True)
        
        context = {
            'perfil': perfil,
            'redes_sociales': redes_sociales,
            'language': language,
            'translations': translations,
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