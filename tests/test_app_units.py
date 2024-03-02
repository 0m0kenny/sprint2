
from my_application.get_functions import get_VR, get_VV, get_VEP
from my_application.helper_functions import user_input, get_xml, get_hgvsg, get_allele
import pytest




def test_vr():
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

        
def test_vv():
        '''testing Variant validator function'''
        # Simulate a GET request to http://rest.variantvalidator.org/VariantValidator/variantvalidator/hg38/NM_001384479.1:c.803C>T/mane
        response = get_VV.VariantValidator('hg38', "NM_001384479.1:c.803C>T", "mane" )
        # Check the status code
        assert response.status_code == 200
        assert response.headers['Content-Type'] == 'application/json'
        content = response.json()
        assert len(content) == 3        
        assert 'Validation Warnings' not in content.keys() #check if no validation warning is present in content
        assert content['flag'] != ['empty results']
        
        
def test_vep():
        '''testing the variant effect predictor function'''       
        # Simulate a GET request to https://rest.ensembl.org/vep/human/hgvs/NC_000001.11:g.230710021G%3EA/
        # ?refseq=True&dbscSNV=True&variant_class=True&Conservation=True&ccds=True&dbNSFP=REVEL_score ###
        response = get_VEP.VariantEPredictor("human", "NC_000001.11:g.230710021G>A")
        # Check the status code
        assert response.status_code == 200
        content = response.json()        
        assert len(content) == 1 #check if the length of the content is 1
        assert content[0]['input'] == 'NC_000001.11:g.230710021G>A' #check if the input key matches NC_000001.11:g.230710021G>A

def test_datatype_inputs(monkeypatch, capsys):
        '''tests the user input'''
        monkeypatch.setattr('builtins.input', lambda x: "e") #susbtitutes aking for user input 
        answer = user_input.datatype()
        assert answer == 'e'        
        monkeypatch.setattr('builtins.input', lambda x: 'nothing')
        with pytest.raises(SystemExit): #checks if function raises system exit error
                user_input.datatype()   
                captured = capsys.readouterr()
                assert "---Error: Your entry 'nothing' is not valid. Please try again below---" in captured.out
                assert "Exceeded maximum number of tries. Exiting program..." in captured.out

def test_species_inputs(monkeypatch):
        '''tests the user input'''
        monkeypatch.setattr('builtins.input', lambda x: "human") #susbtitutes aking for user input 
        answer = user_input.species()
        assert answer == 'human'   

def test_selecttranscript_inputs(monkeypatch):
        '''tests the user input'''
        monkeypatch.setattr('builtins.input', lambda x: "raw") #susbtitutes aking for user input 
        answer = user_input.select_transcript()
        assert answer == 'raw' 

def test_genomebuild_inputs(monkeypatch, capsys):
        '''tests the user input'''
        monkeypatch.setattr('builtins.input', lambda x: "hg38")
        answer = user_input.genomebuild()
        assert answer == 'hg38' 
        monkeypatch.setattr('builtins.input', lambda x: 'h7')
        with pytest.raises(SystemExit): #checks if function raises system exit error
                user_input.genomebuild()   
                captured = capsys.readouterr()
                assert "---Error: Your entry 'h7' is not valid. Please try again below---" in captured.out
                assert "Exceeded maximum number of tries. Exiting program..." in captured.out   

def test_select_transcript_inputs(monkeypatch):
        '''tests the user input'''
        monkeypatch.setattr('builtins.input', lambda x: "all")
        answer = user_input.select_transcript()
        assert answer == 'all'        

def test_contenttype_inputs(monkeypatch, capsys):
        '''tests the user input'''
        monkeypatch.setattr('builtins.input', lambda x: "text/xml")
        answer = user_input.content_type()
        assert answer != 'application/json'
        monkeypatch.setattr('builtins.input', lambda x: 'nothing')
        with pytest.raises(SystemExit): #checks if function raises system exit error
                user_input.content_type()   
                captured = capsys.readouterr()
                assert "---Error: Your entry 'nothing' is not valid. Please try again below---" in captured.out
                assert "Exceeded maximum number of tries. Exiting program..." in captured.out
             
def test_allele_inputs(monkeypatch, capsys):
        '''tests the user input'''
        monkeypatch.setattr('builtins.input', lambda x: "t")
        answer = user_input.allele(2, ['A', 'T'], 'rs769506022')
        assert answer == 'T' 
        monkeypatch.setattr('builtins.input', lambda x: "w") #tests in user enteres wrong input
        with pytest.raises(SystemExit): #checks if function raises system exit error
                user_input.allele(2, ['A', 'T'], 'rs769506022')   
                captured = capsys.readouterr()
                assert "Error: Your entry 'w' is not valid. Please try again below---" in captured.out
                assert "Exceeded maximum number of tries. Exiting program..." in captured.out

def test_xml():
        '''tests the get_xml function'''
        response = get_VEP.VariantEPredictor("human", "NC_000001.11:g.230710021G>A")
        xml_data = str(get_xml.text_xml(response))
        assert "b'<?xml version=" in xml_data
   

def test_hgvsg():
        '''tests the get_hgvsg module'''
        response = get_VR.VariantRecorder('human', "rs769506022")
        content = response.json()    
        allele_choice = 'T'         
        hgvsg = get_hgvsg.get_hgvsg(allele_choice, content)
        assert hgvsg == "NC_000001.11:g.230703164C>T"
        
def test_get_allele():
        '''tests the get_allele module'''
        response = get_VR.VariantRecorder('human', "rs769506022")
        allele_list = get_allele.get_allele(response.json())
        assert isinstance(allele_list, list)
        assert 'A' in allele_list