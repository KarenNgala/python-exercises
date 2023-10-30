# Find largest alphabet that appears in a string, S
# in both lower and upper case

# if no such character, output NO

def largest_alphabet(S):
    arr = []
    for char in S:
        arr.append(char)

    characters = []
    for i in arr:
        if i.lower() in S and i.upper() in S:        
            characters.append(i)
        
    if len(characters) > 0:
        print(max(characters))
    else:
        print("NO") 



largest_alphabet("aabcdwWefD")
largest_alphabet("Codility")