import logging

logger_datatype = logging.getLogger('datatype_input')
logger_genome_build = logging.getLogger('genome_build_input')
logger_allele = logging.getLogger('allele_input')
logger_content_type = logging.getLogger('content_type')


def datatype():
        '''ask user to input for the type of variant description user has '''
        while True:
                datatype = input('''\nWhich variant description do you have?
                    ENsemble or RefSeq? Enter E for Ensemble, R for Refsef:  ''' )
                if datatype == 'E' or datatype == 'e' or datatype == 'R' or datatype == 'r':
                        break
                else: 
                        print(f"\n---Error: your entry '{datatype}' not valid. Please enter either E or R only---")
                        logger_datatype.error('user input invalid')
                        continue
                
        return datatype
      
                              
    
def species():
        '''ask user to input to get species (for variant recoder and variant effect predictor)'''
        species = input('''\nWhich speices is variant from? eg human:  ''' )
        return  species
    
def variant():
        '''ask user to input for the variant description/identifier'''
        variant = input('''\nEnter Variant eg rs769506022, NM_001384479.1:c.803C>T :  ''' )
        return variant
    
def genomebuild():
        '''asks user to input genome build (for variant validator)'''
        choices = ['GRch38', 'hg38', 'GRCh37', 'hg19'] #list of entries allowed
        while True:
                genome_build = input(f"\nEnter genome build from this list only {choices}:   ")
                if genome_build in choices: #verify if user entry is in list
                        break 
                else:
                        print(f"\n--- Error: The genome build {genome_build} you have entered is not valid. Please try again---")
                        logger_genome_build.error('User input invalid')
                        continue
        return genome_build
   
def select_transcript():
        '''asks user to input select transcript (for variant validator)'''
        choices = ['raw', 'mane_select', 'mane', 'select', 'refseq_select']

        select_transcripts = input(f'''\n Enter transcript to return (Eg NM_001384479.1, all (for all possible transcripts),
        {choices} etc (go to 'https://variantvalidator.org/service/validate/' to see full list):  ''')
        return select_transcripts
    
def allele(no_of_allele, keys, variant):
        '''shows user allele variants available and asks user to choose which allele to get annotation'''
        
        while True:
                input_allele = input(f'''\n--- There are {no_of_allele} allele(s) present for the variant {variant}:
                -These are: {keys}. Please enter which allele you want to view the vep annotation for eg A", 
                -(Note: You can only select one allele at a time):  ''')
                allele = input_allele.upper() #converts user input into upper case to allow iteration over response
                if allele in keys: #verifies if the user input is in the list of keys
                        break 
                else:
                        print(f"\n---Error: Your entry '{input_allele}' is not valid. Please try again below---")
                        logger_allele.error('user input invalid')
                        continue
        return allele
def content_type():
        '''ask user to enter what contenttype to return data'''
        while True:
                choices = ['application/json', 'text/xml', 'text']
                content_type = input(f'''\n--- Response Successful! How should the data be returned?
                             Please select from the following options {choices}: ''') 
                if content_type in choices:
                        break
                else:
                        print(f"\n---Error: Your entry '{content_type}' is not valid. Please try again below---")
                        logger_content_type.error('user input invalid')
                        continue
        return content_type