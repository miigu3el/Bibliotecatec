# Generated by Django 4.2.5 on 2023-09-15 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_autor_site_autor_alter_editora_site_editora'),
    ]

    operations = [
        migrations.RenameField(
            model_name='autor',
            old_name='cidade_autor',
            new_name='cidade',
        ),
        migrations.RenameField(
            model_name='autor',
            old_name='nome_autor',
            new_name='nome',
        ),
        migrations.RenameField(
            model_name='autor',
            old_name='site_autor',
            new_name='site',
        ),
        migrations.RenameField(
            model_name='cidade',
            old_name='nome_cidade',
            new_name='nome',
        ),
        migrations.RenameField(
            model_name='editora',
            old_name='cidade_editora',
            new_name='cidade',
        ),
        migrations.RenameField(
            model_name='editora',
            old_name='nome_editora',
            new_name='nome',
        ),
        migrations.RenameField(
            model_name='editora',
            old_name='site_editora',
            new_name='site',
        ),
        migrations.RenameField(
            model_name='genero',
            old_name='nome_genero',
            new_name='nome',
        ),
        migrations.RenameField(
            model_name='leitor',
            old_name='cpf_leitor',
            new_name='cpf',
        ),
        migrations.RenameField(
            model_name='leitor',
            old_name='email_leitor',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='leitor',
            old_name='nome_leitor',
            new_name='nome',
        ),
        migrations.RenameField(
            model_name='livro',
            old_name='data_plub',
            new_name='data_pub',
        ),
        migrations.RenameField(
            model_name='livro',
            old_name='nome_livro',
            new_name='nome',
        ),
    ]