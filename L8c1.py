import hashlib


def hash_sha_str(a:str):
    hashSub = set()
    for i in range(len(a) + 1):
        for j in range(i + 1, len(a) + 1):
            hi = hashlib.sha1(a[i:j:].encode('utf-8')).hexdigest()
            hashSub.add(hi)
    inpStr = set(a[i:j] for i in range(len(a) + 1) for j in range(i + 1, len(a)+1)) 
    inpStr.remove(a)  
    hashSub.remove(hashlib.sha1(a.encode('utf-8')).hexdigest())
    hashDict = dict(zip(inpStr, hashSub))
    for i,j in hashDict.items():
        print(f'Подстрока {i} и её hash_код {j}')
    
    return len(hashSub)

a = "fghjuh"
print(f'количество подстрок в строке {a}: {hash_sha_str(a)}')



