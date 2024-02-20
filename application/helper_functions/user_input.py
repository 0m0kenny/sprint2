def datatype():
        '''ask user to input for the type of variant description user has '''
        datatype = input('''Which variant description do you have?
                    ENsemble or RefSeq? Enter E for Ensemble, R for Refsef:  ''' )
        return datatype 
    
def species():
        '''ask user to input to get species (for variant recoder and variant effect predictor)'''
        species = input('''Which speices is variant from? eg human: ''' )
        return  species
    
def variant():
        '''ask user to input for the variant description/identifier'''
        variant = input('''Enter Variant eg rs769506022, NM_001384479.1:c.803C>T  :  ''' )
        return variant
    
def genomebuild():
        '''asks user to input genome build (for variant validator)'''
        genome_build = input("Enter genome build eg hg38:   ")
        return genome_build
   
def select_transcript():
        '''asks user to input select transcript (for variant validator)'''
        select_transcripts = input('''Enter transcript to return (Eg NM_001384479.1, all (for all possible transcripts)
        mane, NM_001384479.1 etc: ''')
        return select_transcripts
    
def allele(no_of_allele, keys, variant):
        '''shows user allele variants available and asks user to choose which allele to get annotation'''
        input_allele = [input(f'''there are {no_of_allele} alleles present for variant {variant}:
        These are: {keys}, please enter which allele you want to view vep for eg A - for all variants''')]
        return input_allele
