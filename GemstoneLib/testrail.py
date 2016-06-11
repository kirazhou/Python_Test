#
# TestRail API binding for Python 2.x (API v2, available since 
# TestRail 3.0)
#
# Learn more:
#
# http://docs.gurock.com/testrail-api2/start
# http://docs.gurock.com/testrail-api2/accessing
#
# Copyright Gurock Software GmbH. See license.md for details.
#

import urllib2
import json
import base64
import sys
import os

'''
1	Passed
2	Blocked
3	Untested (not allowed when adding a result)
4	Retest
5	Failed
'''

# Offical API
# http://docs.gurock.com/testrail-api2/bindings-python#examplepost_request

# API for add result
# http://docs.gurock.com/testrail-api2/reference-results#add_result_for_case

#e example
# https://github.com/diro/robot-testrail

class _APIClient:
    def __init__(self, base_url):
        self.user = ''
        self.password = ''
        if not base_url.endswith('/'):
            base_url += '/'
        self.__url = base_url + 'index.php?/api/v2/'

        #test result status
        self.passed = 1
        self.blocked = 2
        self.untested = 3
        self.retest = 4
        self.failed = 5

    #
    # Send Get
    #
    # Issues a GET request (read) against the API and returns the result
    # (as Python dict).
    #
    # Arguments:
    #
    # uri                 The API method to call including parameters
    #                     (e.g. get_case/1)
    #
    def send_get(self, uri):
        return self.__send_request('GET', uri, None)

    #
    # Send POST
    #
    # Issues a POST request (write) against the API and returns the result
    # (as Python dict).
    #
    # Arguments:
    #
    # uri                 The API method to call including parameters
    #                     (e.g. add_case/1)
    # data                The data to submit as part of the request (as
    #                     Python dict, strings must be UTF-8 encoded)
    #
    def send_post(self, uri, data):
        return self.__send_request('POST', uri, data)

    def __send_request(self, method, uri, data):
        url = self.__url + uri
        request = urllib2.Request(url)
        if (method == 'POST'):
            request.add_data(json.dumps(data))
        auth = base64.b64encode('%s:%s' % (self.user, self.password))
        request.add_header('Authorization', 'Basic %s' % auth)
        request.add_header('Content-Type', 'application/json')

        e = None
        try:
            response = urllib2.urlopen(request).read()
        except urllib2.HTTPError as e:
            response = e.read()

        if response:
            result = json.loads(response)
        else:
            result = {}

        if e != None:
            if result and 'error' in result:
                error = '"' + result['error'] + '"'
            else:
                error = 'No additional error message received'
            raise _APIError('TestRail API returned HTTP %s (%s)' % (e.code, error))

        return result

    #
    # Send POST
    #
    # Issues a POST request (write) against the API and returns the result
    # (as Python dict).
    #
    # Arguments:
    #
    # uri                 The API method to call including parameters
    #                     (e.g. add_case/1)
    # data                The data to submit as part of the request (as
    #                     Python dict, strings must be UTF-8 encoded)
    #
    def send_add_result_for_case(self, test_run_id, test_case_id, data):
        uri = 'add_result_for_case/' + test_run_id + '/' + test_case_id
        return self.__send_request('POST', uri, data)

    # def __send_request(self, method, uri, data):
    #     url = self.__url + uri
    #     request = urllib2.Request(url)
    #     if (method == 'POST'):
    #         request.add_data(json.dumps(data))
    #     auth = base64.b64encode('%s:%s' % (self.user, self.password))
    #     request.add_header('Authorization', 'Basic %s' % auth)
    #     request.add_header('Content-Type', 'application/json')
    #
    #     e = None
    #     try:
    #         response = urllib2.urlopen(request).read()
    #     except urllib2.HTTPError as e:
    #         response = e.read()
    #
    #     if response:
    #         result = json.loads(response)
    #     else:
    #         result = {}
    #
    #     if e != None:
    #         if result and 'error' in result:
    #             error = '"' + result['error'] + '"'
    #         else:
    #             error = 'No additional error message received'
    #         raise _APIError('TestRail API returned HTTP %s (%s)' % (e.code, error))
    #
    #     return result


testrail_client = _APIClient('http://172.17.3.70/testrail')
testrail_client.user = 'yigang.tao@Istuary.com'
testrail_client.password = 'w0KB294#!RG33e|y'


class _APIError(Exception):
    pass
