from django.core.management.base import BaseCommand , CommandError
from clubs.models import Club

class Command(BaseCommand):
	def handle(self,*args,**options):
		clubs =(
            'GFG',
            'Technovation',
            'Codechef',
            'Culturalclub',
            'GDSC',
            'Samvad',
			)
		count=0
		for club in clubs:
			if Club.objects.filter(name=club).exists():
				pass
			else:
				Club.objects.create(name=club)
				count += 1
		self.stdout.write(self.style.SUCCESS(f"Clubs populated successfully"))
		self.stdout.write(self.style.SUCCESS(f"{count} clubs created"))
		self.stdout.write(self.style.SUCCESS(f"total interests: {Club.objects.all().count()}"))

