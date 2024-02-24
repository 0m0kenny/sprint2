import requests
from get_functions import get_VEP, get_VR, get_VV
from helper_functions import user_input, get_requests, get_allele, get_hgvsg, representations
import logging
from logging import handlers
import dicttoxml




#configure logger
logging.basicConfig(filename= "applog.log", level=logging.DEBUG, format="%(levelname)s -- %(asctime)s -- %(funcName)s -- %(message)s" )
#create logger object for main script
logger_main = logging.getLogger(__name__)

#create rotating file handler to use disk space more efficiently
file_handler = handlers.RotatingFileHandler('applog.log', maxBytes=500000, backupCount=2)
file_handler.setLevel(logging.DEBUG)
logger_main.addHandler(file_handler)
dicttoxml.LOG.setLevel(logging.ERROR) #dicttoxml generates too much info tags so set log level to error to avoid this 















def Redirect():
    '''allows variant recoder function to be called based on user input'''  
    #create logger info message once script is run
    logger_main.info('Starting Application')
    while True:    
        datatype = user_input.datatype()
        species = user_input.species()
        variant = user_input.variant()    
        
        try:
            if datatype == 'E' or datatype == 'e':
                
                response = get_VR.VariantRecorder(species, variant) 
                response.raise_for_status() # Raises an exception for unsuccessful HTTP status codes        
                       
                content = response.json()
                                 
                allele_list = get_allele.get_allele(content) #gets the variant allele in the response

                allele_choice = user_input.allele(len(allele_list), allele_list, variant) #asks user to choose which allele to get vep for from list of allele present
                hgvsg = get_hgvsg.get_hgvsg(allele_choice, content) #iterate over content to get the hgvsg value
                        
            elif datatype == 'R' or datatype == 'r':       
                
                genome_build = user_input.genomebuild() #collects genome_build from user
                select_transcripts = user_input.select_transcript() #collects transcripts from the user
                response = get_VV.VariantValidator(genome_build, variant, select_transcripts)
                response.raise_for_status() # Raises an exception for unsuccessful HTTP status codes 
                content = response.json() #returns a nested dict
                
                #loops through the dict to find the value hgvsg using the expected response structure                        
                key = content[variant]['primary_assembly_loci'][genome_build] #raises a key error if key not found in response
                hgvsg = list(key.items())[0][1]
        
            #collects species enetered by user and hgvsg data collected from vr or vv and sends to vep 
            response = get_VEP.VariantEPredictor(species, hgvsg)
            response.raise_for_status()
            content = response.json()

            return response        
                   
        #vv does not raise httperror if wrong variant/selecttranscript entered because status code still 200.        
        except KeyError as error: #key error raised for vv response if the variant key is not found in the response dict
            print(f"\n --- Error: The variant '{variant}' and/or select_transcript '{select_transcripts}' you entered is not valid.", 
                    '\n --- Please make sure your entries are correct and try again below ---\n')
            logger_main.exception('Unable to find variant/selecttranscript in response')                      
            continue #allows the user to start from the begining without exiting/terminating the program

        except requests.exceptions.ConnectionError: #raise exception for no internet
            print('--A connection error or timeout occurred, please check your internet connection and try again---')
            logger_main.excpetion('Connection/Timeout error')
            continue  
                         
        except  requests.exceptions.HTTPError: #raises exception for error 400 from vr or vep
            print(f"\n --- Error code: {response.status_code} ", '\n --------', response.json(), 
                      '\n --- Please make sure your entry is correct and try again below ---\n')
            logger_main.exception(f'HTTPError: {response.status_code}. Species/variant entered is wrong' )
            continue     
#create logger info message once script is finished
logger_main.info('Finished')
    
        
if __name__ == "__main__":
    
    response = Redirect()

    
    print('-\n-----------------------------------RESULTS---------------------------------------------------\n')
    print('\n---------status code-------------\n',  '\n', response.status_code)
    print('\n-----------url----------\n', '\n', response.url)
    contenttype = user_input.content_type()
    if contenttype == 'application/json':
        print('\n----------headers-------------\n','\n', response.headers)
        print('\n-----------json----------\n', '\n', response.json())  
    elif contenttype == 'text/xml':
        content = response.json()
        response.headers['content-type'] = 'text/xml'
        representations.text_xml(response, 200)
        print('\n----------headers-------------\n','\n', response.headers)
        print('\n-----------text/xml----------\n', '\n', content)
    else:
        print('\n----------headers-------------\n','\n', response.headers)
        print('\n---------text---------------\n','\n', response.text)
 

