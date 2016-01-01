map = {"a" => "u", "u" => "a", "b" => "v", "v" => "b",
       "c" => "w", "w" => "c", "d" => "x", "x" => "d",
       "e" => "y", "y" => "e", "f" => "z", "z" => "f",
       "g" => "n", "n" => "g", "h" => "o", "o" => "h",
       "i" => "p", "p" => "i", "j" => "q", "q" => "j",
       "k" => "r", "r" => "k", "l" => "s", "s" => "l",
       "m" => "t", "t" => "m"}
File.open(ARGV[0]).each_line do |line|
    puts line.chomp.each_char.map {|c| map[c]}.join
end
