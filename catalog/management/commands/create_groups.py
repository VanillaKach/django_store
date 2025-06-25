from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from catalog.models import Product
from blog.models import BlogPost


class Command(BaseCommand):
    help = 'Creates moderator and content manager groups with permissions'

    def handle(self, *args, **options):
        # Группа модераторов продуктов
        mod_group, created = Group.objects.get_or_create(name='Модератор продуктов')
        product_content_type = ContentType.objects.get_for_model(Product)

        mod_permissions = [
            'delete_product',
            'can_unpublish_product',
            'can_change_publish_status'
        ]

        for perm in mod_permissions:
            permission = Permission.objects.get(
                codename=perm,
                content_type=product_content_type
            )
            mod_group.permissions.add(permission)

        # Группа контент-менеджеров
        cm_group, created = Group.objects.get_or_create(name='Контент-менеджер')
        blog_content_type = ContentType.objects.get_for_model(BlogPost)

        cm_permissions = [
            'add_blogpost',
            'change_blogpost',
            'delete_blogpost'
        ]

        for perm in cm_permissions:
            permission = Permission.objects.get(
                codename=perm,
                content_type=blog_content_type
            )
            cm_group.permissions.add(permission)

        self.stdout.write(self.style.SUCCESS('Groups created successfully'))
