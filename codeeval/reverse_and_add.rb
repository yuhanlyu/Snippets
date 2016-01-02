File.open(ARGV[0]).each_line do |line|
    n, i, r = line.to_i, 0, line.reverse.to_i
    n, i, r = n + r, i + 1, (n + r).to_s.reverse.to_i while n != r
    puts "#{i} #{n}"
end
