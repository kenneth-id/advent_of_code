open Core

let solvers = [ (1, Aoc_2025.Day_01.solve) ]

let () =
  match Sys.get_argv () with
  | [| _; day_str |] -> (
      let day = Int.of_string day_str in
      match List.Assoc.find solvers ~equal:Int.equal day with
      | Some solver ->
          let filename = sprintf "input/day_%02d.txt" day in
          let input = In_channel.read_all filename in
          let result = solver input in
          printf "Day %d: %d\n" day result
      | None -> printf "Day %d not implemented\n" day)
  | _ -> printf "Usage: aoc_2025 <day>\n"
