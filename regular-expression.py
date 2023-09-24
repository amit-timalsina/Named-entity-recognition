import re

def find_greeting(text):
    """
    Return greeting string ("Hi", "Hello", etc) if greeting pattern matches
    """
    greeting_pattern = r'^(Hi|Hello|Yo)*'
    match = re.match(greeting_pattern, text, re.IGNORECASE)
    if match:
        return match.group()

if __name__ == "__main__":
    print(find_greeting("Hi Mr. Yann!"))
    print(find_greeting("Hello, marie"))
    print(find_greeting("Hello"))
    print(find_greeting("hello!"))
    print(find_greeting("Helloworld"))
