def cal_camino (value_dist, value_mag):
    opr = value_mag[0]
    for m in range (1, len(value_mag)-1):
        opr = opr - value_dist[m] 
        if opr <0:
            opr = -1
            break
        else :
            opr = opr + value_mag[m]
            
     
    return opr






def optimalPoint(magic, dist):
    # Write your code here
    value_mag = magic[:]
    value_dist = dist[:]
    index_ini =-1
    value_road = -1

    for idx in range(0,len(dist)-1):
        pos = 0
        for i in range  (idx, idx+len(dist)-1):
            if i< len(dist):
                value_mag[pos] = magic[i]
                value_dist[pos] = dist[i] 
            else:
                value_mag[pos] = magic[i-len(magic)]
                value_dist[pos] = dist[i - len(dist)]
            pos += 1    

        opr = cal_camino(value_dist,value_mag)
        if(opr> value_road):
            value_road = opr
            index_ini =  idx 


    return index_ini            




if __name__ == '__main__':
    magic = [2,4,5,2]
    dist = [4,3,1,3]

    result = optimalPoint(magic, dist)

    print (result)
