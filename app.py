def hello():
    return "Hello from Jenkins CI/CD Pipeline!"

def add(a, b):
    return a + b

if __name__ == "__main__":
    print(hello())
    print(f"2 + 3 = {add(2, 3)}")
