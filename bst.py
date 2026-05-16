from typing import Optional, List
class BSTNode:
  def__init__(self,key:str,nama:strz):
    self.key=key
    self.nama=nama
    self.left:Optonal['BSTNode']=None
    self.right:Optional['BSTNode']=None
class BSTGedung:
  def__init__(self):
    self.root:Optional[BSTNode]=None
  def (self,key:str,nama:str)->None:
    if self.root is None:
      self.root=BSTNode(key,nama)
      return
    curr=self.root
    while True:
      if key<curr.key:
        if curr.left is None:
          curr.left=BSTNode(key,nama)
          break
        curr=curr.left
      elif key>curr.key:
        if curr.right is None:
          curr.right=BSTNode(key,nama)
      else:
        curr.nama=nama
        break
  def search(self,key:str)-> Optional[str]:
    curr=self .root
    while curr is not None:
      if key==curr.key:
        return curr.nama
      elif key<curr.key:
        curr=curr.right
    return None
  def inorder(self)->List[str]:
    result=[]
    def _inorder(node:Optional[BSTNode}):
      if node:
        _inorder(node.left)
        result.append(f"{node.key}-{node.nama}")
        _inorder(node.right)
_inorder(self.root)
return reslt
    
    
