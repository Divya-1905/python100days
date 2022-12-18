bage = {
    'pen':'hero',
    'box':'hulk',
    'paper':'a2'
}
print(bage.get('pen'))
print(bage.update({'box':'dsf'}))
print('box'in bage.keys()) #key is check the left side of set
print('a2' in bage.values()) #values is check the right side of set 
                             # so this a key and values
print(bage.items())     # print all values 
print(bage.update({'paper':'4'}))                       