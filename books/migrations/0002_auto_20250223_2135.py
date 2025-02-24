from django.db import migrations

def create_preinstalled_book(apps, schema_editor):
    Book = apps.get_model('books', 'Book')
    Book.objects.create(title='Demo Book', rating=0.0)

class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),  # Make sure this matches your first migration name
    ]

    operations = [
        migrations.RunPython(create_preinstalled_book),
    ]
