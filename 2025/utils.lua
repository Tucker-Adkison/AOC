function split(inputString, delimiter)
    local result = {}
    -- Pattern to match any character that is NOT the delimiter, one or more times
    local pattern = "([^" .. delimiter .. "]+)"
    for match in string.gmatch(inputString, pattern) do
        table.insert(result, match)
    end
    return result
end

return {
  split = split
}