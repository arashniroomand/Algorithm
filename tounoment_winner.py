def tournamentWinner(competitions, results):
    Dict = {}
    result = 0
    for List in competitions:
        score = 3
        List.remove(List[results[result]])
        result+=1
        iskey = List[0] in Dict
        if iskey:
            Dict[List[0]] += score
        else:
            Dict[List[0]] = 3
    max_score = max(Dict, key = lambda x:Dict[x])
    return max_score
        
        
        
        
                



tournamentWinner([
    ["HTML","C#"],["C#","Python"],["Python","HTML"]],
                 [0,0,1])
   
 
