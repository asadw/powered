# test comment on 6/26/2019

from math import sqrt

def cellCompete(states, days):
    # WRITE YOUR CODE HERE
    
    def find_next_states(next_states, days_left):
        if days_left == 0:
            return next_states
        else:
            newstates = []
            for (x, state) in enumerate(next_states):
                if x == 0:
                    newstates.append(0 if next_states[x+1] == 0 else 1)
                elif x == (len(next_states)-1):
                    newstates.append(0 if next_states[x-1] == 0 else 1)
                else:
                    right = next_states[x+1]
                    left = next_states[x-1]
                    newstates.append(0 if right == left else 1)
            return find_next_states(newstates, days_left-1)
    
    return find_next_states(states, days)

def reconstructTree(input):
    pass

def ClosestXdestinations(numDestinations, allLocations, numDeliveries):
    locations_dict = {}
    
    for location in allLocations:
        x = location[0]
        y = location[1]
        distance = sqrt((x*x)+(y*y))
        locations_dict[distance] = location
        
    destinations = []
    for delivery in sorted(locations_dict.keys())[0:numDeliveries]:
        destinations.append(locations_dict[delivery])
    print(destinations)

def main():
    ClosestXdestinations(3, [[1,-3],[1,2],[3,4]], 1)

if __name__ == '__main__':
        main()
