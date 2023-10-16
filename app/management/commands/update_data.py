import os
import csv
from django.conf import settings
from django.core.management.base import BaseCommand
from app.models import Cell


class Command(BaseCommand):

    def handle(self, *args, **options):
        file_path = os.path.join(settings.BASE_DIR, 'data', 'enrichment_val.txt')
        counter = 0
        with open(file_path, 'r', newline='') as file:
            reader = csv.DictReader(file, delimiter='\t')
            next(reader)
            for row in reader:
                gene = int(row['GENE'])

                for i in range(0, 461):
                    cluster = str(row[f'Cluster{i}'])
                    cell = Cell.objects.filter(gene=gene, cluster=i)
                    if cell.exists():
                        cell=cell.first()
                        cell.enrichment_val = cluster
                        cell.save()

                        print(i, cell, flush=True)

                counter += 1
                print('Fin Row', counter, flush=True)

        self.stdout.write('Finished!')
