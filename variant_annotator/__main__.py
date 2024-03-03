import requests
from get_functions import get_VEP, get_VR, get_VV
from helper_functions import user_input, get_allele, get_hgvsg, output
import logging
from logging import handlers
import dicttoxml
import sys



# Configure logger
logging.basicConfig(filename= "applog.log", level=logging.DEBUG, format="%(levelname)s -- %(asctime)s -- %(funcName)s -- %(message)s" )
# Create logger object for main script
logger_main = logging.getLogger(__name__)

# Create rotating file handler to use disk space more efficiently
file_handler = handlers.RotatingFileHandler('applog.log', maxBytes=500000, backupCount=2)
# Set file log level
file_handler.setLevel(logging.ERROR)
# Set file_handler as handler
logger_main.addHandler(file_handler)

# dicttoxml generates too much info tags so set log level to error to avoid this
dicttoxml.LOG.setLevel(logging.ERROR)
# Set stream handlers and level
stderr_handler = logging.StreamHandler(sys.stderr)
stderr_handler.setLevel(logging.CRITICAL)
logger_main.addHandler(stderr_handler)



def Redirect():
    '''allows variant recoder function to be called based on user input'''
    # Create logger info message once script is running
    logger_main.info('Starting Application')
    
    while True:
        # Prompt user input
        datatype = user_input.datatype()
        species = user_input.species()
        variant = user_input.variant()  
        
        try:
            if datatype == 'E':

                # Make requests to Rest ensemble variant recoder api
                response = get_VR.VariantRecorder(species, variant)
                response.raise_for_status() # Raise an exception for unsuccessful HTTP status codes     
                # Log Exception
                logger_main.exception(f'HTTPError: {response.status_code}. Species/variant entered is wrong' )
                # Convert response to json
                content = response.json()
                
                # Parse response to retrieve allele
                allele_list = get_allele.get_allele(content)

                # Asks user to choose allele fron list
                allele_choice = user_input.allele(len(allele_list), allele_list, variant)

                # Iterate over content to get the hgvsg value
                hgvsg = get_hgvsg.get_hgvsg(allele_choice, content)
                      
            elif datatype == 'R':
                # Make requests to Variant validator api
                # Ask user for genome_build and select transcripts
                genome_build = user_input.genomebuild()
                select_transcripts = user_input.select_transcript()
                # Make requests to Variant validator api
                response = get_VV.VariantValidator(genome_build, variant, select_transcripts)

                # Raise an exception for unsuccessful HTTP status codes
                response.raise_for_status()

                # Convert response to json
                content = response.json()
                
                # Loops through content to find the hgvsg value using the expected response structure
                # Raises a key error if key not found in response         
                key = content[variant]['primary_assembly_loci'][genome_build]
                hgvsg = list(key.items())[0][1]
            
            # Collects species enetered by user and hgvsg data collected from vr or vv
            # and makes requests to rest ensemble vep
            response = get_VEP.VariantEPredictor(species, hgvsg)
            response.raise_for_status()
            content = response.json()

            # Create logger info message once script is has finished running
            logger_main.info('Finished')
             
            return response     
                   
                   
        # vv does not raise httperror if wrong variant/selecttranscript entered because status code still 200.
        # but response structure will be different so key error raised
        except KeyError:
            # Key error raised for vv response if the variant key is not found in the response dict
            print(f"\n --- Error: The variant '{variant}' and/or select_transcript '{select_transcripts}' you entered is not valid.",
                    '\n --- Please make sure your entries are correct and try again below ---\n')
            
            # Log exception
            logger_main.exception('Unable to find variant/selecttranscript in response')

            continue  # Allows the user to start from the begining without needing to exit/terminate the program
        
        # ConnectionError exception
        except requests.exceptions.ConnectionError: 
            print('--A connection error or timeout occurred, please check your internet connection and try again---')

            # Log excpetion
            logger_main.exception('Connection/Timeout error')

            continue  # Allows the user to start from the begining without needing to exit/terminate the program
                         
        # Except httperror 400 from vr or vep
        except requests.exceptions.HTTPError:
            print(f"\n --- Error code: {response.status_code} ", '\n --------', response.json(),
                      '\n --- Please make sure your entry is correct and try again below ---\n')
            
            # Log the exception
            logger_main.exception(f'HTTPError: {response.status_code}. Species/variant entered is wrong' )

            continue # Allows the user to start from the begining without needing to exit/terminate the program
               


        
if __name__ == "__main__":
    
    # Call redirect function
    response = Redirect()

    # Print response according to content type chosen by user
    output.output(response)

    
     