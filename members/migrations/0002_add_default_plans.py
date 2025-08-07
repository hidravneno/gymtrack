from django.db import migrations

def create_default_plans(apps, schema_editor):
    MembershipPlan = apps.get_model('members', 'MembershipPlan')
    
    plans = [
        {
            'name': 'Plan Diario',
            'description': 'Acceso por 1 día',
            'price': 5.00,
            'duration_days': 1
        },
        {
            'name': 'Plan Semanal',
            'description': 'Acceso ilimitado por 7 días',
            'price': 15.00,
            'duration_days': 7
        },
        {
            'name': 'Plan Mensual',
            'description': 'Acceso ilimitado por 30 días',
            'price': 30.00,
            'duration_days': 30
        },
    ]
    
    for plan_data in plans:
        MembershipPlan.objects.create(**plan_data)

def remove_default_plans(apps, schema_editor):
    MembershipPlan = apps.get_model('members', 'MembershipPlan')
    MembershipPlan.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_default_plans, remove_default_plans),
    ]
