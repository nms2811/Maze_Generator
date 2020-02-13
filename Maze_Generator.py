#NAME: Minseop Noh
#STUDENT NUMBER: 128546157
#COURSE:PRG469 NAA
#INSTRUCTOR NAME:Danny Abesdris
#DUE DATE: Mar 4, 2019
#DATE SUBMITTED: Feb 27, 2019
#PURPOSE: Making a maze and find an unknown destination expressed by '#' 
#  with start point expressed by '@' at(1,0) 

# STUDENT OATH:
# -------------
#
# "I declare that the attached project is wholly my own work in accordance
# with Seneca Academic Policy. No part of this project has been copied
# manually or electronically from any other source (including web sites) or
# distributed to other students."
#
# Minseop Noh   ________________________  128546157  _________________

import random, sys
import copy

# usage: python mazeGen.py 35 20
#        Modified and augmented by: danny abesdris 02/07/2019
def mazeGen (row, cols) :
    try :
        (rows, cols) = (int(sys.argv[1]), int(sys.argv[2])) # accepts 2 command line arguments
        rows -= 1
        cols -= 1
    except (ValueError, IndexError) :
        print("2 command line arguments expected...")
        print("Usage: python maze.py rows cols")
        print("       minimum rows >= 20 minimum cols >= 35")
        quit( )
    try :
        assert rows >= 19 and cols >= 34
    except AssertionError :
        print("Error: maze dimensions must be at least 20 x 35...")
        print("Usage: python maze.py rows cols")
        print("       minimum rows >= 20 minimum cols >= 35")
        quit( )

    (blank, roof, wall, corner) = ' -|+'
    M = str(roof * int(cols / 2))
    n = random.randint(1, (int(cols / 2)) * (int(rows / 2) - 1))
    temp = ""
    for i in range(int(rows / 2)) :
        e = s = t = ''
        N = wall
        if i == 0 :
            t = '@'  # add entry marker '@' on first row first col only
        # end if
        for j in range(int(cols / 2)) :
            if i and(random.randint(0, 1) or j == 0) :
                s += N + blank
                t += wall
                N = wall
                M = M[1 : ] + corner
            else :
                s += M[0] + roof
                if i or j :
                    t += blank  # add blank to compensate for '@' on first row only
                # end if
                N = corner
                M = M[1 : ] + roof
            # end if / else
            n -= 1
            t += ' #' [n == 0]
        # end for
        if cols & 1 :
            s += s[-1]
            t += blank
            e = roof
        # end if
        # print(s + N + '\n' + t + wall)
        temp += str(s + N + '\n' + t + wall + '\n')
    # end for

    if rows & 1 :
        # print(t + wall)
        temp += str(t + wall + '\n')
    # end if
    # print(roof.join(M) + e + roof + corner)
    temp += str(roof.join(M) + e + roof + corner + '\n')
    return temp
# end def

def createMazeMatrix(maze) :
    array_row = []
    array_column = []
    count = 0
    for i in range(int(sys.argv[1])) :
        while (len(array_column) != int(sys.argv[2])) :
            if maze[count: count + 1] != '\n' :
                array_column.append(maze[count : count + 1])
                count += 1
            else :
                count += 1
            #end if/else
        #end while
        array_row.append(array_column)
        array_column = []
    #end for
    return array_row
#end def

def traverseMaze(array) : 
    default = copy.deepcopy(array)
    stack = [ ]
    coord = [[0, 0], 0]
    path = ""
    i = 1
    j = 0
    a = 0
    b = 0
    sum = 0
    count = 0
    while (array[i][j] != "#") :
        if array[i][j + 1] == " " and array[i + 1][j] != " ":
            path += "N"
            j += 1
            if len(stack) != 0 :
                stack[len(stack) - 1][1] += 1
            #end if
        elif array[i + 1][j] == " " and array[i][j + 1] != " " :
            path += "E"
            i += 1
            if len(stack) != 0 :
                stack[len(stack) - 1][1] += 1
            #end if
        elif array[i + 1][j] == " " and array[i][j + 1] == " " :
            coord[0][0] = i
            coord[0][1] = j + 1
            if len(stack) == 0 :
                coord[1] = 1
            else :
                coord[1] = 0
            #end if/else
            stack.append(copy.deepcopy(coord))
            i += 1
            path += "E"
            if len(stack) != 0 :
                stack[len(stack) - 1][1] += 1
            #end if
        elif array[i + 1][j] == "#" :
            path += "E"
            i += 1
            a = i
            b = j
            if len(stack) != 0 :
                stack[len(stack) - 1][1] += 1
            #end if
            for i in range(len(stack)) :
                sum += stack[i][1]
            #end for
            break
        elif array[i][j + 1] == "#" :
            path += "N"
            j += 1
            a = i
            b = j
            if len(stack) != 0 :
                stack[len(stack) - 1][1] += 1
            #end if
            for i in range(len(stack)) :
                sum += stack[i][1]
            #end for
            break
        else : 
            value = stack[(len(stack) - 1)]
            i = value[0][0]
            j = value[0][1]
            if i == 1 :
                path = path[: (-1 * (value[1] - 1))]
            else :
                path = path[: (-1 * value[1])]
            path += "N"
            sum += value[1]
            stack.pop()
            if len(stack) > 0 :
                stack[(len(stack) - 1)][1] += 1
            #end if
        #end if/else
    #end while
    for i in range(len(default)) :
        for j in range(len(default[i])) :
            if default[i][j] == " " :
                count += 1
        #end for
    #end for
    i = 1
    j = 0
    temp_path = copy.deepcopy(path)
    temp_path = temp_path[:-1]
    while (temp_path != "") :
        if temp_path[:1] == "N" :
            j += 1
            default[i][j] = "X"
            temp_path = temp_path[1:]
        else :
            i += 1
            default[i][j] = "X"
            temp_path = temp_path[1:]
        #end if/else
    #end while
    for i in range(len(default)) :
        for j in range(len(default[i])) :
            print(default[i][j], end = "")
        #end for
        print()
    #end for
    print("maze dimensions: (", sys.argv[1], "x", sys.argv[2], ")")
    print("found # at coords: (", a, ",", b, ") path:", path)
    print("total searches: (", sum, "/", count, ")", round((sum/count) * 100, 4), "% of maze")
#end def

traverseMaze(createMazeMatrix(mazeGen(sys.argv[1], sys.argv[2])))