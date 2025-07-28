def bake_time_ramining(expected_bake_time, preparation_time):
    return expected_bake_time - preparation_time

bread = bake_time_ramining(60, 20)
print(bread)