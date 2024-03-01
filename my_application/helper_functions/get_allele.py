def get_allele(vr_response):
    ''' iterates over response from variant recoder to get list of alleles present'''
    keys = [] 
       
    for dictionary in vr_response:
        for key in dictionary:
            keys.append(key)
                                               
        return keys