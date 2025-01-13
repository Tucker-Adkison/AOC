import java.io.File
import java.io.InputStream
import java.math.BigInteger
import java.util.LinkedList

val inputStream: InputStream = File("input_9").inputStream()

val lineList = mutableListOf<String>()
val stack = ArrayDeque<String>()
var freeSpace = 0L
var id = 0L
var fileSystem = mutableListOf<String>()
var free = false

var chunks = mutableListOf<MutableList<String>>()

inputStream.bufferedReader().forEachLine { line ->
    for (c in line) {
        if (!free) {
            val temp = List(c.toString().toInt()) {id.toString()}
            fileSystem.addAll(temp)
            temp.forEach{
                stack.addLast(it)
            }
            id++
            
            if (temp.isNotEmpty()) {
                chunks.add(temp.toMutableList())
            }
        } else {
            val temp = List(c.toString().toInt()) {"."}
            fileSystem.addAll(temp)
            freeSpace += c.toString().toInt()

            if (temp.isNotEmpty()) {
                chunks.add(temp.toMutableList())
            }
        }
        
        free = !free
    }
} 

val amountToRemove = freeSpace.toInt()

while (freeSpace > 0 && stack.isNotEmpty()) {
    val char = stack.removeLast().toString()
    val index = fileSystem.indexOf(".")
    fileSystem[index] = char
    
    freeSpace--;
}

fileSystem = fileSystem.dropLast(amountToRemove).toMutableList()

var result = 0L

for (i in fileSystem.indices) {
    result += i * fileSystem[i].toString().toInt()
}

for (i in chunks.lastIndex downTo 0) {
    var chunk = chunks[i]
    if (!chunk.contains(".")) {
        var index = -1
        for (j in 0..i) {
            if (chunks[j].contains(".")) {
                val indices = mutableListOf<Int>()
                
                for ((i, v) in chunks[j].withIndex()) {
                    if (v == ".") {
                        indices.add(i)
                    }
                }
                
                if (indices.size >= chunk.size) {
                    for (k in chunk.indices) {
                        chunks[j][indices[k]] = chunk[k]
                        chunk[k] = "."
                    }

                    break
                }
            }
        }
    }
}

var i = 0L
result = 0L

var chunkString = ""
for (chunk in chunks) {
    for (c in chunk) {
        if (c == ".") {
            i++
            continue
        }
        
        result += i * c.toInt()

        i++
    }
}

println(result)