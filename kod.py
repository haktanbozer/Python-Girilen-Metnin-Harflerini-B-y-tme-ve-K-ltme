def degistir():
    string = input("Bir metin girin: ")
    print("Girilen metin:", string)
    newstring = ""

    for string_index in range(len(string)):
        if string_index % 2 == 0:
            newstring += string[string_index].upper()
        else:
            newstring += string[string_index].lower()

    print("Dönüştürülen metin:", newstring)

degistir()
