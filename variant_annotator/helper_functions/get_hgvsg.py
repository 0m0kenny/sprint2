def get_hgvsg(allele_choice, vr_response):
    '''parse response from variant recoder and gets hgvsg based on allele chosen by user'''
    
    # Iterate over each dictionary in the json response
    for dictionary in vr_response:
        for key in dictionary.keys(): # Iterate over each key in each dictionary
            if key in allele_choice: # Check if key is the same as alle user input
                hgvsg = dictionary[key]['hgvsg'] # Access hgvsg value based on the allele input by user
                for a in hgvsg:
                    return str(a) # Returns the hgvsg value as a string