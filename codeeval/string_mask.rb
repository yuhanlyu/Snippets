File.open(ARGV[0]).each_line do |line|
    s, mask = line.split.map(&:each_char)
    puts s.zip(mask).map {|c, m| m == "1" ? c.swapcase : c}.join
end
