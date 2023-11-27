import os
import numpy as np
import pandas as pd
from django.conf import settings
from django.core.management.base import BaseCommand
from sqlalchemy import create_engine
from app.models import Cell, Phenotype


class Command(BaseCommand):

    def handle(self, *args, **options):
        engine = create_engine(
            f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('POSTGRES_HOST', 'localhost')}:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"
        )

        if Cell.objects.all().count() == 0:
            print('Cell models data inserting started. . .')
            tsv_file_path = os.path.join(settings.BASE_DIR, 'data')
            fields = ['Name', 'GENE', 'CHR',	'START',	'STOP',	'NSNPS',	'NPARAM',	'N',	'ZSTAT',	'SCZ_2022_P',	'SCZ_2018_P',	'SCZ_2014_P',	'SCZ_2011_P',	'alcohol_2022_P',	'MS_2018_P',	'sleep_2019_P',	'ALZ_2022_P',	'PTSD_2023_P',
                      'BMI_2018_P', 'CIG_2022_P', 'MDD_2023_P',	'MDD_2019_P',	'ADHD_2019_P',	'AN_2019_P',	'ASD_2017_P',	'BIP_2021_P',	'EDUC_2018_P',	'HGT_2018_P',	'INTEL_2018_P', 'NEURO_2018_P',	'SPE_RANK',	'SPE_VAL', 'GENE_EXP', 'Enrichment_score']

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

        if Phenotype.objects.all().count() == 0:
            print('Phenotype models data inserting started. . .')
            xlsx_file_path = os.path.join(settings.BASE_DIR, 'data')

            excel_file = pd.ExcelFile(f'{xlsx_file_path}/supplementary.xlsx')

            sheet_count = 0
            for sheet in excel_file.sheet_names:
                fields = ['Cluster', 'sig1_and_cond2_and_none0', 'TYPE', 'NGENES', 'BETA', 'BETA_STD', 'SE', 'P',
                          'Supercluster', 'Class_auto_annotation',
                          'Neurotransmitter_auto_annotation', 'Neuropeptide_auto_annotation',
                          'Subtype_auto_annotation', 'Transferred_MTG_Label', 'Top_three_regions',
                          'Top_three_dissections', 'Top_Enriched_Genes', 'Number_of_cells',
                          'Doublet_Finder_score', 'Total_UMI', 'Fraction_unspliced',
                          'Fraction_mitochondrial', 'H19_30_002', 'H19_30_001', 'H18_30_002',
                          'H18_30_001', 'Fraction_cells_from_top_donor', 'Number_of_dissections',
                          'Top_dissection_percentage', 'Dissections']

                if sheet_count != 0:
                    df = excel_file.parse(sheet)
                    print('\n===================================\n', df, flush=True)
                    print('\n===================================\n', df.columns, flush=True)
                    print('\n===================================\n', sheet_count, flush=True)

                    if sheet_count == 1:
                        fields.remove('sig1_and_cond2_and_none0')
                    elif sheet_count == 2:
                        fields.remove('sig1_and_cond2_and_none0')
                        fields.remove('Top_three_dissections')
                        fields.remove('Number_of_dissections')
                        fields.remove('Top_dissection_percentage')
                    elif sheet_count == 3:
                        fields.remove('sig1_and_cond2_and_none0')
                        fields.remove('Top_three_dissections')
                        fields.remove('Number_of_dissections')
                        fields.remove('Top_dissection_percentage')
                    elif sheet_count == 4:
                        fields.remove('Subtype_auto_annotation')
                        fields.remove('Top_three_regions')
                        fields.remove('Top_three_dissections')
                        fields.remove('Top_Enriched_Genes')
                        fields.remove('Number_of_cells')
                        fields.remove('Dissections')
                    elif sheet_count == 5:
                        fields.remove('Top_three_regions')
                        fields.remove('Top_three_dissections')
                        fields.remove('Top_Enriched_Genes')
                        fields.remove('Dissections')


                    df = df[fields]

                    df.columns = df.columns.str.lower()
                    df.insert(0, 'sheet', sheet_count)

                    print('\n===================================\n', df.columns, flush=True)

                    try:
                        df.to_sql('app_phenotype', con=engine,
                                if_exists='append', index=False, method='multi')
                    except Exception as e:
                        print(f"Error writing sheet {sheet} to SQL: {e}")

                sheet_count += 1

        self.stdout.write('Finished!')
