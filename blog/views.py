from django.shortcuts import render
from .models import Travels
from sys import maxsize
from itertools import permutations


def index(request):
    return render(request,'index.html')

def abt(request):
    return render(request,'about.html')

def work(request):
    return render(request,'working.html')


def minpath(request):
    cities = request.GET.get('cities','default')
    s = request.GET.get('sc', 'default')
    check = request.GET.get('Ada', 'off')
    otherc =  request.GET.get('Ada', 'off')
    G = request.GET.get('Gbtn', 'default')
    ccity = request.GET.get('connected', 'default')
    print(ccity)
    s = int(s)
    print(s)

    def Convert(string):
        li = list(string.split(" "))
        return li
    Li = Convert(otherc)
    print(Li)

    keys = []
    for i in Li:
        if i == 'AndhraPradesh':
            keys.append(0)
        if i == 'ArunachalPradesh':
            keys.append(1)
        if i == 'Assam':
            keys.append(2)
        if i == 'Bihar':
            keys.append(3)
        if i == 'Chhattisgarh':
            keys.append(4)
        if i == 'Goa':
            keys.append(5)
        if i == 'Gujarat':
            keys.append(6)
        if i == 'Haryana':
            keys.append(7)
        if i == 'HimachalPradesh':
            keys.append(8)
        if i == 'Jharkhand':
            keys.append(9)
        if i == 'Karnataka':
            keys.append(10)
        if i == 'Kerala':
            keys.append(11)
        if i == 'MadhyaPradesh':
            keys.append(12)
        if i == 'Maharashtra':
            keys.append(13)
        if i == 'Manipur':
            keys.append(14)
        elif i == 'Meghalaya':
            keys.append(15)
        if i == 'Mizoram':
            keys.append(16)
        if i == 'Nagaland':
            keys.append(17)
        if i == 'Odisha':
            keys.append(18)
        if i == 'Punjab':
            keys.append(19)
        if i == 'Rajasthan':
            keys.append(20)
        if i == 'Sikkim':
            keys.append(21)
        if i == 'TamilNadu':
            keys.append(22)
        if i == 'Telangana':
            keys.append(23)
        if i == 'Tripura':
            keys.append(24)
        if i == 'UttarPradesh':
            keys.append(25)
        if i == 'Uttarakhand':
            keys.append(26)
        if i == 'WestBengal':
            keys.append(27)

    print(keys)





    All_Data = list(Travels.objects.values())
    print(All_Data)
    graph = []

    for item in All_Data:
        graph.append(list(item.values()))


    for i in graph:
        i.pop(0)
        i.pop(0)


    print(graph)


    ngraph = []
    for i in graph:
        temp = list(map(int,i))
        ngraph.append(temp)
    print(ngraph)


    V = int(cities)
    possible_paths = []
    Different_cost = []
    minpath = 0

    def travellingSalesmanProblem(graph, s):

        # vertex = []
        # for i in range(V):
        #     if i != s:
        #         vertex.append(i)

        min_path = maxsize
        next_permutation = permutations(keys)

        count = 0
        for i in next_permutation:
            count = count + 1
            print(i)
            current_pathweight = 0

            k = s
            for j in i:
                current_pathweight += graph[k][j]
                k = j
            current_pathweight += graph[k][s]

            Different_cost.append(current_pathweight)

            min_path = min(min_path, current_pathweight)

        print(count)
        return min_path

    Min_cost = travellingSalesmanProblem(ngraph, s)

    print(Min_cost)

    V = int(cities)
    vertex = []
    # for i in range(V):
    #     if i != s:
    #         vertex.append(i)

    next_permutation = permutations(keys )

    for x in list(next_permutation):
        strr = ""
        for y in x:
            if y == 0:
                strr = strr + '-Andhra Pradesh'
            if y == 1:
                strr = strr + '-Arunachal Pradesh'
            if y == 2:
                strr = strr + '-Assam'
            if y == 3:
                strr = strr + '-Bihar'
            if y == 4:
                strr = strr + '-Chhattisgarh'
            if y == 5:
                strr = strr + '-Goa'
            if y == 6:
                strr = strr + '-Gujarat'
            if y == 7:
                strr = strr + '-Haryana'
            if y == 8:
                strr = strr + '-Himachal Pradesh'
            if y == 9:
                strr = strr + '-Jharkhand'
            if y == 10:
                strr = strr + '-Karnatka'
            if y == 11:
                strr = strr + '-Kerala'
            if y == 12:
                strr = strr + '-Madhya Pradesh'
            if y == 13:
                strr = strr + '-Maharashtra'
            if y == 14:
                strr = strr + '-Manipur'
            if y == 15:
                strr = strr + '-Meghalaya'
            if y == 16:
                strr = strr + '-Mizoram'
            if y == 17:
                strr = strr + '-Nagaland'
            if y == 18:
                strr = strr + '-Odisha'
            if y == 19:
                strr = strr + '-Punjab'
            if y == 20:
                strr = strr + '-Rajasthan'
            if y == 21:
                strr = strr + '-Sikkim'
            if y == 22:
                strr = strr + '-TamilNadu'
            if y == 23:
                strr = strr + '-Telangana'
            if y == 24:
                strr = strr + '-Tripura'
            if y == 25:
                strr = strr + '-Uttar Pradesh'
            if y == 26:
                strr = strr + '-Uttarakhand'
            if y == 27:
                strr = strr + '-West Bengal'

        if s == 0:
            possible_paths.append('Andhra pradesh' + strr + '-Andhrapradesh')
        if s == 1:
            possible_paths.append('Arunachal Pradesh' + strr + '-Arunachal pradesh')
        if s == 2:
            possible_paths.append('Assam' + strr + '-Assam')
        if s == 3:
            possible_paths.append('Bihar' + strr + '-Bihar')
        if s == 4:
            possible_paths.append('Chhattisgarh' + strr + '-Chhattisgarh')
        if s == 5:
            possible_paths.append('Goa' + strr + '-Goa')

        if s == 6:
            possible_paths.append('Gujarat' + strr + '-Gujarat')
        if s == 7:
            possible_paths.append('Haryana' + strr + '-Haryana')
        if s == 8:
            possible_paths.append('Himachal pradesh' + strr + '-Himachal pradesh')
        if s == 9:
            possible_paths.append('Jharkhand' + strr + '-Jharkhand')
        if s == 10:
            possible_paths.append('Karnatka' + strr + '-Karnatka')
        if s == 11:
            possible_paths.append('Kerala' + strr + '-Kerala')
        if s == 12:
            possible_paths.append('Madhya Pradesh' + strr + '-Madhya Pradesh')
        if s == 13:
            possible_paths.append('Maharashtra' + strr + '-Maharashtra')
        if s == 14:
            possible_paths.append('Manipur' + strr + '-Manipur')
        if s == 15:
            possible_paths.append('Meghalaya' + strr + '-Meghalaya')
        if s == 16:
            possible_paths.append('Mizoram' + strr + '-Mizoram')
        if s == 17:
            possible_paths.append('Nagaland' + strr + '-Nagaland')
        if s == 18:
            possible_paths.append('Odhisa' + strr + '-Odhisa')
        if s == 19:
            possible_paths.append('Punjab' + strr + '-Punjab')
        if s == 20:
            possible_paths.append('Rajasthan' + strr + '-Rajasthan')
        if s == 21:
            possible_paths.append('Sikkim' + strr + '-Sikkim')
        if s == 22:
            possible_paths.append('Tamil Nadu' + strr + '-Tamil Nadu')
        if s == 23:
            possible_paths.append('Telangana' + strr + '-Telangana')
        if s == 24:
            possible_paths.append('Tripura' + strr + '-Tripura')
        if s == 25:
            possible_paths.append('Uttar Pradesh' + strr + '-Uttar Pradesh')
        if s == 26:
            possible_paths.append('Uttarakhand' + strr + '-Uttarakhand')
        if s == 27:
            possible_paths.append('West Bengal' + strr + '-West Bengal')





    params = {possible_paths[i]: Different_cost[i] for i in range(len(possible_paths))}
    params.update({'Mincost_path': Min_cost})

    pal = {"cost":Different_cost,"paths":possible_paths}

    if G == "graph":
        return render(request, 'gr.html',pal)
    else:
        return render(request, 'output.html', {'pa': params})

