File.open(ARGV[0]).each_line do |line|
    rows = line.split(" | ").map {|row| row.split.map(&:to_i)}
    puts (0...rows[0].length).each.map {|col| 
        rows[(0...rows.length).max_by{|x| rows[x][col]}][col]}.join(" ")
end
