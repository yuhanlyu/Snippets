File.open(ARGV[0]).each_line do |line|
    t, p = line.chomp.split(",")
    puts t.end_with?(p) ? 1 : 0
end
