local file = io.open("inputs/input_3.txt")
local result = 0

for line in file:lines() do
  local curr = ""

  for i = #line, 1, -1 do 
    local c = line:sub(i, i)

    if #curr < 12 then 
      curr = c .. curr
    else 
      local newCurr = curr
      for j = 12, 1, -1 do 
        local temp = c .. curr:sub(1, j-1) .. curr:sub(j+1)
        if tonumber(temp) > tonumber(newCurr) then 
          newCurr = temp
        end
      end
      
      curr = newCurr
    end
  end
  
  result = result + tonumber(curr:sub(1, 12))
end

print(result)