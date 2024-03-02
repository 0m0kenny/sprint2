from my_application.__main__ import Redirect
from unittest.mock import patch
import pytest
from my_application.helper_functions import output


@patch('builtins.input', side_effect=['E', 'human', 'rs769506022', 'A'])
def test_redirect_with_vr(mocked_input):
    '''tests the function as if variant recoder was called'''
    response = Redirect()
    content = response.json()
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'
    assert content[0]['input'] == 'NC_000001.11:g.230703164C>A'

@patch('builtins.input', side_effect=['R','human', 'NM_001384479.1:c.803C>T', 'hg38', 'mane'])
def test_redirect_with_vv(mocked_input):
    '''tests the function as if variantvalidator was called'''
    response = Redirect()
    content = response.json()
    assert response.status_code == 200
    url = '''=True&dbscSNV=True&variant_class=True&Conservation=True&ccds=True&dbNSFP=REVEL_score'''
    assert url in response.url
    assert content[0]['allele_string'] == 'G/A'

@patch('builtins.input', side_effect=['R','human', 'rss87', 'hg38', 'mane'])
def test_vv_error(mocked_input, monkeypatch, capsys):
    '''tests the function to see if error raised for wrong variant'''
    with pytest.raises(StopIteration): #checks if function raises error and prompts user again
        response = Redirect()
        assert response.status_code == 200  
        captured = capsys.readouterr()
        assert "Error: The variant 'rss87' and/or select_transcript 'mane' you entered is not valid"  in captured.out
    


@patch('builtins.input', side_effect=['R','huma', 'NM_001384479.1:c.803C>T', 'hg38', 'mane', 'text/xml'])
def test_species_input(mocked_input, capsys):
    '''tests if wrong species input raises error'''
    with pytest.raises(StopIteration): #checks if function raises system exit error
        response = Redirect()
        assert response.status_code == 200  
        captured = capsys.readouterr()
        assert "Can not find internal name for species 'huma'"  in captured.out

@patch('builtins.input', side_effect=['R','human', 'NM_001384479.1:c.803C>T', 'hg38', 'mane'])
def test_output(mocked_input, capsys, monkeypatch):
    '''test the output function'''
    response = Redirect()
    monkeypatch.setattr('builtins.input', lambda x: "text/xml")
    output.output(response)
    assert response.headers['Content-Type'] == 'text/xml'
    captured = capsys.readouterr()
    assert 'text/xml' in captured.out
    assert "b'<?xml version=" in captured.out
   
