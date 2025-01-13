import java.io.File
import java.io.InputStream
import kotlin.collections.ArrayDeque

typealias Node = Pair<String, Int>

fun findGates(a: String, b: String, rules: MutableList<String>): List<String> {
    val gates = mutableListOf<String>()
    for (rule in rules) {
        if (a in rule && b in rule) {
            gates.add(rule)
        }
    }

    return gates
}

fun replaceRule(firstRule: String, secondRule: String, rules: MutableList<String>) {
    val index = rules.indexOf(firstRule)
    
    rules[index] = secondRule
}

fun findAllGates(a: String, rules: MutableList<String>): List<String> {
    val gates = mutableListOf<String>()
    
    for (rule in rules) {
        if (a in rule) {
            gates.add(rule)
        }
    }

    return gates
}

fun addBinary(a: String, b: String): String {
    var carry = 0
    var result = ""
    var i = a.length - 1
    var j = b.length - 1

    while (i >= 0 || j >= 0 || carry > 0) {
        val digitA = if (i >= 0) a[i--] - '0' else 0
        val digitB = if (j >= 0) b[j--] - '0' else 0

        val sum = digitA + digitB + carry
        carry = sum / 2
        result = (sum % 2).toString() + result
    }

    return result
}

fun performRule(rule: String, registers: MutableMap<String, Int>): Node {
    val leftRightSplit = rule.split("->")

    val iAndO = leftRightSplit[0].split(" ")
    val a = iAndO[0]
    val b = iAndO[2]
    val result = when(iAndO[1]) {
        "OR" -> registers[a]!!.or(registers[b]!!)
        "XOR" -> registers[a]!!.toInt().xor(registers[b]!!)
        "AND" -> registers[a]!!.toInt().and(registers[b]!!)
        else -> -1
    }

    registers[leftRightSplit[1].trimStart()] = result

    return Node(leftRightSplit[1].trimStart(), result)
}

val inputStream: InputStream = File("inputs/input_24").inputStream()
val xRegisters = mutableListOf<Node>()
val yRegisters = mutableListOf<Node>()
val registers = mutableMapOf<String, Int>()
val rules = mutableListOf<String>()

inputStream.bufferedReader().forEachLine { line ->
    if (!line.isEmpty()) {
        if (":" in line) {
            val rAndV = line.split(":")

            if ('x' in rAndV[0]) {
                xRegisters.add(Node(rAndV[0], rAndV[1].trimStart().toInt()))
            } else {
                yRegisters.add(Node(rAndV[0], rAndV[1].trimStart().toInt()))
            }

            registers[rAndV[0]] = rAndV[1].trimStart().toInt()
        } else {
            if (line.isNotEmpty()) {
                rules.add(line)
            }
        }
    }
}

var binaryX = ""
var binaryY = ""

for ((xPair, yPair) in xRegisters.zip(yRegisters)) {
    binaryX = xPair.second.toString() + binaryX
    binaryY = yPair.second.toString() + binaryY
}

var swappedRules = mutableListOf<String>()
var binary = addBinary(binaryX, binaryY)
var cIn: Node? = null
var output = ""
var i = 0

for ((xPair, yPair) in xRegisters.zip(yRegisters)) {
    var z = "z$i"

    if (i < 10) {
        z = "z0$i"
    }

    var gates = findGates(xPair.first, yPair.first, rules) 
    var firstRule = gates.filter {"XOR" in it}.first()
    var secondRule = gates.filter {"AND" in it}.first()

    var dNode = performRule(firstRule, registers)
    var eNode = performRule(secondRule, registers)

    if (cIn != null) {
        var zGates = findGates(cIn!!.first, dNode.first, rules).toMutableList()

        if (zGates.isEmpty()) {        
            val firstRuleReplaced = firstRule.replace(dNode.first, eNode.first)
            val secondRuleReplaced = secondRule.replace(eNode.first, dNode.first)
            
            replaceRule(firstRule, firstRuleReplaced, rules)
            replaceRule(secondRule, secondRuleReplaced, rules)

            swappedRules.add(dNode.first)
            swappedRules.add(eNode.first)

            zGates = findGates(cIn!!.first, eNode.first, rules).toMutableList()
            eNode = performRule(secondRule.replace(eNode.first, dNode.first), registers)

            firstRule = firstRuleReplaced
            secondRule = secondRuleReplaced
        }

        val zRule = zGates.filter {"XOR" in it}.first()
        var zNode = performRule(zRule, registers)

        if (!('z' in zNode.first)) {
            val badZRule = findAllGates(z, rules).first()

            val badZRuleReplaced = badZRule.replace(z, zNode.first)
            val zRuleReplaced = zRule.replace(zNode.first, z)
            
            replaceRule(badZRule, badZRuleReplaced, rules)
            replaceRule(zRule, zRuleReplaced, rules)

            swappedRules.add(zNode.first)
            swappedRules.add(z)

            if (secondRule == badZRule) {
                eNode = performRule(badZRule.replace(z, zNode.first), registers)
            }

            zNode = performRule(zRule.replace(zNode.first, z), registers)

            if (badZRule in zGates) {
                var index = zGates.indexOf(badZRule)
                zGates[index] = badZRuleReplaced
            } else if (zRule in zGates) {
                var index = zGates.indexOf(zRule)
                zGates[index] = zRuleReplaced
            }
        }
       
        output = zNode.second.toString() + output

        val gRule = zGates.filter {"AND" in it}.first()
        val gNode = performRule(gRule, registers)

        val cInGates = findGates(eNode.first, gNode.first, rules) 
        val cInRule = cInGates.first()
        
        cIn = performRule(cInRule, registers)
    } else {
        output = dNode.second.toString() + output
        cIn = eNode
    }

    i += 1
}

swappedRules.sort()

println(swappedRules.joinToString(","))