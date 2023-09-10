from django.db.models import Q
from django.views.generic import TemplateView
from app.models import Cell
from decimal import Decimal

class Index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        param, query, count = self.request.GET, Q(), 0

        scz_2022_p = param.get('scz_2022_p', '')
        spe_rank = param.get('spe_rank', '')
        cluster = param.get('cluster', '')
        visualization = param.get('visualization', 'option0')
        gene = param.get('gene', '')

        context['scz_2022_p'] = scz_2022_p
        context['spe_rank'] = spe_rank
        context['cluster'] = cluster
        context['visualization'] = visualization
        context['gene'] = gene
        context['count'] = count
        context['cells'] = []

        if visualization in ['option1', 'option2']:
            if scz_2022_p:
                query.add(Q(scz_2022_p_log__gte=scz_2022_p), Q.AND)

        if visualization == 'option2':
            query.add(Q(cluster=cluster), Q.AND)
            if spe_rank:
                query.add(Q(spe_rank__gte=spe_rank), Q.AND)

        if visualization == 'option3':
            if gene:
                query.add(Q(name=gene), Q.AND)

        if visualization == 'option4':
            if spe_rank and cluster:
                query.add(Q(spe_rank__gte=spe_rank, cluster=cluster), Q.AND)

        if visualization == 'option5':
            if cluster:
                query.add(Q(cluster=cluster), Q.AND)

        if not scz_2022_p and not gene and not spe_rank and not cluster:
            filtered_genes = []
        else:

            filtered_genes = Cell.objects.filter(query).exclude(spe_rank__isnull=True, spe_val__isnull=True,).values(
                'cluster', 'name', 'gene', 'spe_rank', 'scz_2022_p', 'scz_2022_p_log', 'spe_val')
            count = filtered_genes.count()

            for result in filtered_genes: # format as scientific notation
                result['scz_2022_p'] = "{:.3E}".format(Decimal(result['scz_2022_p']))

        context['count'] = count
        context['results'] = filtered_genes

        return context
