local utils = require "utils"

local function checkIfRepeating(id) 
  local str = tostring(id)
  local strLen = #str
  local mid = math.floor(#str / 2)
  local didBreak = false

  for step = 1, mid do
    local curr = str:sub(1, 1+step-1)
    local count = 0
    didBreak = false
    for i = 1, strLen, step do
      local temp = str:sub(i, i+step-1)

      if temp ~= curr then 
        didBreak =true 
        break
      else 
        count = count + 1
      end
    end

    if not didBreak and count >= 2 then 
      return true 
    end
  end

  return not didBreak
end

local result = 0
local file = io.open("inputs/input_2.txt")

for line in file:lines() do
  local commaSplit = utils.split(line, ",")
  for _, commaPair in ipairs(commaSplit) do
    local startId, endId = string.match(commaPair, "(%d+)-(%d+)")

    for id = startId, endId do
      id = math.floor(id)
      if #tostring(id) >= 2 and  checkIfRepeating(id) then 
        result = result + id
      end
    end 
  end
end

print(result)
