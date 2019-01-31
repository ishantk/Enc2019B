pixel1 = [111, 0, 222]
pixel2 = [123, 111, 223]
pixel3 = [157, 235, 0]
pixel4 = [111, 0, 222]
pixel5 = [123, 111, 223]
pixel6 = [157, 235, 0]
pixel7 = [111, 0, 222]
pixel8 = [123, 111, 223]
pixel9 = [157, 235, 0]

# photo = [[pixel1, pixel2, pixel3], [pixel4, pixel5, pixel6], [pixel7, pixel8, pixel9]]
# List of List of Lists
photo = [ [[111, 0, 222], [123, 111, 223], [157, 235, 0]],
          [[111, 0, 222], [123, 111, 223], [157, 235, 0]],
          [[111, 0, 222], [123, 111, 223], [157, 235, 0]]
          ]
# [111, 0, 222] -> (111 + 0 + 222) // 3 -> 111 -> [111, 111, 111]

print(len(photo))
print(len(photo[0]))
print(len(photo[0][0]))
print(photo[0][0][1])

# GrayScale the Above Photo
# Rotate Above Photo to 90 Degree Right Side