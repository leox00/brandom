from requests import get

url = "https://www.random.org/integers/?num=1&min=1&max=10&col=5&base=10&format=plain&rnd=new"

def randint(min: int = 1, max: int = 10, quantity: int = 1):
    numbers = get("https://www.random.org/integers/?num={quantity}&min={min}&max={max}&col=5&base=10&format=plain&rnd=new").text
    print(numbers)

def randstr(lenght: int = 1, alphabet: str = "abcdefghijklmnopqrstuvwxyz"):
    letters = ""
    for i in range(lenght):
        number = int(get(f"https://www.random.org/integers/?num=1&min=1&max={len(alphabet)-1}&col=5&base=10&format=plain&rnd=new").text)
        letters += alphabet[number]
    print(letters)