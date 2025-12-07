defmodule Day7 do
  def main do
    lines =
      File.stream!("inputs/input_7.txt")
      |> Enum.map(fn line -> String.split(line, "", trim: true) end)

    start_index = lines |> hd() |> Enum.find_index(&(&1 == "S"))
    {result, _} = split(lines, 0, start_index, %{})
    IO.puts(result + 1)
  end

  def split([], _, _, m) do
    {0, m}
  end

  def split([head | tail], line_index, index, memo) do
    key = {line_index, index}

    if Map.has_key?(memo, key) do
      {Map.get(memo, key), memo}
    else
      {result, m3} =
        if Enum.at(head, index) == "^" do
          {r1, m1} =
            split(tail, line_index + 1, index + 1, memo)

          {r2, m2} = split(tail, line_index + 1, index - 1, m1)

          {r1 + r2 + 1, m2}
        else
          split(tail, line_index + 1, index, memo)
        end

      {result, Map.put(m3, key, result)}
    end
  end
end

Day7.main()
