from requests import get

url = "https://www.random.org/integers/?num=1&min=1&max=10&col=5&base=10&format=plain&rnd=new"

def randint(min: int = 1, max: int = 10, quantity: int = 1):
    number = get(f"https://www.random.org/integers/?num={quantity}&min={min}&max={max}&col=5&base=10&format=plain&rnd=new").text
    print(number)

def randstr(lenght: int = 1, alphabet: str = "abcdefghijklmnopqrstuvwxyz"):
    letters = ""
    for i in range(lenght):
        number = int(get(f"https://www.random.org/integers/?num=1&min=1&max={len(alphabet)-1}&col=5&base=10&format=plain&rnd=new").text)
        letters += alphabet[number]
    print(letters)

def randbool(quantity: int = 1):
    for i in range(quantity):
        number = int(get(f"https://www.random.org/integers/?num=1&min=0&max=1&col=5&base=10&format=plain&rnd=new").text)
        if number == 0:
            print(False)
        elif number == 1:
            print(True)
        else:
            raise ValueError(number)