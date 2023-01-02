# Most of the code was provided by @wanderer04
import json
import csv
import pandas

with open('PATH FOR credentials.txt') as f:
    f = f.readlines()
x = input("Enter username\n")+'\n' == f[0]
y = input("Enter password\n") == f[1]
meta = json.load(open('PATH FOR meta.json'))


if x and y:
    #Ask for booking, cancellation or exit
    file=open("reservation.txt", 'w')
    regular, tatkal, seat = meta['regular'], meta['tatkal'], 15
    passenger_data = []
    while True:
        choice1=int(input())    
        if choice1==1:
            choice2=input()     
            n=int(input())      
            if choice2=='A':
                regular-=n
            elif choice2=='B':
                tatkal-=n
            sufficient_seats=True
            if regular < 0 or tatkal < 0:
                sufficient_seats=False
                file.write("\ninsuffient seats!!! Try for other dates...\n")
            else:
                file.write("\nRemaining Seats:\n")
                file.write("Regular = {}\n".format(regular))
                file.write("Tatkal = {}\n".format(tatkal))
                file.write("Passenger Name - Age - Source - Destination - Seat No\n")
            data=[]
            for i in range(n):
                data1=input().split(',')
                name=data1[0].strip()
                age=int(data1[1].strip())
                data.append((name, age))
            destination=input()
            date=input() # DD-MM-YY
            if sufficient_seats:
                total_fare=0
                for data1 in data:
                    name, age = data1[0], data1[1]
                    file.write("{} - {} - Bengaluru - {} - {}\n".format(name, age, destination, seat))
                    seat-=1
                    fares= meta['ticket-prices']
                    fare=fares[destination]
                    if age>=60: # Senior citizen
                        fare*=0.9
                    if choice2=='B':
                        fare+=100
                    total_fare+=fare
                    passenger_data.append((name, age, choice2, fare, date))
                file.write("Date of Journey: {}\n".format(date))
                file.write("total fare = Rs. {}\n".format(total_fare))            
        elif choice1==2:
            name=input()
            age=int(input())
            canc_date=input()
            passenger=0
            for row in passenger_data:
                if row[0]==name and row[1]==age:
                    passenger=row
                    break
            if passenger[2]=='A':
                regular+=1
            elif passenger[2]=='B':
                tatkal+=1
            file.write("\nRemaining Seats:\n")
            file.write("Regular = {}\n".format(regular))
            file.write("Tatkal = {}\n".format(tatkal))
            file.write("No. of Passessngers to Cancel = 1\n")
            file.write("Cancelled Passenger Name = {}\n".format(name))
            file.write("Cancelled Passenger Age = {}\n".format(age))
            days=int(passenger[-1][:2])-int(canc_date[:2])
            fare=passenger[-2]
            if days>=20:
                refund=fare*meta['cncl']['20d']
            elif days>=14:
                refund=fare*meta['cncl']['14d']
            elif days>=7:
                refund=fare*meta['cncl']['7d']
            elif days>=4:
                refund=fare*meta['cncl']['4d']
            else:
                refund=0
            file.write("Refund Amount = Rs. {}\n".format(refund))
            file.write("Cancellation Charge = Rs. {}\n".format(refund))
        elif choice1==3:
            break
    file.close()
    # printing output
    print()
    file=open("reservation.txt")
    data=file.read()
    print(data)
    file.close()