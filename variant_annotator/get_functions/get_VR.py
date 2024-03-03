from helper_functions import get_requests


def VariantRecorder(species, id):
        '''Translate a variant identifier, HGVS notation or genomic SPDI notation to 
        all possible variant IDs, HGVS and genomic SPDI'''
        # Specify the url to request data from
        url = f"https://rest.ensembl.org/variant_recoder/{species}/{id}/"
       
        return get_requests.request_vrdata(url)