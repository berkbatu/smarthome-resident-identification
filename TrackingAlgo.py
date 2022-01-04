
################# Tracking Algorithm Start

p1path=[0] #some definitions to use
p2path=[0]
p1Finalpath=[0]
p2Finalpath=[0]
mostCommonSensors1=[0]
mostCommonSensors2=[0]
trackFeatures=[]
timeframe=[0]
startTime=[(hourlist[0],minutelist[0])]
p1=0
p2=0
p3=0
p4=0
other=0
currentSensor=0
prevSensor=0
sTime=datetime.strptime(timestamps[0], "%Y-%m-%d %H:%M:%S.%f")
endTime=datetime.strptime(timestamps[0], "%Y-%m-%d %H:%M:%S.%f")
p1bool=False
p2bool=False
p3bool=False
p4bool=False
counter=0
for i in range(len(sensors)):
    currentSensor=sensors[i]
    if(prevSensor!=sensors[i]):
        endTime=datetime.strptime(timestamps[i], "%Y-%m-%d %H:%M:%S.%f")
        if((checkAdj(p1,currentSensor)==True or p1==currentSensor or checkAdj(currentSensor,p1)==True or len(p1path)==1)):
            p1=currentSensor
            counter+=1
            p1path.append(str(endTime)+" | "+str(currentSensor))
            p1Finalpath.append(str(endTime)+" | "+str(currentSensor))
            mostCommonSensors1.append(getArtificalSensor(currentSensor))
            if(p1bool==False):
                p1bool=True
        elif((checkAdj(p2,currentSensor)==True or p1==currentSensor or checkAdj(currentSensor,p2)==True or len(p2path)==1)):
            p2=currentSensor
            p2path.append(str(endTime)+" | "+str(currentSensor))
            p2Finalpath.append(str(endTime)+" | "+str(currentSensor))
            mostCommonSensors2.append(getArtificalSensor(currentSensor))
            if(p2bool==False):
                p2bool=True
        #personCount+=1 #also check time. arttırmak yerine binary tut her kişide
        if(i>0 and (datetime.strptime(timestamps[i], "%Y-%m-%d %H:%M:%S.%f")-datetime.strptime(timestamps[i-1], "%Y-%m-%d %H:%M:%S.%f")).seconds>1200):
            print("\nStart:",sTime," End:",timestamps[i-1],"\nCount:",p1bool,p2bool, "DIFF:",(datetime.strptime(timestamps[i-1], "%Y-%m-%d %H:%M:%S.%f")-sTime))
            print("\nPerson 1 Path: \n",p1path)
            print("\nPerson 2 Path: \n",p2path)
            sTime=datetime.strptime(timestamps[i], "%Y-%m-%d %H:%M:%S.%f")
            p1bool=False
            p2bool=False
            
            if(len(Counter(mostCommonSensors1).most_common())>3 and len(Counter(mostCommonSensors2).most_common())>3):
                
                #feature person1 - most common 3 sensors + the avg gait speed
                featureRow=[Counter(mostCommonSensors1).most_common(4)[0][0],Counter(mostCommonSensors1).most_common(4)[1][0],Counter(mostCommonSensors1).most_common(4)[2][0],Counter(mostCommonSensors1).most_common(4)[3][0],Counter(mostCommonSensors1).most_common(5)[4][0],(len(p1path)*60/(timestamps[i-1]-sTime).seconds)]
                trackFeatures.append(featureRow)
            
                #feature person2
                featureRow=[Counter(mostCommonSensors2).most_common(4)[0][0],Counter(mostCommonSensors2).most_common(4)[1][0],Counter(mostCommonSensors2).most_common(4)[2][0],Counter(mostCommonSensors2).most_common(4)[3][0],Counter(mostCommonSensors1).most_common(5)[4][0],(len(p2path)*60/(timestamps[i-1]-sTime).seconds)]
                trackFeatures.append(featureRow)
            
            #FEATURELARI ÇIKAR. MOST COMMON SENSORLERI TUTTUK EN SON LISTEDE!!! GO GO GO
            p1path.clear()
            p2path.clear()
            p1path=[0]
            p2path=[0]
        
    prevSensor=currentSensor

################# Tracking Algorithm End


newTracks=trackFeatures[:60]
def getArtificalSensor(sensor):
    if(sensor >= 43 and sensor <= 50):
        return sensor
    else:
        return sensor
