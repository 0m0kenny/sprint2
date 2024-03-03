from helper_functions import get_requests

def VariantEPredictor(species, hgvs_notation):
        '''Determines the effect of the variant on gene, transcript, protein and regulaotry regions'''
        # Specify the url to request data from
        url = f"https://rest.ensembl.org/vep/{species}/hgvs/{hgvs_notation}/"
        
        return get_requests.request_vepdata(url)