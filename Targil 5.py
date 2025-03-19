# Targil 5:
# Parking:

def parking(pay,r,p,v):
    detail = [[],[],[]]
    count = 0
    Regular = [pay,r]
    Priority = [2 * pay,p]
    VIP = [3 * pay,v]

    def print_list(*s):
        list1 = list(s)
        for w in list1:
            print(w, end=', ')

    def print_parking(x):
        if x == 'Regular':
            print_list(detail[0])
        if x == 'Priority':
            print_list(detail[1])
        if x == 'VIP':
            print_list(detail[2])

    def next_time():
        nonlocal count
        count += 1

    def start_parking(num,type):
        nonlocal Regular,Priority,VIP,detail


        if type == 'Regular':
            if Regular[1] > 0:
                Regular[1] = Regular[1] - 1
                Rdetail = ['car:',num,'parking time:',count]
                detail[0].append(Rdetail)
                print_parking('Regular')


            else:
                print('Regular parking is full')

        if type == 'Priority':
            if Priority[1] > 0:
                Priority[1]-=1
                Pdetail = ['car:',num,'parking time:',count]
                detail[1].append(Pdetail)
            else:
                print('Priority parking is full')

        if type == 'VIP':
            if VIP[1] > 0:
                VIP[1]-=1
                Vdetail = ['car:',num,'parking time:',count]
                detail[2].append(Vdetail)
            else:
                print('VIP parking is full')


    return {'print_list':print_list,'print_parking':print_parking,'next_time':next_time,'start_parking':start_parking}

print("Shalev")

park1 = parking(10,3,3,3)
park1['next_time']()
park1['start_parking'](223,'Regular')
park1['next_time']()
park1['print_parking']('Regular')


