File.open(ARGV[0]).each_line do |line|
    s, p = line.split(", ")
    puts s.delete(p)
end
