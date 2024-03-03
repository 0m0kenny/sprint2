def get_allele(vr_response):
    ''' iterates over response from variant recoder to get list of alleles present'''
    keys = [] # Create empty list to add each allele
    
    # Iterate over each dictionary in the json response
    for dictionary in vr_response:
        for key in dictionary: # Iterate over each key in each dictionary
            keys.append(key) # Add each key (allele) to the keys list
                                               
        return keys