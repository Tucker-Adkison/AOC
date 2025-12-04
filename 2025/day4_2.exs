defmodule Day4 do
  def process_list(lines, acc) do
    neighbors = [{0, 1}, {1, 0}, {0, -1}, {-1, 0}, {1, 1}, {-1, 1}, {1, -1}, {-1, -1}]

    {new_lines, count} =
      Enum.reduce(0..(length(lines) - 1), {[], 0}, fn i, {list_acc, count_acc} ->
        line = Enum.at(lines, i)

        {new_line, count} =
          Enum.reduce(0..(length(line) - 1), {[], 0}, fn j, {list_acc, count_acc} ->
            char = Enum.at(line, j)

            num_of_ats =
              if char == "@" do
                Enum.reduce(neighbors, 0, fn n, acc ->
                  first = elem(n, 0) + i
                  second = elem(n, 1) + j

                  if first >= 0 and first < length(lines) and second >= 0 and
                       second < length(line) and
                       Enum.at(Enum.at(lines, first), second) == "@",
                     do: acc + 1,
                     else: acc
                end)
              end

            if num_of_ats < 4 and not is_nil(num_of_ats),
              do: {["." | list_acc], count_acc + 1},
              else: {[char | list_acc], count_acc}
          end)

        {[Enum.reverse(new_line) | list_acc], count_acc + count}
      end)

    if count != 0 do
      acc + process_list(new_lines, count)
    else
      count
    end
  end

  def main do
    lines =
      File.stream!("inputs/input_4.txt")
      |> Enum.map(fn line ->
        Enum.filter(String.split(line, "", trim: true), fn line ->
          not is_nil(line) and line != "\n"
        end)
      end)

    IO.puts(process_list(lines, 1))
  end
end

Day4.main()
