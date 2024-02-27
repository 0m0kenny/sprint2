from helper_functions import get_requests

def VariantEPredictor(species, hgvs_notation): #allows options to be optional
        '''Determines the effect of the variant on gene, transcript, protein and regulaotry regions'''

        url = f"https://rest.ensembl.org/vep/{species}/hgvs/{hgvs_notation}/"
        
        return get_requests.request_vepdata(url) 