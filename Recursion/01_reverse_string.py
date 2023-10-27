def main():
    text = input("write a sentence: ")
    print(reverse_string(text))

    
def reverse_string(text):
    if len(text) == 1:
        return(text)
    return(reverse_string(text[1:]) + text[0])
    
    
main()