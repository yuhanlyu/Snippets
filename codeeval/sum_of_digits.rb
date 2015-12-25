File.open(ARGV[0]).each_line do |line|
    puts line.chars.map(&:to_i).inject(:+)
end
