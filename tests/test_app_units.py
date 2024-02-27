
from my_application.get_functions import get_VR, get_VV, get_VEP
from my_application.helper_functions import get_requests, user_input




def test_vr_class():
        '''testing Variant Recoder function'''    
        # Simulate a GET request to /variant_recoder/human/ENST00000366667:c.803C>T
        response = get_VR.VariantRecorder('human', "rs769506022")
        # Check the status code
        assert response.status_code == 200
        assert response.headers['Content-Type'] == 'application/json'
        content = response.json()
        assert len(content) == 1         
        assert 'T' in content[0].keys() #check if alllee T is present in content
        assert 'hgvsg' in content[0]['T']
        assert content[0]['A']['hgvsg'] == ['NC_000001.11:g.230703164C>A']

# def test_exceptions():
#         '''test if appropraite exceptions are raised'''
#         with pytest.raises(requests.exceptions.HTTPError):
#                 get_VR.VariantRecorder('dfghj', "rs769506022") 

# def test_exceptions():
#         '''test if appropraite exceptions are raised'''
#         response = get_VR.VariantRecorder('dfghj', "rs769506022") 
#         #response.raise_for_status()
#         with pytest.raises(requests.exceptions.HTTPError):
#               response
        




#         
def test_vv_class():
        '''testing Variant validator function'''
        # Simulate a GET request to http://rest.variantvalidator.org/VariantValidator/variantvalidator/hg38/NM_001384479.1:c.803C>T/mane
        response = get_VV.VariantValidator('hg38', "NM_001384479.1:c.803C>T", "mane")
        # Check the status code
        assert response.status_code == 200
        assert response.headers['Content-Type'] == 'application/json'
        content = response.json()
        assert len(content) == 3        
        assert 'Validation Warnings' not in content.keys() #check if no validation warning is present in content
        assert content['flag'] != ['empty results']
        
        
def test_vep_class():
        '''testing the variant effect predictor function'''       
        # Simulate a GET request to https://rest.ensembl.org/vep/human/hgvs/NC_000001.11:g.230710021G%3EA/
        # ?refseq=True&dbscSNV=True&variant_class=True&Conservation=True&ccds=True&dbNSFP=REVEL_score ###
        response = get_VEP.VariantEPredictor("human", "NC_000001.11:g.230710021G>A")
        # Check the status code
        assert response.status_code == 200
        content = response.json()        
        assert len(content) == 1 #check if the length of the content is 1
        assert content[0]['input'] == 'NC_000001.11:g.230710021G>A' #check if the input key matches NC_000001.11:g.230710021G>A
                    
def test_datatype_inputs(monkeypatch):
        '''tests the user input'''
        monkeypatch.setattr('builtins.input', lambda x: "e")
        answer = user_input.datatype()
        assert answer == 'e'        

def test_genomebuild_inputs(monkeypatch):
        '''tests the user input'''
        monkeypatch.setattr('builtins.input', lambda x: "hg38")
        answer = user_input.genomebuild()
        assert answer == 'hg38'      

def test_select_transcript_inputs(monkeypatch):
        '''tests the user input'''
        monkeypatch.setattr('builtins.input', lambda x: "all")
        answer = user_input.select_transcript()
        assert answer == 'all'        

def test_contenttype_inputs(monkeypatch):
        '''tests the user input'''
        monkeypatch.setattr('builtins.input', lambda x: "text/xml")
        answer = user_input.content_type()
        assert answer != 'application/json'
             
def test_allele_inputs(monkeypatch):
        '''tests the user input'''
        monkeypatch.setattr('builtins.input', lambda x: "t")
        answer = user_input.allele(2, ['A', 'T'], 'rs769506022')
        assert answer == 'T'       

# class TestgetClass(unittest.TestCase):
#       '''tests the get request functions'''
#       def vr_requests(self):
#                 self.url = f"https://rest.ensembl.org/variant_recoder/human/rs769506022/"
#                 self.response = get_requests.request_vrdata(self.url)
#                 self.assertEqual(self.response.headers['Content-Type'], 'application/json')
#                 content = self.response.json()
#                 self.assertEqual(len(content), 1)


# class TestUserInputClass(unittest.TestCase):
#        '''tests the functions with user inputs'''
#        @mock.patch('user_input.datatype.input', create=True)  #use mock.patch decorator to stimulate user input
#        def test_datatype(self, mocked_input):   
#                 mocked_input.side_effect = ['t', 'e', 'R'] #allows you to state multiple results that can be tested
#                 actual_input = user_input.datatype() #calls the datatype function and uses the mocked input as the user input
#                 expected_input = ['e', 'E'] 
#                 self.assertEqual(actual_input, expected_input) #tests if the mocked input is equal to the expected input
        
 
        

      



# if __name__ == '__main__':
#     unittest.main()