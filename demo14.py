CP = [180, 170, 330, 450, 59, 160, 720, 830] #cp
SP = [100, 200, 300, 400, 500, 600, 700, 800] #s
Z=zip(CP,SP)
for CP,SP in Z:
    if CP>SP:
        x=CP-SP
        print("loss:",x)
    elif SP>CP:
        y=SP-CP
        print("profit:",y)





