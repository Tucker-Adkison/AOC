defmodule Day5 do
  def main do
    lines =
      File.stream!("inputs/input_5.txt")
      |> Enum.map(fn line ->
        String.split(line |> String.replace("\n", ""), "-", trim: true)
      end)

    lines_with_two =
      Enum.filter(lines, fn x -> length(x) == 2 end)
      |> Enum.map(fn line -> Enum.map(line, fn x -> String.to_integer(x) end) end)
      |> Enum.map(fn line -> Enum.at(line, 0)..Enum.at(line, 1) end)
      |> Enum.sort()

    IO.inspect(
      Enum.reduce(lines_with_two, [], fn line, acc ->
        if length(acc) == 0 do
          [line]
        else
          [prev | tail] = acc

          if line.first in prev do
            if prev.last < line.last do
              [prev.first..line.last | tail]
            else
              acc
            end
          else
            [line | acc]
          end
        end
      end)
      |> Enum.map(&Range.size/1)
      |> Enum.sum()
    )
  end
end

Day5.main()
