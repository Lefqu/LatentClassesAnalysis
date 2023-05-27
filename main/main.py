import numpy as np
import matplotlib.pyplot as plt

#подготовка данных
paramsCount = 2
parXs = []
parYs = []
clusterNum = []
j = 0

with open(r'C:\Users\maxkr\Desktop\University\CoursePROG\input\Feritins2-3.txt') as file:
    while 1:
        s = file.readline()
        if (s == ''):
            break
        data = [float(x) for x in s.split('\t')]
        parXs.append(data[0])
        parYs.append(data[1])
        clusterNum.append(data[2])
        j += 1

cluster1 = []
cluster2 = []

cluster1X = []
cluster1Y = []

cluster2X = []
cluster2Y = []

exp = []
for i in range(len(parXs)):
    if (clusterNum[i] == 2):
        exp.append(parXs[i])
        exp.append(parYs[i])
        cluster1X.append(parXs[i])
        cluster1Y.append(parYs[i])
        cluster1.append(exp)
        exp = []
    elif (clusterNum[i] == 3):
        exp.append(parXs[i])
        exp.append(parYs[i])
        cluster2X.append(parXs[i])
        cluster2Y.append(parYs[i])
        cluster2.append(exp)
        exp = []

print("Cluster 1 :", cluster1, "\n")
print("Cluster 2 :", cluster2, "\n")

# print("Cluster 1x :", cluster1X, "\n")
# print("Cluster 1y :", cluster1Y, "\n")

# print("Cluster 2x :", cluster2X, "\n")
# print("Cluster 2y :", cluster2Y, "\n")


# Draw BEFORE computing
# plt.scatter(cluster1X, cluster1Y, marker = 'o', color = 'blue', s = 30 , label = 'Cluster1')
# plt.scatter(cluster2X, cluster2Y, marker = 'o', color = 'red', s = 30, label = 'Cluster2')
# plt.xlabel('X axis')
# plt.ylabel('Y axis')
# plt.legend(loc = 'best')
# plt.savefig('Start_partition.png')
#plt.show()

# 1
k = 1
while 1:
    print(f"PROHOD {k}")
    corr1 = np.corrcoef(cluster1X, cluster1Y)[0, 1]
    corr2 = np.corrcoef(cluster2X, cluster2Y)[0, 1]
    R = corr1**2 + corr2**2
    print("R ==", R, "\n")
    avgX1 = np.mean(cluster1X)
    avgY1 = np.mean(cluster1Y)
    avgX2 = np.mean(cluster2X)
    avgY2 = np.mean(cluster2Y)

    # отрисовка ПОШАГОВО1
    plt.scatter(cluster1X, cluster1Y, marker = 'o', color = 'blue', s = 30 , label = 'Cluster 1')
    plt.scatter(cluster2X, cluster2Y, marker = 'o', color = 'red', s = 30, label = 'Cluster 2')
    plt.xlabel('X axis')
    plt.ylabel('Y axis')
    plt.legend(loc = 'best')
    plt.show()



    maxQ = 0
    for i in range(len(cluster2)):

        ax = (cluster2X[i] - avgX1) / (np.sqrt(np.var(cluster1X)) * np.sqrt(len(cluster1) + 1))
        ay = (cluster2Y[i] - avgY1) / (np.sqrt(np.var(cluster1Y)) * np.sqrt(len(cluster1) + 1))
        ro1_new = (corr1 + ax*ay) / np.sqrt((1 + ax**2) * (1 + ay**2))
        bx = (cluster2X[i] - avgX2) / (np.sqrt(np.var(cluster2X)) * np.sqrt(len(cluster2) - 1))
        by = (cluster2Y[i] - avgY2) / (np.sqrt(np.var(cluster2Y)) * np.sqrt(len(cluster2) - 1))
        ro2_new = (corr2 - bx*by) / np.sqrt((1 + bx**2) * (1 + by**2))
        Q = R - ro1_new**2 - ro2_new**2
        print("Q == ", Q)
        if (Q < maxQ):
            maxQ = Q
            obj_index = i

    if (maxQ == 0):
        break
    else:
        cluster1.append(cluster2[obj_index])
        cluster2.pop(obj_index)
        cluster1X.append(cluster2X[obj_index])
        cluster2X.pop(obj_index)
        cluster1Y.append(cluster2Y[obj_index])
        cluster2Y.pop(obj_index)
        corr1 = np.corrcoef(cluster1X, cluster1Y)[0, 1]
        corr2 = np.corrcoef(cluster2X, cluster2Y)[0, 1]
        R = corr1**2 + corr2**2
        print(cluster1, '\n', cluster2, '\n')
        #print("R == ", R, "\n")
    k += 1

    # minCheck = 0
    # print("проверка условия: (<0 or not)")
    # for i in range(len(cluster2)):
    #     check = corr1 * (cluster2X[i] - avgX1) * (cluster2Y[i] - avgY1)
    #     print(check, '\n')
    #     if (check < minCheck):
    #         minCheck = check
    #         minCheckIndex = i

    # if (minCheck == 0): # if nothing more to move
    #     break
    # else:
    #     cluster1.append(cluster2[minCheckIndex])
    #     cluster2.pop(minCheckIndex)
    #     cluster1X.append(cluster2X[minCheckIndex])
    #     cluster2X.pop(minCheckIndex)
    #     cluster1Y.append(cluster2Y[minCheckIndex])
    #     cluster2Y.pop(minCheckIndex)
    #     corr1 = np.corrcoef(cluster1X, cluster1Y)[0, 1]
    #     corr2 = np.corrcoef(cluster2X, cluster2Y)[0, 1]
    #     R = corr1**2 + corr2**2
    #     print(cluster1, '\n', cluster2, '\n')
    #     #print("R == ", R, "\n")
    # k += 1


fout1 = open(r"C:\Users\maxkr\Desktop\University\CoursePROG\output\cluster1.txt", "w")
fout1.write("Cluster 1 elements:\nX\tY\n")
for i in range(len(cluster1)):
    fout1.write(f"{cluster1X[i]}\t{cluster1Y[i]}\n")
fout1.close()

fout2 = open(r"C:\Users\maxkr\Desktop\University\CoursePROG\output\cluster2.txt", "w")
fout2.write("Cluster 2 elements:\nX\tY\n")
for i in range(len(cluster2)):
    fout2.write(f"{cluster2X[i]}\t{cluster2Y[i]}\n")
fout1.close()

# Draw AFTER computing
plt.scatter(cluster1X, cluster1Y, marker = 'o', color = 'blue', s = 30 , label = 'Cluster1')
plt.scatter(cluster2X, cluster2Y, marker = 'o', color = 'red', s = 30, label = 'Cluster2')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.legend(loc = 'best')
plt.savefig('End_partition.png')
# plt.show()




# мб сделать проход со вторым кластером


