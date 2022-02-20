def function():

    myDict = {}

    myDict[('a1','b1','c1')]='d1'

    myDict[('x1','y1','z1')]='a1'

    new_key1=('a1','b1','c1')

    new_key2=('x1','y1','z1')

    if new_key1 in myDict:

        print(myDict[new_key1])

    if new_key2 in myDict:

        print(myDict[new_key2])

function()
