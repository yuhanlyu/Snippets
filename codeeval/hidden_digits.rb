File.open(ARGV[0]).each_line do |line|
    result = ""
    line.chars.each do |c|
        if c =~ /[0-9]/
            result << c
        elsif c =~ /[a-j]/
            result << (c.ord - 97).to_s
        end
    end
    puts result.empty? ? "NONE" : result
end
