class Node:
    
    def __init__ (self, coordinates):
    
        self.coordinates = coordinates
        self.left = None
        self.right = None

class Tree:

    def __init__ (self):
    
        self.root = None

    #INSERT

    def insert(self, coordinates):
        
        self.root = self.insert_rec(coordinates, self.root, 0)
    
    def insert_rec(self, coordinates, root, depth):

        if root is None:

            root = Node(coordinates)

        else:

            dim = depth % 2

            if coordinates[dim] < root.coordinates[dim]:

                root.left = self.insert_rec(coordinates, root.left, depth + 1)

            elif coordinates[dim] >= root.coordinates[dim]:

                root.right = self.insert_rec(coordinates, root.right, depth + 1)

        return root

    #SEARCH

    def search(self,coordinates):

        self.search_rec(coordinates, self.root, 0)
    
    def search_rec(self, coordinates,root,depth):

        dim = depth % 2

        if root is None:

            print ("false")

        elif coordinates == root.coordinates:

            print("true")

        elif coordinates[dim] < root.coordinates[dim]:

            print("0")

            self.search_rec(coordinates, root.left, depth + 1)
        
        elif coordinates[dim] >= root.coordinates[dim]:

            print("1")

            self.search_rec(coordinates, root.right, depth + 1)
    
    #BUILD

    def build(self,points):

        self.root = self.build_rec(points,0)
    
    def build_rec(self,points,depth):

        if len(points) > 1:
            
            dim = depth % 2

            points.sort(key=lambda x: x[dim])

            half = len(points) >> 1

            temp = Node(points[half])

            temp.left = self.build_rec(points[:half], depth + 1)
            temp.right = self.build_rec(points[half + 1:], depth + 1)

            return temp

        elif len(points) == 1:
            
            temp = Node(points[0])
            return temp

    #DELETE
    
    def delete(self,coordinates):
        
        self.delete_rec(coordinates,self.root,0)

    def delete_rec(self,coordinates,root,depth):

        if root is None:

            return None
        
        dim = depth % 2

        if root.coordinates == coordinates:

            if root.right is not None:

                temp = find_min(root.right,dim,depth+1).coordinates

                root.coordinates = temp

                root.right = self.delete_rec(temp,root.right,depth+1)

            elif root.left is not None:

                temp = find_min(root.left,dim,depth+1).coordinates
            
                root.coordinates = temp

                root.right = self.delete_rec(temp,root.left,depth+1)

                root.left = None

            else:

                del root

                return None
        
        else:

            if coordinates[dim] < root.coordinates[dim]:

                root.left = self.delete_rec(coordinates, root.left, depth + 1)

            elif coordinates[dim] >= root.coordinates[dim]:

                root.right = self.delete_rec(coordinates, root.right, depth + 1)
        
        return root

    #UPDATE

    def update(self,old_coordinates,new_coordinates):

        self.delete(old_coordinates)
        self.insert(new_coordinates)

    #PRINT

    def print(self):

        self.print_rec([self.root])

    def print_rec(self,roots):
        
        temp = []
        b = False

        for x in roots:
            
            print(x.coordinates,end='')

            if x.left is not None:

                temp.append(x.left)
                b = True

            if x.right is not None:
                
                temp.append(x.right)
                b = True
        
        print('')

        if b is True:

            self.print_rec(temp)


def find_min(root,dimension,depth):

    if root is None:

        return None

    dim = depth % 2

    if dim == dimension:

        if root.left is None:

            return root

        else:

            return find_min(root.left,dimension,depth+1)
    
    else:

        temp = root
        a = find_min(root.left,dimension,depth+1)
        b = find_min(root.right,dimension,depth+1)

        if (a is not None) and (a.coordinates[dimension] < temp.coordinates[dimension]):

            temp = a
        
        if (b is not None) and (b.coordinates[dimension] < temp.coordinates[dimension]):

            temp = b

        return temp



#points = [(3,2),(5,9),(8,11),(6,1),(2,8)]
#T = Tree()
#T.build(points)
#T.print()

#T.insert([4,5])
#T.insert([1,1])
#print(T.root.left.coordinates)
#print(T.search([1,3]))

T = Tree()
T.insert([30,40])
T.insert([5,25])
T.insert([70,70])
T.insert([10,12])
T.insert([50,35])
T.insert([35,45])

#T.print()

T.delete([30,40])

T.print()