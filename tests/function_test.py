from variant_annotator.__main__ import Redirect
from unittest.mock import patch
import pytest
from variant_annotator.helper_functions import output

# Stimulate multiple user input required by the Redirect function
@patch('builtins.input', side_effect=['E', 'human', 'rs769506022', 'A'])
def test_redirect_with_vr(mocked_input):
    '''tests the Redirect function as if variant recoder was called'''
    response = Redirect() # Call the function
    content = response.json() # Convert response to json
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'
    assert content[0]['input'] == 'NC_000001.11:g.230703164C>A'

# Stimulate multiple user input required by the Redirect function
@patch('builtins.input', side_effect=['R','human', 'NM_001384479.1:c.803C>T', 'hg38', 'mane'])
def test_redirect_with_vv(mocked_input):
    '''tests the function as if variantvalidator was called'''
    response = Redirect()
    content = response.json() # Convert response to json
    assert response.status_code == 200
    # Declare parts of the response url as a variable
    url = '''=True&dbscSNV=True&variant_class=True&Conservation=True&ccds=True&dbNSFP=REVEL_score'''
    assert url in response.url # Check if the url match parts of the url in response.url
    assert content[0]['allele_string'] == 'G/A'


@patch('builtins.input', side_effect=['R','human', 'rss87', 'hg38', 'mane'])
def test_vv_error(mocked_input, monkeypatch, capsys):
    '''tests the Redirect function to see if error raised for wrong variant/select_transcript input'''
    # Checks if function raises error and prompts user again due to while True looping construct in function
    with pytest.raises(StopIteration): 
        response = Redirect() # Call the redirect function
        assert response.status_code == 200
        captured = capsys.readouterr() # Capture the message printed on Stdout
        assert "Error: The variant 'rss87' and/or select_transcript 'mane' you entered is not valid"  in captured.out
    


@patch('builtins.input', side_effect=['R','huma', 'NM_001384479.1:c.803C>T', 'hg38', 'mane', 'text/xml'])
def test_species_input(mocked_input, capsys):
    '''tests the Redirect function to see if error raised for wrong species input'''
    with pytest.raises(StopIteration): #checks if function raises system exit error
        response = Redirect()
        assert response.status_code == 200
        captured = capsys.readouterr()
        assert "Can not find internal name for species 'huma'"  in captured.out

@patch('builtins.input', side_effect=['R','human', 'NM_001384479.1:c.803C>T', 'hg38', 'mane'])
def test_output(mocked_input, capsys, monkeypatch):
    '''test the output function'''
    # Call the Redirect function for use as arg in output function
    response = Redirect()
    # Stimulate user input
    monkeypatch.setattr('builtins.input', lambda x: "text/xml")
    # Call the output function using returned Redirect response as arg
    output.output(response)
    # Check that the headers is changed to match the user input - text/xml
    assert response.headers['Content-Type'] == 'text/xml'
    captured = capsys.readouterr() # Capture the printed response on Stdout
    # Check that the output function correctly converts the response from Redirect to text/xml
    assert 'text/xml' in captured.out
    assert "b'<?xml version=" in captured.out