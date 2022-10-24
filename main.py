#urllip, !request!
import requests
import json

translate = {"super effective": 2, "normal effective": 1, "not very effective": 0.5, "no effect": 0}
attacks = {}
data = requests.get("https://raw.githubusercontent.com/yorkcshub/Miscellanous/master/effectiveness.json")
data_json = json.loads(data.text)


for power in data_json:
    for attacker in data_json[power]:
        temp = attacks.get(attacker, {})
        for defender in data_json[power][attacker]:
            temp[defender] = translate[power]
        attacks[attacker]=temp

def attack(p1, p2, list_pok):
    list_pok = list_pok.split(",")
    t1 = []
    t2 = []
    t1b = 0
    t2b = 0
    #print(list_pok)
    for i in range(0,p1):
        t1.append(list_pok[i])
    for i in range(0,p2):
        t2.append(list_pok[i+p1])
    #print(list_pok)
    #print(t1)
    #print(t2)
    for i in t1:
        for j in t2:
            i2 = i.split()
            j2 = j.split()
            temp2 = []
            for x in i2:
                temp = []
                for y in j2:
                    temp.append(attacks[x][y])
                result = 1
                for n in temp:
                    result = result * n
                temp2.append(result)
            t1b += max(temp2)
    for i in t2:
        for j in t1:
            i2 = i.split()
            j2 = j.split()
            temp2 = []
            for x in i2:
                temp = []
                for y in j2:
                    temp.append(attacks[x][y])
                result = 1
                for n in temp:
                    result = result * n
                temp2.append(result)
            t2b += max(temp2)
    if t1b > t2b:
        return t1b, t2b, "ME"
    elif t1b < t2b:
        return t1b, t2b, "FOE"
    else:
        return t1b, t2b, "EQUAL"

print(attack(2,6,"Psychic Dark,Fire,Ghost Ice,Fairy Electric,Normal Steel,Ghost,Poison Fire,Dark Bug"))






