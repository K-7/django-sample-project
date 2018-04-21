from django.core.management.base import BaseCommand
from users.models import UserProfile, Gallery


class Command(BaseCommand):
    help = 'Add User and Image data into database'

    def handle(self, *args, **options):
        """ Add a SuperUser and a normal user
        Add gallery of photos and description
        """
        user = None
        try:
            user = UserProfile.objects.get(username='admin@k2a.in')
        except UserProfile.DoesNotExist:
            user = UserProfile.objects.create_superuser('admin@k2a.in', 'admin@k2a.in', 'admin')

        try:
            user = UserProfile.objects.get(username='me@k2a.in')
        except UserProfile.DoesNotExist:
            user = UserProfile.objects.create(
                username='me@k2a.in',
                phno='1234567891',
                email='me@k2a.in',
                first_name='Admin User'
            )
            user.set_password('1234')
            user.save()

        gallery_list = [
            {
                'title':'Winc',
                'short_description': 'Wines that delight you',
                'filename': 'p11.jpeg'
            },
            {
                'title':'Oyo',
                'short_description': 'Beds that comfort you',
                'filename': 'p22.jpeg'
            },
            {
                'title':'AirBnb',
                'short_description': 'Houses that Bring Joy',
                'filename': 'p33.jpeg'
            },
            {
                'title':'Tamara',
                'short_description': 'ultimate Relaxation. Resort & Spa',
                'filename': 'p44.jpeg'
            },
            {
                'title':'Coorg Cliff',
                'short_description': 'Best of coorg that gives warmth and comfort',
                'filename': 'p11.jpeg'
            },
            {
                'title':'Baby Cottage',
                'short_description': 'Service Apartment',
                'filename': 'p22.jpeg'
            }
        ]

        for gallery in gallery_list:
            try:
                gallery = Gallery.objects.get(title=gallery['title'])
            except:
                gallery = Gallery.objects.create(
                    photo_filename = gallery['filename'],
                    short_description = gallery['short_description'],
                    title = gallery['title'],
                    user = user
                )
                gallery.save()







