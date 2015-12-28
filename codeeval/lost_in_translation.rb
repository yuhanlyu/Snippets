map = {'y' => 'a', 'n' => 'b', 'f' => 'c', 'i' => 'd', 'c' => 'e', 'w' => 'f', 
       'l' => 'g', 'b' => 'h', 'k' => 'i', 'u' => 'j', 'o' => 'k', 'm' => 'l', 
       'x' => 'm', 's' => 'n', 'e' => 'o', 'v' => 'p', 'z' => 'q', 'p' => 'r', 
       'd' => 's', 'r' => 't', 'j' => 'u', 'g' => 'v', 't' => 'w', 'h' => 'x', 
       'a' => 'y', 'q' => 'z'}

File.open(ARGV[0]).each_line do |line|
    puts line.chomp.split.map {|s| s.each_char.map {|c| map[c]}.join}.join(" ")
end
