# reversa a string using for loop

text="python"

reverse_text=""

for i in range(len(text)-1,-1,-1):
    reverse_text=text[i]
    
    print(reverse_text)
    
# Explanation:

# len(text) - 1 → last index (which is 5)

# -1 → loop ends before this index (i.e., 0 will be included)

# -1 → step is negative (moving backwards)

# So this range(5, -1, -1) gives: 5, 4, 3, 2, 1, 0