# for i in range(1, 6):
    #for j in range(1, i +1):
        #print(j, end=" ")
    #print( )

#for i in range(1, 6):
    #print(i, end=" ")

while True:
    print("Menu")
    print("1. Pola 1")
    print("2. Pola 2")
    print("3. Keluar")

    pilihan = str(input("Silahkan pilih dari menu(1/2/3): "))

    if pilihan == "1":
        #Pola 1
        for i in range(1, 12):
            if i % 3 == 0:
                print ("Hello", end=" ")
            else:
                print(i, end=" ")

    elif pilihan == "2":
        #Pola 2
        for i in range(1, 4):
            for j in range(1, 5):
                print(i, end=" ")
            print( )
        print( )

    elif pilihan == "3":
        print("Done")
        break

    else:
        print("Not valid option")

                
            
    
    

            
              
    