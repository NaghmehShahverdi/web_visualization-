from django.db import models


class Cell(models.Model):
    cluster = models.PositiveIntegerField()
    name = models.CharField(max_length=20, null=True, blank=True)
    gene = models.PositiveIntegerField(null=True, blank=True)
    chr = models.PositiveIntegerField(null=True, blank=True)
    start = models.PositiveIntegerField(null=True, blank=True)
    stop = models.PositiveIntegerField(null=True, blank=True)
    nsnps = models.PositiveIntegerField(null=True, blank=True)
    nparam = models.PositiveIntegerField(null=True, blank=True)
    n = models.IntegerField(null=True, blank=True)
    zstat = models.FloatField(null=True, blank=True)
    scz_2022_p = models.FloatField(null=True, blank=True)
    scz_2018_p = models.FloatField(null=True, blank=True)
    scz_2014_p = models.FloatField(null=True, blank=True)
    scz_2011_p = models.FloatField(null=True, blank=True)
    alcohol_2022_p = models.FloatField(null=True, blank=True)
    ms_2018_p = models.FloatField(null=True, blank=True)
    sleep_2019_p = models.FloatField(null=True, blank=True)
    alz_2022_p = models.FloatField(null=True, blank=True)
    ptsd_2023_p = models.FloatField(null=True, blank=True)
    bmi_2018_p = models.FloatField(null=True, blank=True)
    cig_2022_p = models.FloatField(null=True, blank=True)
    mdd_2023_p = models.FloatField(null=True, blank=True)
    mdd_2019_p = models.FloatField(null=True, blank=True)
    adhd_2019_p = models.FloatField(null=True, blank=True)
    an_2019_p = models.FloatField(null=True, blank=True)
    asd_2017_p = models.FloatField(null=True, blank=True)
    bip_2021_p = models.FloatField(null=True, blank=True)
    educ_2018_p = models.FloatField(null=True, blank=True)
    hgt_2018_p = models.FloatField(null=True, blank=True)
    intel_2018_p = models.FloatField(null=True, blank=True)
    neuro_2018_p = models.FloatField(null=True, blank=True)
    spe_rank = models.FloatField(null=True, blank=True)
    spe_val = models.FloatField(null=True, blank=True)
    gene_exp = models.FloatField(null=True, blank=True)

    scz_2022_p_log = models.FloatField(null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.cluster} --- {self.name} --- {self.spe_rank}'
