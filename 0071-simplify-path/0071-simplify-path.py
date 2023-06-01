class Solution:
    def simplifyPath(self, path: str) -> str:
        absDirList = [dir for dir in path.split('/') if dir != '']
        canDirList = []
        for dir in absDirList:
            if(dir == '.'):
                continue
            elif(dir == '..'):
                if(len(canDirList) > 0):
                    canDirList.pop()
            else:
                canDirList.append(dir)
        canPath = '/' + '/'.join(canDirList)
        return canPath