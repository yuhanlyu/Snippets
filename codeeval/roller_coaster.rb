File.open(ARGV[0]).each_line do |line|
    puts line.each_char.each_with_object([false]).map {|c, is_even|
        if c =~ /[[:alpha:]]/
           is_even[0] = !is_even[0];
           is_even[0] ? c.upcase : c.downcase
        else
            c
        end
    }.join("")
end
