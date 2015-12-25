File.open(ARGV[0]).each_line do |line|
    up = line.chomp.each_char.count {|c| c == c.upcase}.to_f
    printf("lowercase: %.2f uppercase %.2f \n", 
            ((line.size - up) / line.size) * 100, 
            (up / line.size) * 100)
end
