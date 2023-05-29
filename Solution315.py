for _ in range(int(input())):
    n = input()
    cu = list(n)
    if n == "1" or n == "3" or n == "5" or n == "7" or n == "9":
        cu[0] = str(int(cu[0]) + 1)
    else:
        for i in range(len(cu)-1):
            if cu[i] == "9":
                for j in range(i, len(cu)):
                    cu[j] = "8"
                break
            elif int(cu[i]) % 2:
                if int("".join(cu[i+1:])) > int("4"*len(cu[i+1:])):
                    cu[i] = str(int(cu[i]) + 1)
                    for j in range(i + 1, len(cu)):
                        cu[j] = "0"
                else:
                    cu[i] = str(int(cu[i]) - 1)
                    for j in range(i + 1, len(cu)):
                        cu[j] = "8"
                break
        if int(cu[-1]) % 2:
            cu[-1] = str(int(cu[-1])-1)
    print("Case #"+str(_+1)+":", abs(int(n) - int("".join(cu))))
