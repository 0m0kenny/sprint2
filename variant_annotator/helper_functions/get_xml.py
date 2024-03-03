from dicttoxml import dicttoxml


def text_xml(data):
    '''changes default datatype of the vep response to text/xml'''
    # Convert the vep response to text/xml using dicttoxml function
    resp = dicttoxml(data)
    return resp
