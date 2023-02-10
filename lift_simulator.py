"""
simulation of a simple, moderately functional lift.
Lift starts from ground floor(0) up to the maximum floor(numberOfFloors - 1) in the building.

0nce it's enroute up, it doesn't return down to drop new requests for lower floors
till it completes its upward requests
"""

numberOfFloors = int(input("Number of building floors: "))

lift = list(range(numberOfFloors)) # + ground floor 

global counter, total_request
counter = 0 #to move the lift across floors
total_request = 0

up = [] #requests for 'up' floors to go to
down = [] #requests for 'down' floors

#funtion to get requests for the lift (i.e press lift buttons)
def make_request():
        isMoving = input("Going somewhere? (Y/N): ")

        if isMoving == 'Y':
            while True:
                try:
                    currentFloor = int(input('\t Current floor: ')) #aka floor where button was pressed
                except ValueError:
                    break

                if currentFloor > max(lift):
                    currentFloor = int(input('\t Current floor: '))
                else:
                    direction = input('\t Destination Direction? (U/D): ') #going up or down
                    if direction == 'U':
                        up.append(currentFloor)
                    elif direction == 'D':
                        down.append(currentFloor)
                    else:
                        direction = input('\t Destination Direction? (U/D): ')

        global total_request
        total_request = up + down #floors to go to
        print("\nRequests for floors", total_request)
        print("UP: ", up)
        print("DOWN: ", down)

#funtion that 'attends' to the requests for 'up'
def moveUp():
    global counter
    print("\n\nLift is currently on floor", lift[counter])

    make_request()

    if counter in up:
        print('\n\tDoor Open\n')

        #delete completed request
        personCount = up.count(counter)
        for i in range(personCount):
            up.remove(counter) 

        #getDestination
        while True:
            try:
                destinationFloor = int(input('Destination floor: ')) #aka floor where button was pressed
            except ValueError:
                break

            if destinationFloor > max(lift):
                break
            else:
                up.append(destinationFloor)

#funtion that 'attends' to the requests for 'down'
def moveDown():
    global counter
    print("\n\nLift is currently on floor", lift[counter])

    make_request()

    if counter in down:
        print('\n\tDoor Open\n')

        #delete completed request
        personCount = down.count(counter)
        for i in range(personCount):
            down.remove(counter) 

        #getDestination
        while True:
            try:
                destinationFloor = int(input('Destination floor: ')) #aka floor where button was pressed
            except ValueError:
                break

            if destinationFloor > max(lift):
                break
            else:
                down.append(destinationFloor)

#----Stop lift with keyboard interrupt
while True:

    if counter == min(lift):
        while counter != max(lift) + 1:
            moveUp()
            counter += 1

    else:
        while counter != min(lift):
            counter -= 1
            moveDown()