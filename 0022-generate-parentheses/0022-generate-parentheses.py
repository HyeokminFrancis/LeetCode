class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def genPar(leftParNum: int, rightParNum: int, par:str, parList: List[str]):
            if(leftParNum == 0 and rightParNum == 0):
                parList.append(par)
                return    
            if(leftParNum > 0):
                genPar(leftParNum - 1, rightParNum + 1, par + '(', parList)
            if(rightParNum > 0):
                genPar(leftParNum, rightParNum - 1, par + ')', parList)
        
        parList = []
        genPar(n, 0, '', parList)
        return parList