"""
Unit tests for module currency

When run as a script, this module invokes several procedures that test
the various functions in the module currency.

Author: Derek Palmer
Date:   01/03/2022
"""

import introcs
import currency


def test_before_space():
    """
    Test procedure for before_space
    """
    print('Testing before_space')
    
    result = currency.before_space('dollars and cents')
    introcs.assert_equals('dollars', result)

    result = currency.before_space(' dollars')
    introcs.assert_equals('', result)

    result = currency.before_space('dollars ')
    introcs.assert_equals('dollars', result)

    result = currency.before_space('d o l l a r s')
    introcs.assert_equals('d', result)

    result = currency.before_space('d o  l l a r s')
    introcs.assert_equals('d', result)

    result = currency.before_space(' ')
    introcs.assert_equals('', result)

    result = currency.before_space('dollars cents')
    introcs.assert_equals('dollars', result)

    result = currency.before_space('  dollars')
    introcs.assert_equals('', result)


def test_after_space():
    """
   Test procedure for after_space
    """
    print('Testing after_space')
    result = currency.after_space('dollars and cents')
    introcs.assert_equals('and cents', result)

    result = currency.after_space(' dollars')
    introcs.assert_equals('dollars', result)

    result = currency.after_space('dollars ')
    introcs.assert_equals('', result)

    result = currency.after_space('d o l l a r s')
    introcs.assert_equals('o l l a r s', result)

    result = currency.after_space('d o  l l a r s')
    introcs.assert_equals('o  l l a r s', result)

    result = currency.after_space(' ')
    introcs.assert_equals('', result)

    result = currency.after_space('dollars cents')
    introcs.assert_equals('cents', result)

    result = currency.after_space('  dollars')
    introcs.assert_equals(' dollars', result)


def test_first_inside_quotes():
    """
        Test procedure for first_inside_quotes
    """
    print('Testing first_inside_quotes')

    result = currency.first_inside_quotes('request""')
    introcs.assert_equals('', result)

    result = currency.first_inside_quotes('request"s"')
    introcs.assert_equals('s', result)

    result = currency.first_inside_quotes('"r"equest"s"')
    introcs.assert_equals('r', result)

    result = currency.first_inside_quotes('"request"')
    introcs.assert_equals('request', result)


def test_get_src():
    """
       Test procedure for get_src
    """
    print('Testing get_src')

    result = currency.get_src('{"success": true, "src": "2 United States Dollars",' +\
     '"dst": "1.772814 Euros", "error": ""}')
    introcs.assert_equals('2 United States Dollars',result)

    result = currency.get_src('{"success": true, "src":"2 United States Dollars",' +\
    '"dst": "1.772814 Euros", "error": ""}')
    introcs.assert_equals('2 United States Dollars',result)

    result = currency.get_src('{"success":false,"src":"","dst":"",' +\
    '"error":"Source currency code is invalid."}')
    introcs.assert_equals('',result)

    result = currency.get_src('{"success":false,"src": "","dst":"",' +\
    '"error":"Source currency code is invalid."}')
    introcs.assert_equals('',result)


def test_get_dst():
    """
    Test procedure for get_dst
    """
    print('Testing get_dst')

    
    result = currency.get_dst('{"success": true, "src": "2 United States Dollars",' +\
     '"dst":"1.772814 Euros", "error": ""}')
    introcs.assert_equals('1.772814 Euros',result)

    result = currency.get_dst('{"success": true, "src":"2 United States Dollars",' +\
     '"dst": "1.772814 Euros", "error": ""}')
    introcs.assert_equals('1.772814 Euros',result)

    result = currency.get_dst('{"success":false,"src":"","dst":"",' +\
    '"error":"Source currency code is invalid."}')
    introcs.assert_equals('',result)

    result = currency.get_dst('{"success":false,"src": "",' +\
    '"dst": "","error":"Source currency code is invalid."}')
    introcs.assert_equals('',result)


def test_has_error():
    """
    Test procedure for has_error
    """
    print('Testing has_error')

    result = currency.has_error('{"success": true, "src": "2 United States Dollars",' +\
    ' "dst": "1.772814 Euros", "error":""}')
    introcs.assert_false(result)

    result = currency.has_error('{"success": true, "src": "2 United States Dollars",' +\
     '"dst": "1.772814 Euros", "error": ""}')
    introcs.assert_false(result)

    result = currency.has_error('{"success":true, "src": "2 United States Dollars",' +\
    '"dst": "1.772814 Euros", "error": ""}')
    introcs.assert_false(result)

    result = currency.has_error('{"success":false,"src":"","dst":"",' +\
    '"error":"Source currency code is invalid."}')
    introcs.assert_true(result)

    result = currency.has_error('{"success":false,"src": "","dst": "",' +\
    '"error":"Source currency code is invalid."}')
    introcs.assert_true(result)

    result = currency.has_error('{"success":false,"src": "","dst": "",' +\
    '"error": "Source currency code is invalid."}')
    introcs.assert_true(result)


def test_service_response():
    """
    Test procedure for service_response
    """
    print('Testing service_response')

    result = currency.service_response('USD','EUR',2.5)
    introcs.assert_equals('{"success": true, "src": "2.5 United States Dollars", '+\
    '"dst": "2.2160175 Euros", "error": ""}',result)

    result = currency.service_response('USD','BAA',50)
    introcs.assert_equals('{"success": false, "src": "", "dst": "", ' +\
    '"error": "The rate for currency BAA is not present."}',result)

    result = currency.service_response('BAA','BTC',50)
    introcs.assert_equals('{"success": false, "src": "", "dst": "", ' +\
    '"error": "The rate for currency BAA is not present."}',result)

    result = currency.service_response('BTC','EUR',-50)
    introcs.assert_equals('{"success": true, "src": "-50.0 Bitcoins", ' +\
    '"dst": "-495800.68969671766 Euros", "error": ""}',result)


def test_iscurrency():
    """
   Test procedure for iscurrency
    """
    print('Testing iscurrency')

    result = currency.iscurrency('BTC')
    introcs.assert_true(result)

    result = currency.iscurrency('BAA')
    introcs.assert_false(result)


def test_exchange():
    """
    Test procedure for exchange
    """
    print('Testing exchange')

    result = currency.exchange('BTC','USD', 10)
    introcs.assert_floats_equal(111867.50323422936,result)

    result = currency.exchange('BTC','USD', -10)
    introcs.assert_floats_equal(-111867.50323422936,result)


test_before_space()
test_after_space()
test_first_inside_quotes()
test_get_src()
test_get_dst()
test_has_error()
test_service_response()
test_iscurrency()
test_exchange()
print('All tests completed successfully')