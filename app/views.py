from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q
from django.views.generic import TemplateView
from app.models import Cell, Phenotype
from app.utils import generate_graph


@method_decorator(login_required, name='dispatch')
class Index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        param, query, count = self.request.GET, Q(), None

        gene = param.get('gene', '')
        cluster = param.get('cluster', '')
        visualization = param.get('visualization', 'option0')
        phenotype = param.get('phenotype', '0')

        context['cluster'] = cluster
        context['visualization'] = visualization
        context['phenotype'] = phenotype
        context['gene'] = gene
        context['count'] = count
        context['cells'] = []
        context['results'] = []

        if visualization == 'option4':
            query = Phenotype.objects.filter(sheet=phenotype)
            context['count'] = query.count()
            context['results'] = query.order_by('p')
        else:

            if visualization in ['option3', 'option2']:
                if gene:
                    query.add(Q(name=gene), Q.AND)

            elif visualization == 'option1':
                if cluster:
                    query.add(Q(cluster=cluster), Q.AND)

            if not gene and not cluster:
                return context
            else:
                query = Cell.objects.filter(query).exclude(
                    spe_rank__isnull=True, spe_val__isnull=True)
                context['count'] = query.count()

            if visualization == 'option3':
                cells=query.values(
                    'cluster', 'spe_val').order_by('cluster')
                phenotype= Phenotype.objects.filter(sheet=phenotype).first()
                context['graph'] = generate_graph(cells,phenotype)

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
            context['additional_info'] = f'<div class="info-pair">Super Cluster: <span class="additional-info-sc">{super_cluster[0]}</span></div><div class="info-pair">Color: <span style="background-color:#{super_cluster[1]}" class="additional-info-color"></span></div>'
        if visualization == 'option2':
            first_item = query.first()
            context['additional_info'] = f'<div class="info-pair">Gene: <span class="additional-info-sc">{first_item.name}</span></div><div class="info-pair">P-value (schizophrenia): <span class="additional-info-sc">{first_item.scz_2022_p:.4e}</span></div><div class="info-pair">NCBI gene number: <span class="additional-info-sc">{first_item.gene}</span></div><div class="info-pair">Chromsome: <span class="additional-info-sc">{first_item.chr}</span></div><div class="info-pair">Start position: <span class="additional-info-sc">{first_item.start}</span></div><div class="info-pair">End position: <span class="additional-info-sc">{first_item.stop}</span></div><div class="info-pair">Genome build: <span class="additional-info-sc">GRCh37</span></div>'
        return context
