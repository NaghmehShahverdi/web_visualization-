from django.db.models import Q
from django.views.generic import TemplateView
from app.models import Cell
from mces.utils import generate_graph1, generate_graph2, generate_graph3, generate_graph4


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
        sort = param.get('sort')

        context['scz_2022_p'] = scz_2022_p
        context['spe_rank'] = spe_rank
        context['cluster'] = cluster
        context['visualization'] = visualization
        context['gene'] = gene
        context['sort'] = sort
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

        if not scz_2022_p and not gene and not spe_rank:
            filtered_genes = []
        else:

            if sort:
                filtered_genes = Cell.objects.filter(query).values(
                    'cluster', 'name', 'spe_rank', 'scz_2022_p_log').order_by(sort)
            else:
                filtered_genes = Cell.objects.filter(query).values(
                    'cluster', 'name', 'spe_rank', 'scz_2022_p_log')
            count = filtered_genes.count()

        if count != 0:
            if visualization == 'option1':
                graph = generate_graph1(filtered_genes)

            if visualization == 'option2':
                graph = generate_graph2(filtered_genes)

            if visualization == 'option3':
                graph = generate_graph3(filtered_genes)

            if visualization == 'option4':
                graph = generate_graph4(filtered_genes)

            context['graph'] = graph

        context['count'] = count

        return context
