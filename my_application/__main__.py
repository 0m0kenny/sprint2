import requests
from get_functions import get_VEP, get_VR, get_VV
from helper_functions import user_input, get_allele, get_hgvsg, output
import logging
from logging import handlers
import dicttoxml
import sys



#configure logger
logging.basicConfig(filename= "applog.log", level=logging.DEBUG, format="%(levelname)s -- %(asctime)s -- %(funcName)s -- %(message)s" )
#create logger object for main script
logger_main = logging.getLogger(__name__)

#create rotating file handler to use disk space more efficiently
file_handler = handlers.RotatingFileHandler('applog.log', maxBytes=500000, backupCount=2)
file_handler.setLevel(logging.ERROR)
logger_main.addHandler(file_handler)
dicttoxml.LOG.setLevel(logging.ERROR) #dicttoxml generates too much info tags so set log level to error to avoid this 
stderr_handler = logging.StreamHandler(sys.stderr)
stderr_handler.setLevel(logging.CRITICAL)
logger_main.addHandler(stderr_handler)





def Redirect():
    '''allows variant recoder function to be called based on user input'''  
    #create logger info message once script is run
    logger_main.info('Starting Application')
    
    while True:
        #prompt user input
        datatype = user_input.datatype()
        species = user_input.species()
        variant = user_input.variant()    
        
        try:
            if datatype == 'E' or datatype == 'e':
                
                response = get_VR.VariantRecorder(species, variant) 
                response.raise_for_status() # Raises an exception for unsuccessful HTTP status codes        
                #log exception
                logger_main.exception(f'HTTPError: {response.status_code}. Species/variant entered is wrong' )      
                content = response.json()
                
                                 
                allele_list = get_allele.get_allele(content) #gets the variant allele in the response

                allele_choice = user_input.allele(len(allele_list), allele_list, variant) #asks user to choose which allele to get vep for from list of allele present
                hgvsg = get_hgvsg.get_hgvsg(allele_choice, content) #iterate over content to get the hgvsg value
                      
            elif datatype == 'R' or datatype == 'r':       
                
                genome_build = user_input.genomebuild()  #collects genome_build from user
                select_transcripts = user_input.select_transcript()  #collects transcripts from the user
                response = get_VV.VariantValidator(genome_build, variant, select_transcripts)
                #Raises an exception for unsuccessful HTTP status codes
                response.raise_for_status()  
                content = response.json()  #returns a nested dict
                
                #loops through the dict to find the value hgvsg using the expected response structure                        
                key = content[variant]['primary_assembly_loci'][genome_build]
                #raises a key error if key not found in response
                hgvsg = list(key.items())[0][1]
            
            #collects species enetered by user and hgvsg data collected from vr or vv and sends to vep 
            response = get_VEP.VariantEPredictor(species, hgvsg)
            response.raise_for_status()
            #tries+=1
            content = response.json()
            logger_main.info('Finished')
             
            return response     
                   
                   
        #vv does not raise httperror if wrong variant/selecttranscript entered because status code still 200.        
        except KeyError: 
            #key error raised for vv response if the variant key is not found in the response dict
            print(f"\n --- Error: The variant '{variant}' and/or select_transcript '{select_transcripts}' you entered is not valid.", 
                    '\n --- Please make sure your entries are correct and try again below ---\n')
            logger_main.exception('Unable to find variant/selecttranscript in response') 
            # tries+=1                     
            continue  #allows the user to start from the begining without exiting/terminating the program
        
        #raise exception for no internet
        except requests.exceptions.ConnectionError: 
            print('--A connection error or timeout occurred, please check your internet connection and try again---')
            logger_main.exception('Connection/Timeout error')
            # tries+=1
            continue  
                         
        #except httperror 400 from vr or vep
        except requests.exceptions.HTTPError: 
            print(f"\n --- Error code: {response.status_code} ", '\n --------', response.json(), 
                      '\n --- Please make sure your entry is correct and try again below ---\n')
            #log the exception
            logger_main.exception(f'HTTPError: {response.status_code}. Species/variant entered is wrong' )
            # tries+=1
            continue
               


        
if __name__ == "__main__":
    
    #call redirect function
    response = Redirect()
    #print response according to content type chosen by user
    output.output(response) 

    
     