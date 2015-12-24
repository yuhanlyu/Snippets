map = {"a" => 1, "b" => 2, "c" => 3, "d" => 4, 
       "e" => 5, "f" => 6, "g" => 7, "h" => 8}
reverse = {1 => "a", 2 => "b", 3 => "c", 4 => "d",
           5 => "e", 6 => "f", 7 => "g", 8 => "h"}
moves = [[-2, -1], [-2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2], [2, -1], [2, 1]]
File.open(ARGV[0]).each_line do |line|
    c, r = map[line[0]], line[1].to_i
    puts moves.map {|dc, dr| [c + dc, r + dr]}
              .select {|c, r| c.between?(1, 8) and r.between?(1, 8)}
              .map {|c, r| reverse[c] + r.to_s}
              .join(' ')
end
