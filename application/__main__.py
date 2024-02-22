import requests
from get_functions import get_VEP, get_VR, get_VV
from helper_functions import user_input, get_requests, get_allele, get_hgvsg
import sys

def Redirect():
    '''allows variant recoder function to be called based on user input'''
    while True:    
        datatype = user_input.datatype()
        species = user_input.species()
        variant = user_input.variant()    
        
        try:
            if datatype == 'E' or datatype == 'e':
                
                response = get_VR.VariantRecorder(species, variant) 
                response.raise_for_status() # Raises an exception for unsuccessful HTTP status codes        
                       
                content = response.json()                  
                allele_list = get_allele.get_allele(content, variant, species) #gets the variant allele in the response
                    
                no_of_allele = len(allele_list)
                allele_choice = user_input.allele(no_of_allele, allele_list, variant) #asks user to choose which allele to get vep for from list of allele present
                hgvsg = get_hgvsg.get_hgvsg(allele_choice, content) #iterate over content to get the hgvsg value
                        
            elif datatype == 'R' or datatype == 'r':       
                
                genome_build = user_input.genomebuild() #collects genome_build from user
                select_transcripts = user_input.select_transcript() #collects transcripts from the user
                response = get_VV.VariantValidator(genome_build, variant, select_transcripts)
                response.raise_for_status() # Raises an exception for unsuccessful HTTP status codes 
                content = response.json() #returns a nested dict
                
                #loops through the dict to find the value hgvsg using the expected response structure                        
                key = content[variant]['primary_assembly_loci'][genome_build]
                hgvsg = list(key.items())[0][1]
        
            #collects species enetered by user and hgvsg data collected from vr or vv and sends to vep 
            response = get_VEP.VariantEPredictor(species, hgvsg)
            content = response.json()
            if response.status_code == 400: #catches any error not caught by other exceptions
                print(response.text)
            #response.raise_for_status() 
            else:
                   return response                   
                
        except KeyError: #raises a key error for vv response if the variant key is not found in the response dict
            print(f'''---Error: The variant '{variant}' / transcript '{select_transcripts}' you entered is not valid. 
        Please make sure the variant description is from Refseq and transcript is correct and try again---''')
                                   
            continue #allows the user to start from the begining without exiting/terminating the program

        except requests.exceptions.ConnectionError: #raise exception for no internet
            print('--A connection error or timeout occurred, please check your internet connection and try again---')
  
            continue  
                         
        except  requests.exceptions.HTTPError: #raises exception for error 400
            if datatype == 'E' or datatype == 'e':
                print(f'''---Error: The variant '{variant}' and/or species '{species}' you entered is not valid. 
                    Please make sure you entered the right variant identifier and/or species---''')
            elif datatype == 'R' or datatype == 'r':
                print(f'''---Error: The variant {variant} / transcript {select_transcripts} / species '{species}' you entered is not valid. 
                    Please make sure the variant description is from Refseq and the species / transcript is correct and try again---''')
            continue     
    
    
        
if __name__ == "__main__":
    
    response = Redirect()

    #print(type(response))
    print('-\n-----------------------------------RESULTS---------------------------------------------------\n')
    print('\n---------status code-------------\n',  '\n', response.status_code)
    print('\n----------headers-------------\n','\n', response.headers)
    print('\n---------text---------------\n','\n', response.text)
    print('\n-----------json----------\n', '\n', response.json()) 
    print('\n-----------url----------\n', '\n', response.url)
  
  

