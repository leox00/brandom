from requests import get

def randint(min: int = 1, max: int = 10, quantity: int = 1):
    url = f"https://www.random.org/integers/?num={quantity}&min={min}&max={max}&col=5&base=10&format=plain&rnd=new"
    print(get(url).text)