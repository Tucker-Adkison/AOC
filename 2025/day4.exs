defmodule Day4 do
  def main do
    lines =
      File.stream!("inputs/input_4.txt")
      |> Enum.map(fn line ->
        String.split(line, "", trim: true)
      end)

    neighbors = [{0, 1}, {1, 0}, {0, -1}, {-1, 0}, {1, 1}, {-1, 1}, {1, -1}, {-1, -1}]

    IO.puts(
      Enum.reduce(0..length(lines), 0, fn i, acc ->
        line = Enum.at(lines, i)

        acc +
          if not is_nil(line) do
            Enum.reduce(0..length(line), 0, fn j, acc ->
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
                else
                  -1
                end

              if num_of_ats < 4 and num_of_ats != -1, do: acc + 1, else: acc
            end)
          else
            0
          end
      end)
    )
  end
end

Day4.main()
