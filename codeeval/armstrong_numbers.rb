File.open(ARGV[0]).each_line do |line|
    puts (line.chomp.each_char
                   .map(&:to_i)
                   .map {|x| x ** (line.size - 1)}
                   .inject(:+) == line.to_i).to_s.capitalize
end
