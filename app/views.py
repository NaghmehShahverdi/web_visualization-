from decimal import Decimal
from django.db.models import Q
from django.views.generic import TemplateView
from app.models import Cell
from app.utils import generate_graph


class Index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        param, query, count = self.request.GET, Q(), None

        gene = param.get('gene', '')
        cluster = param.get('cluster', '')
        visualization = param.get('visualization', 'option0')

        context['cluster'] = cluster
        context['visualization'] = visualization
        context['gene'] = gene
        context['count'] = count
        context['cells'] = []
        context['results'] = []

        if visualization in ['option3', 'option2']:
            if gene:
                query.add(Q(name=gene), Q.AND)

        if visualization == 'option1':
            if cluster:
                query.add(Q(cluster=cluster), Q.AND)

        if not gene and not cluster:
            return context
        else:
            query = Cell.objects.filter(query).exclude(
                spe_rank__isnull=True, spe_val__isnull=True)
            context['count'] = query.count()



        if visualization == 'option3':
            context['graph'] = generate_graph(query.values(
                'cluster', 'spe_val').order_by('cluster'))

        else:
            context['results'] = query.order_by('-spe_val')

        context['columns_desc'] = {
            "cluster": "description for cluster . . .",
            "gene_number": "description for gene_number . . .",
            "specificity_rank": "description for specificity_rank . . .",
            "specificity_value": "description for specificity_value . . .",
            "super_cluster": "description for super_cluster . . .",
            "color": "description for color . . .",
            "name": "description for name . . .",
            "p_value": "description for p_value . . .",
            "enrichment_score": "description for enrichment_score . . .",
        }
        if visualization == 'option1':
            super_cluster = str(query.first().get_cluster_display()).split('#')
            context['additional_info'] = f'<b>Super Cluster: </b><span class="additional-info-sc">{super_cluster[0]}</span><b>Color: </b><span style="background-color:#{super_cluster[1]}" class="additional-info-color"></span>'

        return context
