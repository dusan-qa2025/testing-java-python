def test_hello_function():
    pass

def test_hello_function():
    result = hello("Ben")

def test_hello_function():
    result = ""
    try:
        result = hello("Ben")
    except Exception as e:
        print("Test 01 - hello_function - failed. Reason: " + str(e))
        return
    
def hello(name):
    pass

def test_hello_function():
    result = ""
    try:
        result = hello("Ben")
    except:
        print("Test 01 - hello_function - failed. Reason: no function to test.")
        return
    
    expected = "Hello Ben";

    if result == expected:
        print("Test 01 - hello_function - passed. All good.")
    else:
        print("Test 01 - hello_function - failed. Reason: Expected and actual result not equal.")
    
def hello(name):
    return "Hello Ben"

def hello(name):
    return "Hello" + name


test_hello_function()