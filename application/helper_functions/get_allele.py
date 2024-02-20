def get_allele(self, vr_response):
        ''' iterates over response from variant recoder to get list of alleles present'''
        self.vr_response = vr_response
        keys = [] 
       
        for dictionary in vr_response:
            for key in dictionary:
                keys.append(key)
        return keys