defmodule Day5 do
  def main do
    {acc, curr, _} =
      File.stream!("inputs/input_6.txt")
      |> Enum.map(fn x -> String.split(x, "") end)
      |> Enum.zip()
      |> Enum.map(&Tuple.to_list/1)
      |> Enum.reduce({0, 0, ""}, fn line, {acc, curr, op} ->
        new_op = if op == "", do: String.trim(Enum.at(line, length(line) - 1)), else: op

        number_str =
          Enum.reduce(line, "", fn s, acc ->
            if String.trim(s) != "" and s != new_op, do: acc <> s, else: acc
          end)

        if number_str != "" do
          cond do
            new_op == "*" ->
              {acc, max(1, curr) * String.to_integer(number_str), new_op}

            new_op == "+" ->
              {acc, curr + String.to_integer(number_str), new_op}

            true ->
              acc
          end
        else
          {acc + curr, 0, ""}
        end
      end)

    IO.puts(acc + curr)
  end
end

Day5.main()
