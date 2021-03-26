from var import Var
from  db import DB
def get_spotsid(id):
    query = "SELECT spot_latitude, spot_longitude FROM data_spot1 WHERE id = %s"
    data = (str(id),)
    db = DB(Var.hostname, Var.port, Var.dbname, Var.username, Var.password)
    return db.execute(query, data)
from dataaccess import DataAccess
from db import DB
#da = DataAccess()
#print("----")
spot_list = get_spotsid("1")
for spot in spot_list:
    print(spot)


from spot import Spot
spot1 = Spot()
spot1.id = "1"
spot1.data1 = '赤レンガ倉庫'
spot1.data2 = 35.4516872
spot1.data3 = 139.6437905
spot2 = Spot()
spot2.id = "2"
spot2.data1 = '江ノ島'
spot2.data2 = 35.3110403
spot2.data3 = 139.4875402
spot3 = Spot()
spot3.id = "3"
spot3.data1 = '高徳院(鎌倉大仏)'
spot3.data2 = 35.3168463
spot3.data3 = 139.5357335
    
import  sys
import random
import math
import copy

POINTS_SIZE = 3
POPULATION_SIZE = 10
GENERATION = 100
MUTATE =  0.1
SELECT_RATE = 0.5

# 経路の距離を計算する
def calc_distance(points, route):
    distance = 0
    for i in range(POINTS_SIZE):
        (x0, y0) = points[route[i]]
        if i == POINTS_SIZE - 1:
            (x1, y1) = points[route[0]]
        else:
            (x1, y1) = points[route[i + 1]]
        distance = distance + math.sqrt((x0 -x1) * (x0 -x1) + (y0 -y1) * (y0 -y1))
    return distance

def sort_fitness(points, population):
    fp = []
    for individual in population:
        fitness = calc_distance(points, individual)
        fp.append((fitness, individual))
    fp.sort()

    sorted_population = []

    for fitness, individual in fp:
        sorted_population.append(individual)
    return sorted_population

def selection (points, population):
    sorted_population = sort_fitness(points, population)
    n = int(POPULATION_SIZE * SELECT_RATE)
    return sorted_population[0:n]

def crossover(ind1, ind2):
    r1 = random.randint(0, POINTS_SIZE - 1)
    r2 = random.randint(r1 + 1, POINTS_SIZE)

    flag = [0] * POINTS_SIZE
    ind = [-1] * POINTS_SIZE

    for i in range(r1, r2):
        city = ind2[i]
        ind[i] = city

        flag[city] = 1
    
    for i in list(range(0, r1)) + list(range(r2, POINTS_SIZE)):
        city = ind1[i]

        if  flag[city] == 0:
            ind[i] = city
            flag[city] = 1

    for i in range(0, POINTS_SIZE):
        if ind[i] == -1:
            for j in range(0,  POINTS_SIZE):
                city = ind1[j]
                if flag[city] == 0:
                    ind[i] = city
                    flag[city] = 1
                    break
    return ind

def mutation(ind1):
    ind2 = copy.deepcopy(ind1)
    if random.random() < MUTATE:
        city1 = random.randint(0, POINTS_SIZE - 1)
        city2 =  random.randint(0, POINTS_SIZE - 1)

        if city1 > city2:
            city1, city2 = city2, city1
        
        ind2[city1:city2 + 1] = reversed(ind1[city1:city2 + 1])
    return ind2

points = [[spot1.data2, spot1.data2], [spot2.data2, spot2.data2], [spot3.data2, spot3.data2]]

for i in range(POINTS_SIZE):
    points.append((random.random(), random.random()))
print(points)

population = []
for i in  range(POPULATION_SIZE):
    individual = list(range(POINTS_SIZE))
    random.shuffle(individual)
    population.append(individual)

for generation in range(GENERATION):
    print(u"TSP by GA (" + str(generation + 1) + u"generation)")

    population = selection(points, population)

    n = POPULATION_SIZE - len(population)

    for i in range(n):
        r1 = random.randint(0, len(population) - 1)
        r2 = random.randint(0, len(population) - 1)
        individual = crossover(population[r1], population[r2])

        individual = mutation(individual)
        population.append(individual)

sort_fitness(points, population)

for ind in range(POPULATION_SIZE):
    route = population[ind]
    dist =  calc_distance(points, route)
    print(route, dist)

    for i in range(POINTS_SIZE):
        (x0, y0) = points[route[i]]
        if i == POINTS_SIZE -  1:
            (x1, y1) = points[route[0]]
        else:
            (x1, y1) = points[route[i+1]]
