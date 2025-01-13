import java.io.File
import java.io.InputStream
import kotlin.math.min
import kotlin.math.roundToLong
import kotlin.collections.ArrayDeque

val inputStream: InputStream = File("input_13").inputStream()
var aButtons = mutableListOf<Pair<Long, Long>>()
var bButtons = mutableListOf<Pair<Long, Long>>()
var prizes = mutableListOf<Pair<Long, Long>>()

inputStream.bufferedReader().forEachLine { line ->
    when {
        line.startsWith("Button") -> {
            val (button, ops) = line.split(": ")
            val (xOp, yOp) = ops.split(", ")
            
            // Extract numbers from X and Y operations
            val x = xOp.replace("X+", "").toLong()
            val y = yOp.replace("Y+", "").toLong()

            if (button == "Button A") {
                aButtons.add(x to y)
            } else if (button == "Button B") {
                bButtons.add(x to y)
            }
        }
        line.startsWith("Prize") -> {
            val coords = line.split(": ")[1]
            val (xStr, yStr) = coords.split(", ")
            val x = xStr.split("=")[1].toLong()
            val y = yStr.split("=")[1].toLong()

            prizes.add(Pair(10000000000000 + x, 10000000000000 + y))
        }
    }

}

var results = 0.0

for (i in aButtons.indices) {
    var buttonA = aButtons[i]
    var buttonB = bButtons[i]
    var prize = prizes[i]
    val matrix = arrayOf(
        doubleArrayOf(buttonA.first.toDouble(), buttonB.first.toDouble()),
        doubleArrayOf(buttonA.second.toDouble(), buttonB.second.toDouble()),
    )

    val inverseMatrix = inverse(matrix)
    val costA = (inverseMatrix[0][0] * prize.first + inverseMatrix[0][1] * prize.second).roundToLong()
    val costB = (inverseMatrix[1][0] * prize.first + inverseMatrix[1][1] * prize.second).roundToLong()
    val finalA = buttonA.first * costA + buttonB.first * costB
    val finalB = buttonA.second * costA + buttonB.second * costB

    if ((finalA == prize.first) && (finalB == prize.second)) {
            val cost = (costA * 3) + costB

            results += cost
    }
}

fun inverse(matrix: Array<DoubleArray>): Array<DoubleArray> {
    val determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    if (determinant == 0.0) {
        throw IllegalArgumentException("Matrix is not invertible.")
    }

    return arrayOf(
        doubleArrayOf(matrix[1][1] / determinant, -matrix[0][1] / determinant),
        doubleArrayOf(-matrix[1][0] / determinant, matrix[0][0] / determinant)
    )
}

println(results)