import os
import numpy as np
import pandas as pd
from django.conf import settings
from django.core.management.base import BaseCommand
from sqlalchemy import create_engine


class Command(BaseCommand):

    def handle(self, *args, **options):
        tsv_file_path = os.path.join(settings.BASE_DIR, 'data')
        fields = ['Name', 'GENE', 'CHR',	'START',	'STOP',	'NSNPS',	'NPARAM',	'N',	'ZSTAT',	'SCZ_2022_P',	'SCZ_2018_P',	'SCZ_2014_P',	'SCZ_2011_P',	'alcohol_2022_P',	'MS_2018_P',	'sleep_2019_P',	'ALZ_2022_P',	'PTSD_2023_P',
                  'BMI_2018_P', 'CIG_2022_P', 'MDD_2023_P',	'MDD_2019_P',	'ADHD_2019_P',	'AN_2019_P',	'ASD_2017_P',	'BIP_2021_P',	'EDUC_2018_P',	'HGT_2018_P',	'INTEL_2018_P', 'NEURO_2018_P',	'SPE_RANK',	'SPE_VAL', 'GENE_EXP','Enrichment_score']

        engine = create_engine(
            f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('POSTGRES_HOST', 'localhost')}:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"
        )

        last_id = 0
        for cluster in range(0, 461):
            df = pd.read_csv(f'{tsv_file_path}/Cluster_{cluster}.tsv', sep='\t')
            df.columns = df.columns.str.replace('.', '_')
            df = df[fields]
            df['scz_2022_p_log'] = -np.log10(df['SCZ_2022_P'])
            df.columns = df.columns.str.lower()
            df.insert(0, 'id', range(last_id + 1, last_id + 1 + len(df)))
            last_id = df['id'].iloc[-1]
            df.insert(1, 'cluster', cluster)

            df.to_sql('app_cell', con=engine, if_exists='append', index=False, method='multi')

            print(f'Cluster_{cluster}.tsv of 460', ' ', ' Inserted.')

        self.stdout.write('Finished!')
