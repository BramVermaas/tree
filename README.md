# Tree
Composite design pattern for python

## Usage
Tree objects can be used to represent any kind of hierarchical data. From folder structures, family trees to bone chains in a 3d package.
It provides convient methods for searching and manipulating your hierarchy structure.

### creation:
Instantiating a tree object:
```python
import tree
mytree = tree.Tree('my tree')
```

### children and parents:
 - A tree object can have multiple children, but has a maximum of 1 parent.
 - Setting tree 'A' as a child of 'B' will automatically make 'B' the parent of 'A'
 - The reverse is also true: setting 'A' as a parent of 'B' will add 'B' to the children of 'A'

Setting children can be achieved with creation arguments:
```python
mychild = tree.Tree('my child')
mytree = tree.Tree('my tree', children = mychild)
```
```python
mytree = tree.Tree('my tree')
mychild = tree.Tree('my child', parent = mytree)
```

Or by setting the appropriate attribute:
```python
mychild = tree.Tree('my child')
mytree.children = mychild
```
```python
mychild = tree.Tree('my child')
mychild.parent = mytree
```


Adding additional children can also be done in 2 ways:
```python
mychild2 = tree.Tree('my child 2', parent = mytree)
```
```python
mychild2 = tree.Tree('my child 2')
mytree.add_children = mychild2
```


## Inherritance

## Extension

## Architecture