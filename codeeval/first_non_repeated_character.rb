File.open(ARGV[0]).each_line do |line|
    counts = line.each_char.each_with_object(Hash.new(0)) {|c, h| h[c] += 1}
    puts line.each_char.find {|c| counts[c] == 1}
end
