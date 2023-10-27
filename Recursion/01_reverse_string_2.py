def main():
    text = "Postavíme Karlštejn"
    text_list = [x for x in text]
    print(text_list)
    reverse(text_list, 0, len(text_list)-1)
    print(text_list)
    
def reverse(text_list, left, right):
    if left > right:
        return
    text_list[left], text_list[right] = text_list[right], text_list[left]
    reverse(text_list, left+1, right-1)
    
    
main()