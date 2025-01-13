import java.io.File
import java.io.InputStream

val inputStream: InputStream = File("input_12").inputStream()
val grid = mutableListOf<MutableList<String>>()

inputStream.bufferedReader().forEachLine { line ->
    val chars = mutableListOf<String>()
    for (c in line) {
        chars.add(c.toString())
    }

    grid.add(chars)
}

/**
 * (-1, -1), (-1, 0), (-1, 1)
 * (0, -1), (0, 0), (0, 1)
 * (1, -1), (1, 0), (1, 1)
 */

var tDiagonals = mapOf(
    setOf(Pair(-1, 0), Pair(0, 1), Pair(1, 0)) to listOf(Pair(-1, 1), Pair(1, 1)),
    setOf(Pair(0, 1), Pair(1, 0), Pair(0, -1)) to listOf(Pair(1, 1), Pair(1, -1)),
    setOf(Pair(1, 0), Pair(0, -1), Pair(-1, 0)) to listOf(Pair(1, -1), Pair(-1, -1)),
    setOf(Pair(0, -1), Pair(-1, 0), Pair(0, 1)) to listOf(Pair(-1, -1), Pair(-1, 1)),
)

var lDiagonals = mapOf(
    setOf(Pair(-1, 0), Pair(0, 1)) to Pair(-1, 1),
    setOf(Pair(0, 1), Pair(1, 0)) to Pair(1, 1),
    setOf(Pair(1, 0), Pair(0, -1)) to Pair(1, -1),
    setOf(Pair(0, -1),  Pair(-1, 0)) to Pair(-1, -1),
)

var combinations = mapOf(
    emptySet<Pair<Int, Int>>() to "O",
    setOf(Pair(1,0)) to "i",
    setOf(Pair(0, 1)) to "i",
    setOf(Pair(-1, 0)) to "i",
    setOf(Pair(0, -1)) to "i",

    setOf(Pair(-1, 0), Pair(0, 1)) to "L",
    setOf(Pair(0, 1), Pair(1, 0)) to "L",
    setOf(Pair(1, 0), Pair(0, -1)) to "L",
    setOf(Pair(0, -1),  Pair(-1, 0)) to "L",

    setOf(Pair(-1, 0), Pair(0, 1), Pair(1, 0)) to "T",
    setOf(Pair(0, 1), Pair(1, 0), Pair(0, -1)) to "T",
    setOf(Pair(1, 0), Pair(0, -1), Pair(-1, 0)) to "T",
    setOf(Pair(0, -1), Pair(-1, 0), Pair(0, 1)) to "T",
    
    setOf(Pair(-1, 0), Pair(1, 0)) to "-",
    setOf(Pair(0, -1), Pair(0, 1)) to "|",
    setOf(Pair(0, -1), Pair(0, 1), Pair(-1, 0), Pair(1, 0)) to "+",
)

var comboNumbers = mapOf(
    "O" to 4,
    "i" to 2,
    "L" to 1,
    "-" to 0,
    "|" to 0,
    "+" to 0,
    "T" to 0,
)

val seen = mutableSetOf<Pair<Int, Int>>()
var result = 0
var newResult = 0

for (x in grid.indices) {
    for (y in grid.indices) {
        val plant = Pair(x, y)
        val plantType = grid[x][y]
        if (seen.contains(plant)) {
            continue
        }

        var stack = ArrayDeque<Pair<Int, Int>>(listOf(plant))
        var prev = plant
        var area = 0
        var perimeter = 0
        var newPerimeter = 0
        var corners = 0

        while (stack.isNotEmpty()) {
            var adjacents = mutableSetOf<Pair<Int, Int>>()

            val curr = stack.removeFirst()

            if (seen.contains(curr)) {
                continue
            }

            area++

            seen.add(curr)

            var adjCount = 0
            var currPerimeter = 0

            for (adj in listOf(Pair(0, 1), Pair(0, -1), Pair(1, 0), Pair(-1, 0))) {
                val adjPlant = Pair(curr.first + adj.first, curr.second + adj.second)

                if (isInBounds(adjPlant)) {
                    val adjPlantType = grid[adjPlant.first][adjPlant.second]
                    
                    if (adjPlantType == plantType) {
                        stack.addFirst(adjPlant)
                        adjCount++
                        adjacents.add(adj)
                    }
                }
            } 

            if (combinations[adjacents] == "L") {
                val diag = lDiagonals[adjacents]!!

                currPerimeter += getConvexCorner(curr, diag, plantType)
            } else if (combinations[adjacents] == "T") {
                for (diag in tDiagonals[adjacents]!!) {
                    currPerimeter += getConvexCorner(curr, diag, plantType)
                }
            } else if (combinations[adjacents] == "+") {
                for (diag in listOf(Pair(1, 1), Pair(-1, -1), Pair(1, -1), Pair(-1, 1))) {
                    currPerimeter += getConvexCorner(curr, diag, plantType)
                }
            }

            currPerimeter += comboNumbers[combinations[adjacents]]!!
            perimeter += (4 - adjCount)
            newPerimeter += currPerimeter
        }

        result += perimeter * area
        newResult += newPerimeter * area
    }
}

println(result)
println(newResult)

fun getConvexCorner(curr: Pair<Int, Int>, diag: Pair<Int, Int>, plantType: String): Int {
    val adjPlant = Pair(curr.first + diag.first, curr.second + diag.second)

    if (isInBounds(adjPlant)) {
        val adjPlantType = grid[adjPlant.first][adjPlant.second]

        if (adjPlantType != plantType) {
            return 1
        }
    }

    return 0
}

fun isInBounds(adj: Pair<Int, Int>) = adj.first >= 0 && adj.second >= 0 && adj.first < grid.size && adj.second < grid[adj.first].size