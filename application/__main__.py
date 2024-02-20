import requests
from get_functions import get_VEP, get_VR, get_VV
from helper_functions import user_input, get_requests, get_allele, get_hgvsg


def Redirect():
    '''allows variant recoder function to be called based on user input'''
        
    datatype = user_input.datatype()
    species = user_input.species()
    variant = user_input.variant()
    if datatype == 'E' or datatype == 'e':
        response = get_VR.VariantRecorder(species, variant) 
        content = response.json()
        allele_list = get_allele.get_allele(content)
        no_of_allele = len(allele_list)
        allele_choice = user_input.allele(no_of_allele, allele_list, variant)
        hgvsg = get_hgvsg.get_hgvsg(allele_choice, content)
           
    elif datatype == 'R' or datatype == 'r':
        genome_build = user_input.genomebuild()
        select_transcripts = user_input.select_transcript()
        response = get_VV.VariantValidator(genome_build, variant, select_transcripts) 
        content = response.json()
        key = content[variant]['primary_assembly_loci'][genome_build]
        hgvsg = list(key.items())[0][1]
           
    else:
        error = {'error': 'please enter a valid database E or R'}
        return error
    vep = get_VEP.VariantEPredictor(species, hgvsg)
    return vep  



 
if __name__ == "__main__":
    
    
  
    
   
    response = Redirect()
    

  


   
    print('-\n-----------------------------------RESULTS---------------------------------------------------\n')
    print('\n---------status code-------------\n',  '\n', response.status_code)
    print('\n----------headers-------------\n','\n', response.headers)
    print('\n---------text---------------\n','\n', response.text)
    print('\n-----------json----------\n', '\n', response.json()) 
    print('\n-----------url----------\n', '\n', response.url)
  
  

