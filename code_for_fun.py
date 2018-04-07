from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.nimabi = defaultdict(list)
        self.temphold = defaultdict(list)
        self.baby=[]
        self.tpsorted = []
        self.nimadeerzi = []
        
    def addEdge(self,u,v):
        self.graph[u].append(v)
        
    def dfs(self,vertices):
        if vertices in self.baby:
            return 
            
        self.baby.append(vertices)
        for i in self.graph[vertices]:
            if i not in self.baby:
                self.dfs(i)
        self.tpsorted.insert(0,vertices)
        
    def bfs(self,vertices,b=0):
        queue = [vertices]
        baby = []
        nimabii =defaultdict(list)
        a = 0       
        nimabii[a].append(vertices)
        while queue:
            vertic = queue.pop(0)
            baby.append(vertic)
            neighbours = self.graph[vertic]
            try:
                if vertic == nimabii[a][0]:
                    a += 1
            except:
                return nimabii
            for neighbour in neighbours:
                queue.append(neighbour)
                if neighbour not in nimabii[a]:
                    nimabii[a].append(neighbour)
        return nimabii
    def tp(self):
       
        self.nimadeerzi= sorted(self.graph, key=lambda k: len(self.graph[k]))
        self.nimadeerzi = self.nimadeerzi[::-1]
        
        for i in list(self.nimadeerzi):
            self.dfs(i)
        return self.tpsorted
    
    def premodify (self,mod):
        checkedlist = []
        for level in list(mod):
            if len(mod[level]) == 0:
                del mod[level]
            for element in mod[level][:]:
                if element not in checkedlist:
                    checkedlist.append(element)
                else:
                    mod[level].remove(element)
            checkedlist =[]
        return mod 
    def graphmodify(self,head):
        head = self.premodify(head)
        checkedlist = []
        a = 0

        for currentlevel in list(head)[::-1]:
            if a == 0 and len(head[currentlevel]) != 0 :
                checkedlist = head[currentlevel]
                a =1
                continue
            for element in head[currentlevel][:]:
                try:
                    while element in checkedlist:
                        head[currentlevel].remove(element)
                except:
                    continue
                              
            checkedlist = checkedlist+head[currentlevel]
        return head

    def generate(self):
        self.tp()
        self.nimabi = self.bfs(self.tpsorted[0])
        key = self.nimabi[1]
        endlevel = self.tpsorted.index(key[0])
        
        for i in range(1,len(self.tpsorted)):
            secondlevel = True
            for j in range(1,i):
                if self.tpsorted[i] in self.graph[self.tpsorted[j]]:
                    
                    secondlevel = False
        
            if secondlevel == True:
                self.temphold = self.bfs(self.tpsorted[i])
                for i in list(self.temphold):
                    if self.temphold[i] not in self.nimabi[i]:
                        self.nimabi[i] = self.nimabi[i]+self.temphold[i]
        self.nimabi= self.graphmodify(self.nimabi)
        
        for i in self.nimabi[0]:
            self.addEdge('IHAVETOCONNECTYOU',i)
        self.nimabi =  self.bfs('IHAVETOCONNECTYOU')
        self.nimabi= self.graphmodify(self.nimabi)
        
        
        return self.nimabi
            

    def display(self):
        self.generate()
        print("YOU CAN TAKE IN THE FOLLOWING ORDER PER SEMESTER")
        for i in list(self.nimabi):
            if i == 0:
                continue
            if len(self.nimabi[i]) == 0:
                continue
                   
            else:
                while len(self.nimabi[i]) < 5:
                    self.nimabi[i].append('Genics')
                if len(self.nimabi[i]) >6:
                    print(self.nimabi[i][0:5])
                    while len(self.nimabi[i][5:]) < 5:
                        self.nimabi[i].append('Genics')
                    print(self.nimabi[i][5:])
                    
                else:
                    print(self.nimabi[i])
                    
           

g = Graph()
g.addEdge('Cmpsc121','Cmpsc122');
g.addEdge('Cmpsc121','Cmpsc450');
g.addEdge('Cmpsc121','Cmpsc455');
g.addEdge('Cmpsc122','Cmpsc221');
g.addEdge('Cmpsc122','Cmpsc360');
g.addEdge('Cmpsc122','Cmpsc465');
g.addEdge('Cmpsc122','Cmpsc442');
g.addEdge('Cmpsc221','Cmpsc311');
g.addEdge('Cmpsc221','Cmpsc475');
g.addEdge('Cmpsc221','Cmpsc461');
g.addEdge('Cmpsc221','Cmpsc444');
g.addEdge('Cmpsc360','Cmpsc461');
g.addEdge('Cmpsc360','Cmpsc465');
g.addEdge('Cmpsc311','Cmpsc473');
g.addEdge('Cmpsc311','Cmpsc458');
g.addEdge('Cmpsc311','Cmpsc475');
g.addEdge('Cmpsc450','Cmpsc456');
g.addEdge('Cmpsc461','Cmpsc471');
g.addEdge('Cmpsc456','Cmpsc475');
g.addEdge('Cmpsc465','Cmpsc464');
g.addEdge('Maths140','Maths141');
g.addEdge('Maths141','Maths220');
g.addEdge('Maths141','Maths230');
g.addEdge('Maths140','Phys212');
g.addEdge('Maths220','Cmpsc458');
g.addEdge('Maths220','Cmpsc450');
g.addEdge('Maths220','Cmpsc455');
g.addEdge('Maths230','Cmpsc458');
g.addEdge('Maths230','Cmpsc450');
g.addEdge('Maths230','Cmpsc455');
g.addEdge('Phys211','Phys212');
g.addEdge('Phys212','Cmpen270');
g.addEdge('Cmpen270','Cmpen331');
g.addEdge('Cmpen331','Cmpsc473');




 
print( "Following is a Topological Sort of the given graph")
g.display()
