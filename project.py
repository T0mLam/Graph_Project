import heapq

# Define member nodes
class Member:
    def __init__(self, name, age, location, friends=None):
        self.name = name
        self.age = age
        self.location = location
        self.friends = friends if friends else []
        
class Graph:
    def __init__(self):
        # Map members' names to the Member object
        self.members = {} 
        
    def __str__():
        pass
    def add_member(self, name, age, location):
        #Check if the object with this 
        if(name not in self.members):
            self.members[name] = Member(name,age,location)
        else:
            print("The member already exists")
            
    def add_relationship(self):
        pass
    def find_friends(self):
        pass
    
    def shortest_path(self, start, end):
        if (start not in self.members or
            end not in self.members):
            return -1
    
        # Dijkstra algorithm
        visited = set()
        pq = [(0, self.members[start])]
        while pq:
            w, member = heapq.heappop(pq)
            
            if member.name == end:
                return w
            
            visited.add(member)

            for friend in self.members[member].friends:
                if friend not in visited:
                    heapq.heappush(pq, (w + 1, friend))
            
