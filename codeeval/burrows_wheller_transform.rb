File.open(ARGV[0]).each_line do |line|
    s = line.chomp[0...-1]
    p, k = s.each_char.with_index.sort, s.index("$")
    puts (0...s.size).map {|_| (_, k = p[k][0], p[k][1])[0]}.join
end
