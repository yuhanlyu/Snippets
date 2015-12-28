File.open(ARGV[0]).each_line do |line|
    l1x, l1y, r1x, r1y, l2x, l2y, r2x, r2y = line.split(",").map(&:to_i)
    puts (!(l1x > r2x || l2x > r1x || l1y < r2y || l2y < r1y)).to_s.capitalize
end
