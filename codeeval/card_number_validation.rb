File.open(ARGV[0]).each_line do |line|
    puts line.gsub(/\D/, "").each_char.map(&:to_i).reverse.each_with_index
             .map {|n, i| i % 2 == 0 ? n : 2 * n}
             .map {|n| n < 10 ? n : n.to_s.each_char.map(&:to_i).reduce(:+)}
             .reduce(:+) % 10 == 0 ? 1 : 0
end
