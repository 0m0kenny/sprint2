import logging
import sys
logger_datatype = logging.getLogger('datatype_input')
logger_genome_build = logging.getLogger('genome_build_input')
logger_allele = logging.getLogger('allele_input')
logger_content_type = logging.getLogger('content_type')


def datatype():
        '''ask user to input for the type of variant description user has '''
        tries = 0
        while tries < 5:
                try:
                        datatype = input('''\nWhich variant description do you have?
                        ENsemble or RefSeq? Enter E for Ensemble, R for Refsef:  ''' )
                        if datatype == 'E' or datatype == 'e' or datatype == 'R' or datatype == 'r':
                               return datatype
                        else:
                                tries+=1
                                raise ValueError
                except ValueError as e:
                        e = f"\n---Error: your entry '{datatype}' not valid. Please enter either E or R only---"
                        print(e)
                        logger_datatype.error('user input invalid')
                        continue
                        
        print(f"\n---Exceeded maximum number of tries. Exiting program...")
        sys.exit(1) 
      
                              
    
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
        tries = 0
        while tries < 5:
                try:
                        genome_build = input(f"\nEnter genome build from this list only {choices}:   ")
                        if genome_build in choices: #verify if user entry is in list
                                return genome_build
                        else:
                                tries+=1
                                raise ValueError
                except ValueError as e:
                        e =f"\n--- Error: The genome build {genome_build} you have entered is not valid. Please try again---"
                        logger_genome_build.error('User input invalid')
                        continue
        print(f"\n---Exceeded maximum number of tries. Exiting program...")
        sys.exit(1) #exits program if user enters wrongly 5 times
   
def select_transcript():
        '''asks user to input select transcript (for variant validator)'''
        choices = ['raw', 'mane_select', 'mane', 'select', 'refseq_select']

        select_transcripts = input(f'''\n Enter transcript to return (Eg NM_001384479.1, all (for all possible transcripts),
        {choices} etc (go to 'https://variantvalidator.org/service/validate/' to see full list):  ''')
        return select_transcripts
    
def allele(no_of_allele, keys, variant):
        '''shows user allele variants available and asks user to choose which allele to get annotation'''
        tries = 0
        
        while tries < 5: #gives user only five tries
                try:
                        input_allele = input(f'''\n--- There are {no_of_allele} allele(s) present for the variant {variant}:
                        -These are: {keys}. Please enter which allele you want to view the vep annotation for eg A", 
                        -(Note: You can only select one allele at a time):  ''')
                        allele = input_allele.upper() #converts user input into upper case to allow iteration over response
                        if allele in keys: #verifies if the user input is in the list of keys
                              
                                return allele
                        else:
                                tries+=1
                                raise ValueError
                        
                                
                except ValueError as e:
                                e = f"\n---Error: Your entry '{input_allele}' is not valid. Please try again below---"
                                print(e)
                                logger_allele.error('user input invalid')
                                continue
                                
        print(f"\n---Exceeded maximum number of tries. Exiting program...")
        sys.exit(1)                        
       
def content_type():
        '''ask user to enter what contenttype to return data'''
        tries = 0
        while tries < 5:
                try:
                        choices = ['application/json', 'text/xml', 'text']
                        content_type = input(f'''\n--- Response Successful! How should the data be returned?
                                Please select from the following options {choices}: ''') 
                        if content_type in choices:
                                return content_type
                        else:
                                tries+=1
                                raise ValueError
                                
                except ValueError as e:
                        e = f"\n---Error: Your entry '{content_type}' is not valid. Please try again below---"
                        print(e)
                        logger_content_type.error('user input invalid')
                        continue
        print(f"\n---Exceeded maximum number of tries. Exiting program...")
        sys.exit(1) 