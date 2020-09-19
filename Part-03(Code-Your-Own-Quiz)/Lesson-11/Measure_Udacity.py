def measure_udacity(u):
    count = 0
    for e in u:
        if e[0] == "U":
            count = count + 1
    return count
print(measure_udacity(["Su","Moe","Hlaing"]))
print(measure_udacity(["Umika","Ubato"]))
print(measure_udacity(["Udacity","United State","union","u2"]))
