File.open(ARGV[0]).each_line do |line|
    puts line[0...line.size / 2].each_char
    .zip(line[line.size / 2...-1].each_char).reduce(1) {|ans, (a, b)|
        if a == b && a == '*'
            ans * 2
        elsif a != b && !(a == '*' || b == '*')
            0
        else
            ans
        end
    }
end
