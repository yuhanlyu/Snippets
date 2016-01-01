File.open(ARGV[0]).each_line do |line|
    puts line.split(" | ").map {|row| row.split.map(&:to_i)}.transpose.sort
             .transpose.map {|row| row.join(" ")}.join(" | ")
end
