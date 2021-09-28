
numbers = [76, 83, 16, 69, 52, 78, 10, 77, 45, 52, 32, 17, 58, 54, 79, 72, 55, 50, 81, 74, 45, 33, 38, 10, 40, 44, 70, 81, 79, 28, 83, 41, 14, 16, 27, 38, 20, 84, 24, 50, 59, 71, 1, 13, 56, 91, 29, 54,
           65, 23, 60, 57, 13, 39, 58, 100000, 94, 94, 42, 46, 58, 59, 29, 69, 60, 83, 9, 83, 5, 64, 70, 55, 89, 67, 89, 70, 8, 90, 17, 48, 17, 94, 18, 98, 72, 96, 26, 13, 7, 58, 67, 38, 48, 43, 98, 65, 8, 74, 44, 92]


words = ["PoGo", "Spange", "Lie-Fi"]
definitions = ["Slang for Pokemon Go", "To collect spare change, either from couches, passerbys on the street or any numerous other ways and means",
               "When your phone or tablet indicates that you are connected to a wireless network, however you are still unable to load webpages or use any internet services with your device"]


dictionary = {}
for x in range(0, 3):
    dictionary[words[x]] = definitions[x]
    print(dictionary)
