import unittest
from unittest import mock
#from application import get_functions
from application.get_functions import get_VR, get_VV, get_VEP
from application.helper_functions import get_requests, user_input


class TestVR(unittest.TestCase):
        '''testing Variant Recoder function'''
        def test_vr_class(self):
        
        # Simulate a GET request to /variant_recoder/human/ENST00000366667:c.803C>T
                self.response = get_VR.VariantRecoder('human', "  rs769506022")
                # Check the status code
                self.assertEqual(self.response.status_code, 200)
                content = self.response.json()
                self.assertEqual(len(content), 1)
                self.assertEqual(self.response.headers['Content-Type'], 'application/json')
                self.assertEqual(content[0]['input'], 'rs769506022')
                self.assertIn('T', content)
                self.assertIsInstance(content, dict)    
                self.assertIsInstance(content, list)

class TestVV(unittest.TestCase):
        '''testing Variant validator function'''
        def test_vv_class(self):
        
                # Simulate a GET request to http://rest.variantvalidator.org/VariantValidator/variantvalidator/hg38/NM_001384479.1:c.803C>T/mane
                self.response = get_VV.VariantValidator('hg38', "NM_001384479.1:c.803C>T", "mane")
                # Check the status code
                self.assertEqual(self.response.status_code, 200)
                content = self.response.json()
                self.assertEqual(len(content), 3) 
                self.assertEqual(self.response.headers['Content-Type'], 'application/json')

class TestVariantEPredictorClass(unittest.TestCase):               
        '''testing the variant effect predictor function'''
        def test_vep_class(self):
                # Simulate a GET request to https://rest.ensembl.org/vep/human/hgvs/NC_000001.11:g.230710021G%3EA/
                # ?refseq=True&dbscSNV=True&variant_class=True&Conservation=True&ccds=True&dbNSFP=REVEL_score ###
                self.response = get_VEP.VariantEPredictor("human", "NC_000001.11:g.230710021G>A")
                # Check the status code
                self.assertEqual(self.response.status_code, 200)
                content = self.response.json()
                self.assertEqual(len(content), 1) #check if the length of the content is 1
                self.assertEqual(self.response.headers['Content-Type'], 'application/json')
                self.assertEqual(content[0]['input'], 'NC_000001.11:g.230710021G>A') #check if the input key matches NC_000001.11:g.230710021G>
                self.assertIsInstance(content, list) #check if the response is a list

class TestgetClass(unittest.TestCase):
      '''tests the get request functions'''
      def vr_requests(self):
                self.url = f"https://rest.ensembl.org/variant_recoder/human/rs769506022/"
                self.response = get_requests.request_vrdata(self.url)
                self.assertEqual(self.response.headers['Content-Type'], 'application/json')
                content = self.response.json()
                self.assertEqual(len(content), 1)


class TestUserInputClass(unittest.TestCase):
       '''tests the functions with user inputs'''
       @mock.patch('user_input.datatype.input', create=True)  #use mock.patch decorator to stimulate user input
       def test_datatype(self, mocked_input):   
                mocked_input.side_effect = ['t', 'e', 'R'] #allows you to state multiple results that can be tested
                actual_input = user_input.datatype() #calls the datatype function and uses the mocked input as the user input
                expected_input = ['e', 'E'] 
                self.assertEqual(actual_input, expected_input) #tests if the mocked input is equal to the expected input
        
 
        

      



if __name__ == '__main__':
    unittest.main()