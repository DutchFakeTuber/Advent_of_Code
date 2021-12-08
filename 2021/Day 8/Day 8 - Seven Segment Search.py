from Seven_Segment_Search import DATA

def getData(data: str, beforePipe=False) -> list:
    splitPipe: list = [[pipe for pipe in line.split(' | ')] for line in data.split('\n')]
    letters: list = [[string for string in characters[1].split()] for characters in splitPipe]
    print(letters)

def main() -> None:
    getData(DATA)

if __name__ == "__main__":
    main()