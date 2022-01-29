# class ClassName:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

#     def add__child(self,data):
#         if self.data == data:
#             return
        
#         if data < self.data:
#             if self.left:
#                 self.left.add__child(2)
#             else:
#                 self.left = ClassName(data)

#         else:
#             if self.right:
#                 self.right.add__child(5);
#             else:
#                 self.right = ClassName(data)

#     def in_order_transversal(self):
#         elements = []

#         if self.left:
#             left = self.left.in_order_transversal()
#             elements += left
        
#         elements.append(self.data)

#         if self.right:
#             right = self.right.in_order_transversal()
#             elements +=right

#     def 
# if __name__ == '__main__':
    
#     pass

# from _typeshed import IdentityFunction


class BinarysearchTree:
    def __init__(self, data):
        self.data = data;
        self.left = None;
        self.right = None;

    def add__child(self,data):
        if self.data == data:
            return 

        if data < self.data:
            if self.left:
                self.left.add__child(data)
            else:
                self.left = BinarysearchTree(data)

        else:
            if self.right:
                self.right.add__child(data)
            else:
                self.right = BinarysearchTree(data)

    def search(self,val):
        if self.data == val:
            return True
        
        if val < self.data:
            if self.left:
                self.left.search(val)
            else:
                return False
        else:
            if self.right:
                self.right.search(val)
            else:
                return False




if __name__ == '__main__':
    numbers = [123,78,233,21,241,22,4]
    # numbers.add__child(1)
    # numbers.search(2)
    # numbers.search(23)
    print(numbers.search(2))

            
        
        



        
        
        