File.open(ARGV[0]).each_line do |line|
    t, p = line.chomp.split(',')
    puts (t.rindex(p) || -1)
end
