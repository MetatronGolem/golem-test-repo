import subprocess
import sys

def test_hello():
    # Run the hello.py script and capture output
    result = subprocess.run([sys.executable, "hello.py"], capture_output=True, text=True)
    
    # Check if output is as expected
    assert result.stdout.strip() == "Hello World"
    print("Test passed!")

if __name__ == "__main__":
    test_hello()
