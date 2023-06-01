class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def genPa(leftPar: int, rightPar: int, par:str, parList: List[str]):
            if(leftPar == 0 and rightPar == 0):
                parList.append(par)
                return
            
            if(leftPar > 0):
                genPa(leftPar - 1, rightPar + 1, par + '(', parList)
            if(rightPar > 0):
                genPa(leftPar, rightPar - 1, par + ')', parList)
            
        
        paList = []
        genPa(n,0,'',paList)
        return paList