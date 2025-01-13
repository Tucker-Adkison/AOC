import java.io.File
import java.io.InputStream

val inputStream: InputStream = File("input_19").inputStream()

val combos = mutableListOf<String>()
val memo = mutableMapOf<Int, Long>()

var i = 0 
var result = 0L
inputStream.bufferedReader().forEachLine { line ->
    if (i == 0) {
        for (l in line.split(", ")) {
            combos.add(l)
        }
    } else if (line.isNotEmpty()) {
        memo.clear()
        result += search("", line, combos, 0, 0L)   
    }
    
    i++
}

println(result)

fun search(curr: String, target:String, combos: List<String>, index: Int, result: Long): Long {
    var currResult = result

    if (index in memo) {
        return memo[index]!!
    }

    if (curr == target) {
        return 1L
    } else if (index == target.length) {
        return 0L
    }

    var con = ""
    for (i in index..<target.length) {
        con += target[i]

        if (con in combos) {
            var temp = search(curr + con, target, combos, i + 1, result)
            
            memo[i+1] = temp

            currResult += temp
        }
    }

    return currResult
}