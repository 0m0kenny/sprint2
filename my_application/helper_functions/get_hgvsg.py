def get_hgvsg(allele_choice, vr_response):
    '''parse response from variant recoder and gets hgvsg based on allele chosen by user'''
    for allele in vr_response:
        for key in allele.keys():
            if key in allele_choice:
                hgvsg = allele[key]['hgvsg'] #access hgvsg value based on the allele input by user
                for a in hgvsg:
                    return str(a) #returns the input as a string