from app import greet

def test_greet():
    print("Success in the workflow run")
    assert greet() == "Hello, CI/CD!"
    
