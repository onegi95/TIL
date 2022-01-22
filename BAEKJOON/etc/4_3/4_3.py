def night(word): # 위치를 받아온다
    where_night = list(word)
    translate_list = [0,'a','b','c','d','e','f','g','h']
    night_x = translate_list.index(where_night[0])
    night_y = int(where_night[1])
    
    moving_x = [-2,1,2,-1,-2,1,2,-1]
    moving_y = [1,2,1,2,-1,-2,-1,-2]

    count = 0
    for i in range(len(moving_x)):
        real_move_x = night_x + moving_x[i]
        real_move_y = night_y + moving_y[i]
        if real_move_x > 1 and real_move_x <= 8 and real_move_y > 1 and real_move_y <= 8:
            count += 1

    return count
print(night('a1'))