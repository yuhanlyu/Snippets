File.open(ARGV[0]).each_line do |line|
    l1, l2 = line.chomp.split(" | ").map {|s| s.split.map(&:to_i)}
    puts l1.zip(l2).map {|x, y| "#{x * y}"}.join(" ")
end
