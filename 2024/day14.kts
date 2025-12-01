import java.io.File
import java.io.InputStream
import kotlin.math.max
import java.util.ArrayDeque

val inputStream: InputStream = File("inputs/input_14").inputStream()

var positions = mutableListOf<Pair<Int, Int>>()
var velocities = mutableListOf<Pair<Int, Int>>()
var visited = mutableSetOf<Pair<Int, Int>>() 

inputStream.bufferedReader().forEachLine { 
    val posVel = it.split(" ")

    val pos = posVel[0].split("=")[1].split(',').map {it.toInt()}
    val vel = posVel[1].split("=")[1].split(',').map {it.toInt()}

    positions.add(pos[0] to pos[1])
    velocities.add(vel[0] to vel[1])

} 

val width = 101
val height = 103
var seconds = 1
var newPositions = mutableListOf<Pair<Int, Int>>()

// for (i in 0..<100) {
while (true) {
    newPositions = mutableListOf<Pair<Int, Int>>()

    for ((pos, vel) in positions.zip(velocities)) {
        var newPos = Pair(pos.first + vel.first, pos.second + vel.second)

        if (newPos.first >= width) {
            newPos = Pair(newPos.first - width, newPos.second)
        }

        if (newPos.second >= height) {
            newPos = Pair(newPos.first, newPos.second - height)
        }

        if (newPos.first < 0) {
            newPos = Pair(width + newPos.first, newPos.second)
        }

        if (newPos.second < 0) {
            newPos = Pair(newPos.first, height + newPos.second)
        }

        newPositions.add(newPos)
    }

    var entropy = 0

    for (position in newPositions) {
        entropy = max(bfs(position, newPositions), entropy)
    }

    if (entropy > 100) {
        break
    }

    positions = newPositions

    visited.clear()
    seconds++
}

for (i in 0..<width) {
    for (j in 0..<height) {
        if (Pair(i, j) in newPositions) {
            print("#")
        } else {
            print(".")
        }
    }
    println()
}

println(seconds)

// val counts = positions.groupingBy { it }.eachCount()
// var result = 1
// var middleW = width / 2
// var middleH = height/ 2

// result *= checkQuad(0, middleW, 0, middleH, counts)
// result *= checkQuad(width - middleW, width, 0, middleH, counts)
// result *= checkQuad(0, middleW, height - middleH, height, counts)
// result *= checkQuad(width - middleW, width, height - middleH, height, counts)

fun checkQuad(left: Int, right: Int, bottom: Int, top: Int, counts: Map<Pair<Int, Int>, Int>): Int {
    var count = 0
    for (i in left..<right) {
        for (j in bottom..<top) {
            if (Pair(i, j) in counts) {
                count += counts[Pair(i, j)]!!
            }
        }
    }

    return count
}

fun bfs(start: Pair<Int, Int>, positions: List<Pair<Int, Int>>): Int {
    val queue = ArrayDeque<Pair<Int, Int>>(listOf(start))
    var seen = 1

    visited.add(start)

    while (queue.isNotEmpty()) {
        var pos = queue.removeFirst()

        for (i in -1..1) {
            for (j in -1..1) {
                val adj = Pair(pos.first + i, pos.second + j)

                if (!(adj in visited) && adj in positions) {
                    visited.add(adj)
                    queue.addLast(adj)
                    seen += 1
                }
            }
        }
    }

    return seen
}