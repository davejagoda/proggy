#!/usr/bin/env python3

def extract_response(response, response_type):
    assert(2 == len(response))
    assert(200 == response['ResponseMetadata']['HTTPStatusCode'])
    results = response[response_type]
    assert(list == type(results))
    return(results)

if '__main__' == __name__:
    print('aws_lib called directly')
