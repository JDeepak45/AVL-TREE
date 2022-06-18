import sys
class treeenode:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
        self.height=1
class avl:
    def insert(self,key,root):
        if root is None:
            return treeenode(key)
        elif key<root.key:
            root.left=self.insert(key,root.left)
        else:
            root.right=self.insert(key,root.right)
        root.height=1+max(self.getheight(root.left),
                            self.getheight(root.right))

        balancefactor=self.getbalance(root)
        if balancefactor>1:
            if key<root.left.key:
                self.rightrotate(root)
            else:
                root.left=self.leftrotate(root.left)
                root.rightrotate(root)
        elif balancefactor<-1:
            if key>root.right.key:
                return self.leftrotate(root)
            else:
                root.right=self.rightrotate(root.right)
                return self.leftrotate(root)
        return root

    def delete(self,key,root):
        if root is None:
            return root
        elif key<root.key:
            root.left=self.delete(key,root.left)
        elif key>root.key:
            root.right=self.delete(key,root.right)
        
        else:
            if root.left is None:
                temp=root.right
                root=None
                return temp
            elif root.right is None:
                temp=root.left
                root=None
                return temp
            temp=self.getminright(root.right)
            root.key=temp.key
            root.right=self.delete(temp.key,root.right)
        if root is None:
            return root


        root.height=1+max(self.getheight(root.left),
                            self.getheight(root.right))

        balancefactor=self.getbalance(root)
        if balancefactor>1:
            if key<root.left.key:
                return self.rightrotate(root)
            else:
                root.left=self.leftrotate(root.left)
                return self.rightrotate(root)
        elif balancefactor<-1:
            if key>root.right.key:
                return self.leftrotate(root)
            else:
                root.right=self.rightrotate(root.right)
                return self.leftrotate(root)
        return root

    def getminright(self,root):
        if root.left is None:
            return root
        return self.getminright(root.left)

    def getheight(self,root):
        if root is None:
            return 0
        return root.height

    def getbalance(self,root):
        if root is None:
            return 0
        else:
            return (self.getheight(root.left)-self.getheight(root.right))

    def leftrotate(self,z):
        y=z.right        
        t=y.left

        y.left=z
        z.right=t
       
        z.height=1+max(self.getheight(z.left),self.getheight(z.right))
        y.height=1+max(self.getheight(y.left),self.getheight(y.right))
        
        return y
    
    def rightrotate(self,z):
        y=z.left        
        t=y.right

        y.right=z
        z.left=t
       
        z.height=1+max(self.getheight(z.left),self.getheight(z.right))
        y.height=1+max(self.getheight(y.left),self.getheight(y.right))
        
        return y

    def preorder(self,root):
        if not root:
            return
        print("{0} ".format(root.key), end="")
        self.preorder(root.left)
        self.preorder(root.right)

    

v=avl()
root=None
nums = [33, 13, 52, 9, 21, 61, 8, 11]
for i in nums:
    root=v.insert(i,root)
v.preorder(root)
v.delete(13,root)
print()
v.preorder(root)