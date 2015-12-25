File.open(ARGV[0]).each_line do |line|
    vals = line.split(",").map {|s| s.split(": ")[1].to_i}
    puts (((3 * vals[0]) + (4 * vals[1]) + (5 * vals[2])) * vals[3])/ \
           (vals[0] + vals[1] + vals[2])
end
