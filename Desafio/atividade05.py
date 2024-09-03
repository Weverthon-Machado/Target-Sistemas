def inverter_string(s):
    s_invertida = ""
    for i in range(len(s) - 1, -1, -1):  
        s_invertida += s[i]  
    return s_invertida


string_original = "exemplo de string"

string_invertida = inverter_string(string_original)

print("String original:", string_original)
print("String invertida:", string_invertida)
