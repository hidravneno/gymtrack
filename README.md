# GymTrack - Sistema de Gestión para Gimnasios

GymTrack es un sistema completo de gestión para gimnasios desarrollado con Django. Permite la administración de miembros, pagos, asistencias y reportes detallados, todo con una interfaz moderna y profesional.

## Características

- **Gestión de Miembros**: Registro, edición y visualización de información de miembros.
- **Control de Pagos**: Registro de pagos con diferentes métodos y generación de recibos.
- **Control de Asistencias**: Registro y seguimiento de asistencias diarias.
- **Reportes y Estadísticas**: Análisis detallado de asistencias, pagos y actividad de miembros.
- **Interfaz Responsiva**: Diseño adaptable para dispositivos móviles y de escritorio.
- **Alertas Interactivas**: Notificaciones con animaciones para mejorar la experiencia del usuario.

## Requisitos

- Python 3.8+
- Django 4.2+
- Otras dependencias en `requirements.txt`

## Instalación

1. Clonar el repositorio:
   ```
   git clone https://github.com/hidravneno/gymtrack.git
   cd gymtrack
   ```

2. Crear y activar entorno virtual:
   ```
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. Instalar dependencias:
   ```
   pip install -r requirements.txt
   ```

4. Configurar la base de datos:
   ```
   python manage.py migrate
   ```

5. Crear un superusuario:
   ```
   python manage.py createsuperuser
   ```

6. Iniciar el servidor de desarrollo:
   ```
   python manage.py runserver
   ```

## Estructura del Proyecto

- **members/**: App para la gestión de miembros y planes de membresía
- **payments/**: App para el manejo de pagos y facturación
- **attendance/**: App para el registro y control de asistencias
- **reports/**: App para análisis, estadísticas y reportes



## Licencia

Este proyecto está bajo la licencia MIT. Ver el archivo `LICENSE` para más detalles.


