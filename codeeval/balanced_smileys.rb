File.open(ARGV[0]).each_line do |line|
    min = max = 0
    line.chomp.gsub(/:\(/, "[").gsub(/:\)/, "]").each_char.with_index {|c, i|
        case c
        when "("
            min, max = min + 1, max + 1
        when ")"
            min, max = min - 1, max - 1
            break if max < 0
        when "["
            max += 1
        when "]"
            min -= 1
        end
    }
    puts 0.between?(min, max) ? "YES" : "NO"
end
