from dicttoxml import dicttoxml


def text_xml(data):
    '''changes default datatype pf the response to text/xml'''
    resp = dicttoxml(data)
    return resp
