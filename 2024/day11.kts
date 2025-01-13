import java.io.File
import java.io.InputStream

var stones = mutableListOf<Long>()
val memo = mutableMapOf<String, Long>()
val inputStream: InputStream = File("input_11").inputStream()

inputStream.bufferedReader().forEachLine { line ->
    var result = 0L
    for (digit in line.split(" ")) {
        result += calculate(digit.toLong(), 0, 75)
    }

    println(result)
}

fun calculate(stone: Long, depth: Int, maxDepth: Int): Long {
    var result = 0L

    if (depth == maxDepth) {
        return 1L
    } else if (memo.contains(stone.toString() + "|" + depth.toString())) {
        return memo[stone.toString() + "|" + depth.toString()]!!
    } 
 
    val stoneStr = stone.toString()

    if (stoneStr == "0") {
        result += calculate(1, depth + 1, maxDepth)
    } else if (stoneStr.length % 2 == 0) {
        val mid = stoneStr.length / 2
        
        result += calculate(stoneStr.substring(0, mid).toLong(), depth + 1, maxDepth)
        result += calculate(stoneStr.substring(mid).toLong(), depth + 1, maxDepth)
    } else {
        result += calculate(stone * 2024L, depth + 1, maxDepth)
    }

    memo[stone.toString() + "|" + depth.toString()] = result

    return result
}