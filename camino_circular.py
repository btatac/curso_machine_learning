def optimalPoint(magic, dist):
    # Write your code here
    i =0
    value_mag = magic[:]
    value_dist = dist[:]
    print (f'magic: {magic}')
    print (f'dist: {dist}')
    value_road = 0
    index_ini = 0
    while i < len(dist):
        j=0
        opr = 0
        pos = 0
        while j < len (dist):
            print (f'i: {i}')
            print (f'j: {j}')
            index = i+j
            print (f'valor de pos: {pos}')
            print (f'valor index: {index}')
            if index < len (dist):
               print (f'valor value_mag[pos]: {magic[index]}')  
               value_mag[pos]= magic[index]
               value_dist[pos] = dist[index]
            else:
                value_mag[pos] = magic [j-i]
                print (f'valor value_mag[pos] en else: {magic[j-i]}')
                value_dist[pos] = dist[j-i]
                print (f'valor value_dist[[pos] en else: {dist[j-i]}')

            pos +=1          
            j += 1

        print (f'value_mag: {value_mag}')
        print (f'value_dist: {value_dist}') 
        print (f'magic: {magic}')
        print (f'dist: {dist}')
        opr = value_mag[0]- value_dist [0]
        if (opr>0):
            opr = opr  +value_mag[1] 

        elif (opr>0):
            opr = opr - value_dist[1]  
        elif (opr>0):
            opr = opr +  value_mag[2] 
        elif (opr>0):
            opr = opr - value_dist[2]
        elif (opr>0):
            opr = opr + value_mag[3]     
        elif (opr>0):
            opr = opr  - value_dist[3]
        elif (opr<=0):
            value_road =0
            print ('dio la suma negativa o 0')

        if (opr >value_road):
            value_road = opr
            index_ini =  dist.index(value_dist [0])
            
        print (f'value_road: {value_road}')    
        i += 1      
    if value_road ==0:
        index_ini =-1  
        print (f'index_ini: {index_ini}') 

    return index_ini

if __name__ == '__main__':
    magic = [2,4,5,2]
    dist = [4,3,1,3]

    result = optimalPoint(magic, dist)

    print (result)



