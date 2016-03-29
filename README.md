# Tree
Composite design pattern for python.

## Usage
Tree objects can be used to represent any kind of hierarchical data. For example: folder structures or bone chains in a 3d package.
It provides convient methods for searching and manipulating your hierarchy structure.

### Creation:
Instantiating a tree object:
```python
import tree
my_tree = tree.Tree('my tree')
```

### Setting children and parents:
 - A tree object can have multiple children.
 - But it has a maximum of 1 parent.
 - Setting tree 'A' as a child of 'B' will automatically make 'B' the parent of 'A'.
 - The reverse is also true, setting 'A' as a parent of 'B' will add 'B' to the children of 'A'.
 - When setting, adding or removing children, you can provide either a single tree, list of trees or an tree iterator

Setting children can be achieved with constructor arguments:
```python
b = tree.Tree('B')
a = tree.Tree('A', children = b)
```
```python
a = tree.Tree('A')
b = tree.Tree('B', parent = a)
```

Or by setting the appropriate attribute:
```python
a = tree.Tree('A')
b = tree.Tree('B')
a.children = b
```
```python
a = tree.Tree('A')
b = tree.Tree('B')
b.parent = a
```

Adding additional children:
```python
c = tree.Tree('C')
a.add_children(c)
```
Removing children:
```python
a.remove_children(b)
```

### Getting children and parents:
 - Tree children are returned as a ChildTraverser object which is an iterator containing the children
 - A tree parent is returned as a single tree object (since there can only be 1)
 
getting children:
```python
a.children
``` 

getting parent:
```python
c.parent
``` 

## Inherritance

## Extension

## Architecture