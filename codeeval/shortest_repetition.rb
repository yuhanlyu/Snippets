File.open(ARGV[0]).each_line do |line|
    line.chomp!
    puts (1..line.length).find {|i| line[0...i] * (line.length / i) == line }
end
