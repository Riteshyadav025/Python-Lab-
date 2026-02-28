def combinationSum(candidates, target):
    result = []
    
    def backtrack(start, remaining, path):
        if remaining == 0:
            result.append(path[:])
            return
        
        for i in range(start, len(candidates)):
            if candidates[i] > remaining:
                continue
            
            path.append(candidates[i])
            backtrack(i, remaining - candidates[i], path)
            path.pop()
    
    backtrack(0, target, [])
    return result
    
candidates = [2,3,6,7]
target = 7

print(combinationSum(candidates, target))
