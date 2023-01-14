def solution(routes):
    
    routes.sort(key = lambda x: x[1])
    
    camera = [routes[0][1]]
    
    for i in range(1,len(routes)):
        
        if camera[-1] < routes[i][0]:
            camera.append(routes[i][1])
        
        else:
            continue
    
    return len(camera)