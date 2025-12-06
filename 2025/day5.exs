defmodule Day5 do
  def main do
    lines =
      File.stream!("inputs/input_5.txt")
      |> Enum.map(fn line ->
        String.split(line |> String.replace("\n", ""), "-", trim: true)
      end)

    IO.puts(
      List.foldr(lines, 0, fn line, acc ->
        if length(line) == 1 do
          num = String.to_integer(Enum.at(line, 0))

          acc +
            Enum.reduce_while(lines, 0, fn line, acc ->
              if length(line) == 0 do
                {:halt, acc}
              else
                if length(line) == 2 do
                  if check_in_range(line, num) do
                    {:halt, acc + 1}
                  else
                    {:cont, acc}
                  end
                else
                  {:halt, acc}
                end
              end
            end)
        else
          acc
        end
      end)
    )
  end

  def check_in_range(range, num) do
    [first, second] = range

    num >= String.to_integer(first) and num <= String.to_integer(second)
  end
end

Day5.main()
