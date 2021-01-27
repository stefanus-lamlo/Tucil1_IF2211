import os
import time
import sys

sys.tracebacklimit = 0
file_name = input("masukkan nama file : ")
file_name = "..\\test\\"+file_name+".txt"
file_sample = open(file_name, 'r')
doc = file_sample.readlines()
kata =[] 
huruf = []
start_time = time.time()
for line in doc:
    kata.append(''.join(c for c in line if c.isalnum()))
    text = list([val for val in line.strip() if val.isalpha()])
    huruf.append(text)

sethuruf = set()
i=0
for i in range(len(huruf)):
    sethuruf.update(huruf[i])

list_huruf = (list(sethuruf))
list_huruf.sort()

jumlah_huruf = len(list_huruf)


jumlah_kata = len(kata) - 2
soal = []
jawaban = []
i=0
for i in range(jumlah_kata):
    soal.append(kata[i])

jawaban.append(kata[jumlah_kata+1])

query = ""

for i in soal:
    query += i
    query += "+"

query += jawaban[0]

counter = 0
if (jumlah_huruf==10):
    all_solutions = list()
    for l1 in range(9, -1, -1):
        for l2 in range(9, -1, -1):
            for l3 in range(9, -1, -1):
                for l4 in range(9, -1, -1):
                    for l5 in range(9, -1, -1):
                        for l6 in range(9, -1, -1):
                            for l7 in range(9, -1, -1):
                                for l8 in range(9, -1, -1):
                                    for l9 in range(9, -1, -1):
                                        for l10 in range(9, -1, -1):
                                            counter=counter+1
                                            temp = query.replace(list_huruf[0],str(l1))
                                            temp = temp.replace(list_huruf[1],str(l2))
                                            temp = temp.replace(list_huruf[2],str(l3))
                                            temp = temp.replace(list_huruf[3],str(l4))
                                            temp = temp.replace(list_huruf[4],str(l5))
                                            temp = temp.replace(list_huruf[5],str(l6))
                                            temp = temp.replace(list_huruf[6],str(l7))
                                            temp = temp.replace(list_huruf[7],str(l8))
                                            temp = temp.replace(list_huruf[8],str(l9))
                                            temp = temp.replace(list_huruf[9],str(l10))
                                            temp = temp.split("+")

                                            operan = len(temp)
                                            count = 0
                                            for i in temp:
                                                count += int(i)
                                            flag = [l1,l2,l3,l4,l5,l6,l7,l8,l9,l10]
                                            flagset = set(flag)

                                            if ((count - (2*int(temp[operan-1]))==0) and len(flagset)==10):
                                                query = query.split("+")    
                                                i = 0
                                                for i in range (operan-1):
                                                    print(query[i])
                                                print("_________+")
                                                print(query[operan-1])
                                                print()

                                                i = 0
                                                for i in range (operan-1):
                                                    print(temp[i])
                                                print("_________+")
                                                print(temp[operan-1])
                                                print()

                                                print("banyak tes untuk menemukan subtitusi angka yang benar adalah", counter)
                                                print("waktu yang dibutuhkan : --- %s seconds ---" % (time.time() - start_time))
                                                break
                                            
if (jumlah_huruf==9):
    all_solutions = list()
    for l1 in range(9, -1, -1):
        for l2 in range(9, -1, -1):
            for l3 in range(9, -1, -1):
                for l4 in range(9, -1, -1):
                    for l5 in range(9, -1, -1):
                        for l6 in range(9, -1, -1):
                            for l7 in range(9, -1, -1):
                                for l8 in range(9, -1, -1):
                                    for l9 in range(9, -1, -1):
                                        counter=counter+1
                                        temp = query.replace(list_huruf[0],str(l1))
                                        temp = temp.replace(list_huruf[1],str(l2))
                                        temp = temp.replace(list_huruf[2],str(l3))
                                        temp = temp.replace(list_huruf[3],str(l4))
                                        temp = temp.replace(list_huruf[4],str(l5))
                                        temp = temp.replace(list_huruf[5],str(l6))
                                        temp = temp.replace(list_huruf[6],str(l7))
                                        temp = temp.replace(list_huruf[7],str(l8))
                                        temp = temp.replace(list_huruf[8],str(l9))
                                        temp = temp.split("+")

                                        operan = len(temp)
                                        count = 0
                                        for i in temp:
                                            count += int(i)
                                        flag = [l1,l2,l3,l4,l5,l6,l7,l8,l9]
                                        flagset = set(flag)

                                        if ((count - (2*int(temp[operan-1]))==0) and len(flagset)==9):
                                            query = query.split("+")    
                                            i = 0
                                            for i in range (operan-1):
                                                print(query[i])
                                            print("_________+")
                                            print(query[operan-1])
                                            print()

                                            i = 0
                                            for i in range (operan-1):
                                                print(temp[i])
                                            print("_________+")
                                            print(temp[operan-1])
                                            print()

                                            print("banyak tes untuk menemukan subtitusi angka yang benar adalah", counter)
                                            print("waktu yang dibutuhkan : --- %s seconds ---" % (time.time() - start_time))
                                            break
    
if (jumlah_huruf==8):
    all_solutions = list()
    for l1 in range(9, -1, -1):
        for l2 in range(9, -1, -1):
            for l3 in range(9, -1, -1):
                for l4 in range(9, -1, -1):
                    for l5 in range(9, -1, -1):
                        for l6 in range(9, -1, -1):
                            for l7 in range(9, -1, -1):
                                for l8 in range(9, -1, -1):
                                    counter=counter+1
                                    temp = query.replace(list_huruf[0],str(l1))
                                    temp = temp.replace(list_huruf[1],str(l2))
                                    temp = temp.replace(list_huruf[2],str(l3))
                                    temp = temp.replace(list_huruf[3],str(l4))
                                    temp = temp.replace(list_huruf[4],str(l5))
                                    temp = temp.replace(list_huruf[5],str(l6))
                                    temp = temp.replace(list_huruf[6],str(l7))
                                    temp = temp.replace(list_huruf[7],str(l8))
                                    temp = temp.split("+")
                                    operan = len(temp)
                                    count = 0
                                    for i in temp:
                                        count += int(i)
                                    flag = [l1,l2,l3,l4,l5,l6,l7,l8]
                                    flagset = set(flag)

                                    if ((count - (2*int(temp[operan-1]))==0) and len(flagset)==8):
                                        query = query.split("+")    
                                        i = 0
                                        for i in range (operan-1):
                                            print(query[i])
                                        print("_________+")
                                        print(query[operan-1])
                                        print()
                                        i = 0
                                        for i in range (operan-1):
                                            print(temp[i])
                                        print("_________+")
                                        print(temp[operan-1])
                                        print()
                                        print("banyak tes untuk menemukan subtitusi angka yang benar adalah", counter)
                                        print("waktu yang dibutuhkan : --- %s seconds ---" % (time.time() - start_time))
                                        break
   
if (jumlah_huruf==7):
    all_solutions = list()
    for l1 in range(9, -1, -1):
        for l2 in range(9, -1, -1):
            for l3 in range(9, -1, -1):
                for l4 in range(9, -1, -1):
                    for l5 in range(9, -1, -1):
                        for l6 in range(9, -1, -1):
                            for l7 in range(9, -1, -1):
                                counter=counter+1
                                temp = query.replace(list_huruf[0],str(l1))
                                temp = temp.replace(list_huruf[1],str(l2))
                                temp = temp.replace(list_huruf[2],str(l3))
                                temp = temp.replace(list_huruf[3],str(l4))
                                temp = temp.replace(list_huruf[4],str(l5))
                                temp = temp.replace(list_huruf[5],str(l6))
                                temp = temp.replace(list_huruf[6],str(l7))
                                temp = temp.split("+")
                                operan = len(temp)
                                count = 0
                                for i in temp:
                                    count += int(i)
                                flag = [l1,l2,l3,l4,l5,l6,l7]
                                flagset = set(flag)

                                if ((count - (2*int(temp[operan-1]))==0) and len(flagset)==7):
                                    query = query.split("+")    
                                    i = 0
                                    for i in range (operan-1):
                                        print(query[i])
                                    print("_________+")
                                    print(query[operan-1])
                                    print()
                                    i = 0
                                    for i in range (operan-1):
                                        print(temp[i])
                                    print("_________+")
                                    print(temp[operan-1])
                                    print()
                                    print("banyak tes untuk menemukan subtitusi angka yang benar adalah", counter)
                                    print("waktu yang dibutuhkan : --- %s seconds ---" % (time.time() - start_time))
                                    break

if (jumlah_huruf==6):
    all_solutions = list()
    for l1 in range(9, -1, -1):
        for l2 in range(9, -1, -1):
            for l3 in range(9, -1, -1):
                for l4 in range(9, -1, -1):
                    for l5 in range(9, -1, -1):
                        for l6 in range(9, -1, -1):
                            counter=counter+1
                            temp = query.replace(list_huruf[0],str(l1))
                            temp = temp.replace(list_huruf[1],str(l2))
                            temp = temp.replace(list_huruf[2],str(l3))
                            temp = temp.replace(list_huruf[3],str(l4))
                            temp = temp.replace(list_huruf[4],str(l5))
                            temp = temp.replace(list_huruf[5],str(l6))
                            temp = temp.split("+")
                            operan = len(temp)
                            count = 0
                            for i in temp:
                                count += int(i)
                            flag = [l1,l2,l3,l4,l5,l6]
                            flagset = set(flag)

                            if ((count - (2*int(temp[operan-1]))==0) and len(flagset)==6):
                                query = query.split("+")    
                                i = 0
                                for i in range (operan-1):
                                    print(query[i])
                                print("_________+")
                                print(query[operan-1])
                                print()
                                i = 0
                                for i in range (operan-1):
                                    print(temp[i])
                                print("_________+")
                                print(temp[operan-1])
                                print()
                                print("banyak tes untuk menemukan subtitusi angka yang benar adalah", counter)
                                print("waktu yang dibutuhkan : --- %s seconds ---" % (time.time() - start_time))
                                break

if (jumlah_huruf==5):
    all_solutions = list()
    for l1 in range(9, -1, -1):
        for l2 in range(9, -1, -1):
            for l3 in range(9, -1, -1):
                for l4 in range(9, -1, -1):
                    for l5 in range(9, -1, -1):
                            counter=counter+1
                            temp = query.replace(list_huruf[0],str(l1))
                            temp = temp.replace(list_huruf[1],str(l2))
                            temp = temp.replace(list_huruf[2],str(l3))
                            temp = temp.replace(list_huruf[3],str(l4))
                            temp = temp.replace(list_huruf[4],str(l5))
                            temp = temp.split("+")
                            operan = len(temp)
                            count = 0
                            for i in temp:
                                count += int(i)
                            flag = [l1,l2,l3,l4,l5]
                            flagset = set(flag)

                            if ((count - (2*int(temp[operan-1]))==0) and len(flagset)==5):
                                query = query.split("+")    
                                i = 0
                                for i in range (operan-1):
                                    print(query[i])
                                print("_________+")
                                print(query[operan-1])
                                print()
                                i = 0
                                for i in range (operan-1):
                                    print(temp[i])
                                print("_________+")
                                print(temp[operan-1])
                                print()
                                print("banyak tes untuk menemukan subtitusi angka yang benar adalah", counter)
                                print("waktu yang dibutuhkan : --- %s seconds ---" % (time.time() - start_time))
                                break

if (jumlah_huruf==4):
    all_solutions = list()
    for l1 in range(9, -1, -1):
        for l2 in range(9, -1, -1):
            for l3 in range(9, -1, -1):
                for l4 in range(9, -1, -1):
                    counter=counter+1
                    temp = query.replace(list_huruf[0],str(l1))
                    temp = temp.replace(list_huruf[1],str(l2))
                    temp = temp.replace(list_huruf[2],str(l3))
                    temp = temp.replace(list_huruf[3],str(l4))
                    temp = temp.split("+")
                    operan = len(temp)
                    count = 0
                    for i in temp:
                        count += int(i)
                    flag = [l1,l2,l3,l4]
                    flagset = set(flag)

                    if ((count - (2*int(temp[operan-1]))==0) and len(flagset)==4):
                        query = query.split("+")    
                        i = 0
                        for i in range (operan-1):
                            print(query[i])
                        print("_________+")
                        print(query[operan-1])
                        print()
                        i = 0
                        for i in range (operan-1):
                            print(temp[i])
                        print("_________+")
                        print(temp[operan-1])
                        print()
                        print("banyak tes untuk menemukan subtitusi angka yang benar adalah", counter)
                        print("waktu yang dibutuhkan : --- %s seconds ---" % (time.time() - start_time))
                        break

if (jumlah_huruf==3):
    all_solutions = list()
    for l1 in range(9, -1, -1):
        for l2 in range(9, -1, -1):
            for l3 in range(9, -1, -1):
                counter=counter+1
                temp = query.replace(list_huruf[0],str(l1))
                temp = temp.replace(list_huruf[1],str(l2))
                temp = temp.replace(list_huruf[2],str(l3))
                temp = temp.split("+")
                operan = len(temp)
                count = 0
                for i in temp:
                    count += int(i)
                flag = [l1,l2,l3]
                flagset = set(flag)

                if ((count - (2*int(temp[operan-1]))==0) and len(flagset)==3):
                    query = query.split("+")    
                    i = 0
                    for i in range (operan-1):
                        print(query[i])
                    print("_________+")
                    print(query[operan-1])
                    print()
                    i = 0
                    for i in range (operan-1):
                        print(temp[i])
                    print("_________+")
                    print(temp[operan-1])
                    print()
                    print("banyak tes untuk menemukan subtitusi angka yang benar adalah", counter)
                    print("waktu yang dibutuhkan : --- %s seconds ---" % (time.time() - start_time))
                    break

if (jumlah_huruf==2):
    all_solutions = list()
    for l1 in range(9, -1, -1):
        for l2 in range(9, -1, -1):
            counter=counter+1
            temp = query.replace(list_huruf[0],str(l1))
            temp = temp.replace(list_huruf[1],str(l2))
            temp = temp.split("+")
            operan = len(temp)
            count = 0
            for i in temp:
                count += int(i)
            flag = [l1,l2]
            flagset = set(flag)

            if ((count - (2*int(temp[operan-1]))==0) and len(flagset)==2):
                query = query.split("+")    
                i = 0
                for i in range (operan-1):
                    print(query[i])
                print("_________+")
                print(query[operan-1])
                print()
                i = 0
                for i in range (operan-1):
                    print(temp[i])
                print("_________+")
                print(temp[operan-1])
                print()
                print("banyak tes untuk menemukan subtitusi angka yang benar adalah", counter)
                print("waktu yang dibutuhkan : --- %s seconds ---" % (time.time() - start_time))
                break
