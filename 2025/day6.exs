defmodule Day5 do
  def main do
    chunks =
      File.stream!("inputs/input_6.txt")
      |> Enum.map(fn line -> String.split(line) end)
      |> List.flatten()
      |> Enum.chunk_by(fn x -> x == "+" or x == "*" end)

    [nums, operations] = chunks

    chunks =
      nums
      |> Enum.with_index()
      |> Enum.group_by(fn {_, index} ->
        rem(index + length(operations), length(operations))
      end)

    IO.puts(
      Enum.reduce(0..length(operations), 0, fn i, acc ->
        chunk = chunks[i]
        operation = operations |> Enum.at(i)

        if is_nil(chunk) do
          acc
        else
          result =
            Enum.reduce(chunk, 0, fn {num, _}, acc ->
              cond do
                operation == "+" -> acc + String.to_integer(num)
                operation == "*" -> max(acc, 1) * String.to_integer(num)
                true -> acc
              end
            end)

          acc + result
        end
      end)
    )
  end
end

Day5.main()
