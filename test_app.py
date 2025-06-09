from app import greet

def test_greet():
    print("Success in the workflow run")
    assert greet() == 7

test_greet()
    
