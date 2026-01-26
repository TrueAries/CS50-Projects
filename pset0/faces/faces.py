def main():
    text = input("Enter Text: ")
    result = convert(text)
    print(result)
    
def convert(text):
    text = text.replace(":)", "😊")
    text = text.replace(":(", "😞")
    return text

if __name__ == "__main__":
    main()

