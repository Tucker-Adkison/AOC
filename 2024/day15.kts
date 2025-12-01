import java.io.File
import java.io.InputStream
import java.util.ArrayDeque
import kotlin.math.min

val inputStream: InputStream = File("inputs/input_15").inputStream()

var grid = mutableListOf<MutableList<String>>()

var first = true
var player = -1 to -1
var i = 0
var j = 0

inputStream.bufferedReader().forEachLine { 
    if (it.isEmpty()) {
        first = false
    }

    if (first) {
        val temp = mutableListOf<String>()
        var j = 0

        for (c in it) {
            if (c == '#') {
                temp.add("#")
                temp.add("#")
            } else if (c == 'O') {
                temp.add("[")
                temp.add("]")
            } else if (c == '.') {
                temp.add(".")
                temp.add(".")
            } else if (c == '@') {
                player = Pair(i, j)
                temp.add("@")
                temp.add(".")
            }

            j += 2
        }

        grid.add(temp)
    } else {

        for (c in it) {
            grid[player.first][player.second] = "."

            if (c == '^') {
                moveBoxes(-1, 0, "^", grid)
            } else if (c == 'v') {
                moveBoxes(1, 0, "v", grid)
            } else if (c == '<') {
                moveBoxes(0, -1, "<", grid)
            } else if (c == '>') {
                moveBoxes(0, 1, ">", grid)
            }

            grid[player.first][player.second] = "@"
        }
    }

    i++
}

var result = 0
i = 0
j = 0

while (i < grid.size) {
    j = 0
    while (j < grid[i].size) {
        if (grid[i][j] == "[" || grid[i][j] == "]") {
            result += (100 * i) + j
            j++
        }
        j++
    }
    i++
}

// grid[player.first][player.second] = "@"


// for (i in grid.indices) {
//     for (j in grid[i].indices) {
//         if (grid[i][j] == "O") {
//             result += i * 100 + j
//         }
//         print(grid[i][j])
//     }
//     println()
// }

println(result)
printGrid(grid)

fun move(dx: Int, dy: Int, grid: MutableList<MutableList<String>>) {
    var x = player.first + dx 
    var y = player.second + dy
    var toMove = mutableListOf<Pair<Int, Int>>()

    if (grid[x][y] == "#") {
        return
    } else if (grid[x][y] == "O") {
        toMove.add(x to y)

        var tempX = x 
        var tempY = y 

        do {
            toMove.add(Pair(tempX, tempY))

            tempX += dx 
            tempY +=  dy
        } while (grid[tempX][tempY] == "O")

        if (grid[tempX][tempY] == "#") {
            return
        } else {
            grid[toMove.first().first][toMove.first().second] = "."
            grid[tempX][tempY] = "O"
        }
    }

    player = x to y
}

fun moveBoxes(dx: Int, dy: Int, moveType: String, grid: MutableList<MutableList<String>>) {
    var x = player.first + dx 
    var y = player.second + dy
    
    if (grid[x][y] == "#") {
        return
    } else if (grid[x][y] == ".") {
        player = x to y
        return 
    }

    var tempX = player.first + dx 
    var tempY = player.second + dy
    var toMove = mutableListOf<Pair<Int, Int>>()
    
    if (moveType == "^" || moveType == "v") {
        if (grid[tempX][tempY] == "[") {
            val rightBracket = Pair(tempX, tempY + 1)

            toMove.addAll(blocksToMoveUp(tempX to tempY, dx, grid))
            toMove.addAll(blocksToMoveUp(rightBracket, dx, grid))
        } else if (grid[tempX][tempY] == "]") {
            val leftBracket = Pair(tempX, tempY - 1)

            toMove.addAll(blocksToMoveUp(tempX to tempY, dx, grid))
            toMove.addAll(blocksToMoveUp(leftBracket, dx, grid))
        }

        for (pos in toMove.reversed()) {
            if (grid[pos.first][pos.second] == "#") {
                return
            }
        }
    } else {
        do {
            toMove.add(Pair(tempX, tempY))

            tempX += dx 
            tempY += dy
        }  while (grid[tempX][tempY] == "[" || grid[tempX][tempY] == "]" )

        if (grid[tempX][tempY] == "#") {
            return
        }
    }

    val prevGrid = grid.map {it.toList()}

    for (pos in toMove) {
        grid[pos.first][pos.second] = "."
    }
    for (pos in toMove) {
        grid[pos.first + dx][pos.second + dy] = prevGrid[pos.first][pos.second]
    }

    player = x to y
}

fun blocksToMoveUp(pos: Pair<Int, Int>, dx: Int, grid: MutableList<MutableList<String>>): MutableList<Pair<Int, Int>> {
    // get the position above
    val newPos = Pair(pos.first + dx, pos.second)
    val positions = mutableListOf<Pair<Int, Int>>()
    positions.add(pos)

    if (grid[newPos.first][newPos.second] == "#") {
        positions.add(newPos)
    } else if (grid[newPos.first][newPos.second] == "]") {
        // left bracket [
        val adj = Pair(newPos.first, newPos.second - 1)

        positions.addAll(blocksToMoveUp(newPos, dx, grid))
        positions.addAll(blocksToMoveUp(adj, dx, grid))
    } else if (grid[newPos.first][newPos.second] == "[") {
        // right bracket ]
        val adj = Pair(newPos.first, newPos.second + 1)

        positions.addAll(blocksToMoveUp(newPos, dx, grid))
        positions.addAll(blocksToMoveUp(adj, dx, grid))
    }

    return positions
}

fun printGrid(grid: MutableList<MutableList<String>>) {
    val fileName = "day15_output.txt"
    for (i in grid.indices) {
        for (j in grid[i].indices) {
            print(grid[i][j])
        }
        println()
    }
}