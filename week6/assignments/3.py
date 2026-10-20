temps = list(map(int, (input("Enter space seperated temperatues: ").strip().split())))

def highest_temp(temps, max_temp=temps[0]):
    if temps == []:
        return max_temp

    if temps[0] > max_temp:
        return highest_temp(temps[1:], temps[0])
    else:
        return highest_temp(temps[1:], max_temp)

print(highest_temp(temps))