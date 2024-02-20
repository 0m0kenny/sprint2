import requests


def request_vvdata(url):
        '''get request for variant validator'''
        return requests.get(url)
    
def request_vrdata(url):
        '''get requests on variant recoder'''
        return requests.get(url, params={"fields" : 'hgvsg'}, headers={ "Content-Type" : "application/json"}) 

def request_vepdata(url):
        '''get requests on variant effect predictor'''
        return requests.get(url, params={"refseq" : 'True', "dbscSNV" : "True", "variant_class" : "True",
                                           "Conservation" : "True", "ccds": "True", "dbNSFP" : "REVEL_score" }, 
                                           headers={ "Content-Type" : "application/json"})   