def test_hello_function():
    result = ""
    try:
        result = hello("Ben")
    except Exception as e:
        print("Test 01 - hello_function - failed. Reason: " + str(e))
        return
    
    expected = "Hello Ben"

    if result == expected:
        print("Test 01 - hello_function - passed. All good.")
    else:
        print("Test 01 - hello_function - failed. Reason: expected and actual result not equal.")

def test_2_hello_function():
    result = ""
    try:
        result = hello("Tom")
    except Exception as e:
        print("Test 02 - hello_function - failed. Reason: " + str(e))
        return
    
    expected = "Hello Tom"

    if result == expected:
        print("Test 02 - hello_function - passed. All good.")
    else:
        print("Test 02 - hello_function - failed. Reason: expected and actual result not equal.")

        
def hello(name):
    return "Hello " + name



test_hello_function()
test_2_hello_function()