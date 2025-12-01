local file = io.open("inputs/input_1.txt")

local dial = 50
local result = 0

for line in file:lines() do
  local t = {}
  local startPosL, endPosL = string.find(line, "L")
  local startPosR, endPosR = string.find(line, "R")

  if startPosL then 
    local lDial = tonumber(string.sub(line, startPosL + 1, #line))
    for i = 1, lDial do 
      if dial == 0 then 
        if i ~= 1 then
          result = result + 1 
        end
        dial = 99
      else 
        dial = dial - 1 
      end
    end

    if dial == 0 then
      result = result + 1 
    end
  else 
    local rDial = tonumber(string.sub(line, startPosR + 1, #line))
    for i = 1, rDial do 
      if dial == 99 then 
        result = result + 1 
        dial = 0
      else 
        dial = dial + 1 
      end
    end
  end
end

print(result)