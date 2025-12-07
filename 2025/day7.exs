defmodule Day7 do
  def main do
    {_, result} =
      File.stream!("inputs/input_7.txt")
      |> Enum.map(fn line -> String.split(line, "", trim: true) end)
      |> Enum.reduce({[], 0}, fn line, {prev, result} ->
        {indexs, count} =
          Enum.reduce(Enum.with_index(line), {[], 0}, fn {c, i}, {acc, count} ->
            if i not in prev do
              if c == "S", do: {[i | acc], count}, else: {acc, count}
            else
              if c == "^", do: {[i + 1, i - 1 | acc], count + 1}, else: {[i | acc], count}
            end
          end)

        {indexs, result + count}
      end)

    IO.puts(result)
  end
end

Day7.main()
