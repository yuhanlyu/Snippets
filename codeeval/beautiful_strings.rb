File.open(ARGV[0]).each_line do |line|
    puts line.downcase.gsub(/[^a-z]/, '').each_char
             .each_with_object(Array.new(26, 0)) {|c, counts| 
                counts[c.ord - 97] += 1}
             .sort.reverse.zip(26.downto(1)).inject(0) {|sum, (c, weight)|
                sum += c * weight }
end
