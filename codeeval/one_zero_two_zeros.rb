File.open(ARGV[0]).each_line do |line|
    num, max = line.split.map(&:to_i)
    puts (1..max).count {|i| i.to_s(2).each_char.count('0') == num}
end
