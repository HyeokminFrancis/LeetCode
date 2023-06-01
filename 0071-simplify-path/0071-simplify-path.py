class Solution:
    def simplifyPath(self, path: str) -> str:
        dirList = path.split('/')
        dirList = [dir for dir in dirList if dir != '']
        print(dirList)

        simPath = []
        for dir in dirList:
            if(dir == '.'):
                continue
            elif(dir == '..'):
                if(len(simPath) > 0):
                    simPath.pop()
            else:
                simPath.append(dir)
            
            
        
        
        
        simPath = '/' + '/'.join(simPath)
        return simPath