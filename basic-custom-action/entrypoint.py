import os

def main():
    message = os.getenv("MY_MESSAGE")
    print(message)

if __name__ == "__main__":
    main()