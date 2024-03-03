import logging
import sys

# Create loggers
logger_datatype = logging.getLogger('datatype_input')
logger_genome_build = logging.getLogger('genome_build_input')
logger_allele = logging.getLogger('allele_input')
logger_content_type = logging.getLogger('content_type')


def datatype():
        '''ask user to input for the type of variant description user has'''
        # Inititate number of input tries to 0
        tries = 0
        # Iterate only 5 times if user input is wrong
        while tries < 5:
                try:
                        # Ask for user input as store as datatype
                        datatype = input('''\nWhich variant description do you have?
                        Ensemble or RefSeq? Enter E for Ensemble, R for Refsef:  ''' )

                        # Specify allowed input
                        choices = ['E', 'R']

                        # Converts user input to uppercase
                        datatype_input = datatype.upper()

                        # Check if input is in allowed list of choices 
                        if datatype_input in choices:

                               return datatype_input
                        else:
                                tries+=1 # Increment the tries by 1

                                raise ValueError

                # Handles ValueError exception
                except ValueError as e:
                        
                        # Specify Error message to be printed to Stdout
                        e = f"\n---Error: your entry '{datatype}' not valid. Please enter either E or R only---"
                        print(e)
                        # Log error
                        logger_datatype.error('user input invalid')
                        continue # Iterate the code until tries > 5
        
        # If tries > 5 print message
        print(f"\n---Exceeded maximum number of tries. Exiting program...")
        # Exit the application
        sys.exit(1)
                              
    
def species():
        '''ask user to input to get species (for variant recoder and variant effect predictor)'''

        # Ask for user input as store as species
        species = input('''\nWhich speices is variant from? eg human:  ''' )

        return species
    
def variant():
        '''ask user to input the variant description/identifier'''

        # Ask for user input as store as variant
        variant = input('''\nEnter Variant eg rs769506022, NM_001384479.1:c.803C>T :  ''' )

        return variant
    
def genomebuild():
        '''asks user to input genome build (for variant validator)'''

        # Specify allowed input
        choices = ['GRch38', 'hg38', 'GRCh37', 'hg19']

        # Inititate number of input tries to 0
        tries = 0

        # Iterate only 5 times if user input is wrong
        while tries < 5:
                try:
                        # Ask for user input as store as genome build
                        genome_build = input(f"\nEnter genome build from this list only {choices}:   ")

                        # Check if input is in allowed list of choices
                        if genome_build in choices:
                                return genome_build
                        else:
                                tries+=1 # Increment the tries by 1
                                raise ValueError

                # Handles ValueError exception
                except ValueError as e:
                        # Specify Error message to be printed to Stdout
                        e = f"\n--- Error: The genome build {genome_build} you have entered is not valid. Please try again---"
                        print(e)
                        # Log Error
                        logger_genome_build.error('User input invalid')
                        continue # Iterate the code until tries > 5

        # If tries > 5 print message
        print(f"\n---Exceeded maximum number of tries. Exiting program...")
        # Exit the application
        sys.exit(1)


def select_transcript():
        '''asks user to input select transcript (for variant validator)'''
        # Specify allowed input
        choices = ['raw', 'mane_select', 'mane', 'select', 'refseq_select']

        # Ask for user input as store as select transcript
        select_transcripts = input(f'''\n Enter transcript to return (Eg NM_001384479.1, all (for all possible transcripts),
        {choices} etc (go to 'https://variantvalidator.org/service/validate/' to see full list):  ''')
        
        return select_transcripts
    
def allele(no_of_allele, keys, variant):
        '''shows user allele variants available and asks user to choose which allele to get annotation'''
        # Inititate number of input tries to 0
        tries = 0
        # Iterate only 5 times if user input is wrong
        while tries < 5:
                try:
                        # Ask for user input as store as input allele
                        input_allele = input(f'''\n--- There are {no_of_allele} allele(s) present for the variant {variant}:
                        -These are: {keys}. Please enter which allele you want to view the vep annotation for eg A",
                        -(Note: You can only select one allele at a time):  ''')

                        #converts user input into upper case to allow iteration over response
                        allele = input_allele.upper()

                        # Check if input is in allowed list of choices which is key arg
                        if allele in keys:
                              
                                return allele
                        else:
                                tries+=1 # Increment the tries by 1
                                raise ValueError

                # Handles ValueError exception
                except ValueError as e:
                        # Specify Error message to be printed to Stdout
                        e = f"\n---Error: Your entry '{input_allele}' is not valid. Please try again below---"
                        print(e)
                        # Log Error
                        logger_allele.error('user input invalid')
                        continue # Iterate the code until tries > 5

        # If tries > 5 print message
        print(f"\n---Exceeded maximum number of tries. Exiting program...")
        # Exit the application                     
        sys.exit(1)
    
def content_type():
        '''ask user to enter what contenttype to return data'''
        # Inititate number of input tries to 0
        tries = 0
        # Iterate only 5 times if user input is wrong
        while tries < 5:
                try:
                        # Specify allowed input
                        choices = ['application/json', 'text/xml', 'text']
                        # Ask for user input as store as content type
                        content_type = input(f'''\n--- Response Successful! How should the data be returned?
                                Please select from the following options {choices}: ''')
                        if content_type in choices:
                                return content_type
                        else:
                                tries+=1 # Increment the tries by 1
                                raise ValueError

                # Handles ValueError exception
                except ValueError as e:
                        # Specify Error message to be printed to Stdout
                        e = f"\n---Error: Your entry '{content_type}' is not valid. Please try again below---"
                        print(e)
                        logger_content_type.error('user input invalid')
                        continue # Iterate the code until tries > 5

        # If tries > 5 print message
        print(f"\n---Exceeded maximum number of tries. Exiting program...")
        # Exit the application
        sys.exit(1)