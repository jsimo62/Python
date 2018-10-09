def main():
    family_heights =[30, 40, 55, 62, 72, 65]
    tallest = max(family_heights)
    print("the tallest is ", tallest)

def max(heights):
    max_height = heights[0]
    for height in heights:
        if height > max_height:
            max_height = height
    return max_height

main()
