open Core

type direction = Left | Right

let parse_direction = function
  | 'L' -> Left
  | 'R' -> Right
  | c -> failwith (sprintf "invalid direction: %c" c)

let parse_rotations input =
  String.split_lines input
  |> List.filter ~f:(fun line -> not (String.is_empty (String.strip line)))
  |> List.map ~f:(fun line ->
         let direction = parse_direction (String.get line 0) in
         let distance = Int.of_string (String.drop_prefix line 1) in
         (direction, distance))

let rec process_rotations cur_pos count_zeros remaining_rotations =
  match remaining_rotations with
  | [] -> count_zeros
  | (direction, distance) :: remaining_rotations ->
      let new_pos =
        match direction with
        | Right -> (cur_pos + distance) % 100
        | Left -> (((cur_pos - distance) % 100) + 100) % 100
      in
      let new_count = if new_pos = 0 then count_zeros + 1 else count_zeros in
      process_rotations new_pos new_count remaining_rotations

let rec process_rotations_2 cur_pos count_zeros remaining_rotations =
  match remaining_rotations with
  | [] -> count_zeros
  | (direction, distance) :: remaining_rotations ->
      let new_pos =
        match direction with
        | Right -> (cur_pos + distance) % 100
        | Left -> (((cur_pos - distance) % 100) + 100) % 100
      in
      let passed_zero_count =
        match direction with
        | Right -> (cur_pos + distance) / 100
        | Left ->
            if cur_pos = 0 then distance / 100
            else if distance >= cur_pos then 1 + ((distance - cur_pos) / 100)
            else 0
      in
      let new_count = count_zeros + passed_zero_count in
      process_rotations_2 new_pos new_count remaining_rotations

let solve input =
  let rotations = parse_rotations input in
  process_rotations_2 50 0 rotations
