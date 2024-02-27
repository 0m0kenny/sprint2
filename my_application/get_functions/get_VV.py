from helper_functions import get_requests


def VariantValidator(genome_build, variant_description, select_transcripts):
        '''Validates syntax and parameters of variant descriptions according to HGVS'''
               
        url = f"http://rest.variantvalidator.org/VariantValidator/variantvalidator/{genome_build}/{variant_description}/{select_transcripts}"
        
        return get_requests.request_vvdata(url)