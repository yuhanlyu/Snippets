File.open(ARGV[0]).each_line do |line|
    c, b = 1, 1
    (1...line.size).each do |i|
        c = 0 if line[i] == "0"
        c, b = c + (line[i-1..i].to_i.between?(10, 26) ? b : 0), c
    end
    puts c
end
