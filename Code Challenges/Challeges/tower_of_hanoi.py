# tower of hanoi problem

def mytower(n,source,target,axulary):
    if n==1:
        print(f"Move 1 from peg {source} to {target}")
        return
    
    mytower(n-1,source,axulary,target)

    print(f"Move {n} from {source} to {target}")

    mytower(n-1,axulary,target,source)


mytower(3,"A","B","C")

