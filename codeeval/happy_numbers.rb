require 'set'
File.open(ARGV[0]).each_line do |line|
    n, set = line.to_i, Set.new
    while n != 1 && !set.include?(n)
        set.add(n)
        n = n.to_s.each_char.map(&:to_i).map(&:abs2).inject(:+)
    end
    puts n == 1 ? 1 : 0
end
