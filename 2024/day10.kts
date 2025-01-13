import java.io.File
import java.io.InputStream
import kotlin.collections.ArrayDeque

val inputStream: InputStream = File("input_10").inputStream()
val grid = mutableListOf<MutableList<Int>>()
val zeros = mutableListOf<Pair<Int, Int>>()
var i = 0

inputStream.bufferedReader().forEachLine { line ->
    grid.add(mutableListOf<Int>())
    
    var j = 0

    for (c in line) {
        if (c.toString() == "0") {
            zeros.add(Pair(i, j))
        }

        grid[i].add(c.toString().toInt())
        j++
    }

    i++;
}

var result = 0

for (start in zeros) {
    var trailhead = 0
    var stack = ArrayDeque<Pair<Int, Int>>(listOf(start))
    var visited = mutableSetOf<Pair<Int, Int>>()

    while (stack.isNotEmpty()) {
        val curr = stack.removeLast()

        // Part 1 needs these
        // if (visited.contains(curr)) {
        //     continue
        // } 

        // visited.add(curr)

        val currVal = grid[curr.first][curr.second]

        if (currVal == 9) {
            trailhead++
            continue
        }

        for (move in listOf(Pair(0, 1), Pair(0, -1), Pair(1, 0), Pair(-1, 0))) {
            val adj = Pair(curr.first + move.first, curr.second + move.second)
            if (isInBounds(adj)) {
                val adjVal = grid[adj.first][adj.second]

                if (adjVal - currVal == 1) {
                    stack.addLast(adj)
                }
            }
        }
    }

    result += trailhead
}

println(result)

fun isInBounds(adj: Pair<Int, Int>) = adj.first >= 0 && adj.second >= 0 && adj.first < grid.size && adj.second < grid[adj.first].size