
# In the code, the function sunsetViews checks the heights of the
# buildings in the given direction ("East" or "West") and returns the sorted indices
# of the buildings that can be seen during sunset.
#
# Please note that the comment is placed above the function definition to provide an
# explanation of the code's functionality.

def sunsetViews(buildings, direction):
    final_result = []
    max_height = 0
    if direction == "East":
        for i in range(len(buildings) -1 , -1 , -1):
            if buildings[i] > max_height:
                final_result.append(i)
                max_height = buildings[i]



        return sorted(final_result)

    elif direction == "West":
        for i in range(len(buildings)):
            if buildings[i] > max_height:
                final_result.append(i)
                max_height = buildings[i]



        return sorted(final_result)






buildings = [1,2,3,4,5,6]
arash = sunsetViews(buildings,"West")
print(arash)

