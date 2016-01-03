map = {"(" => ")", "[" => "]", "{" => "}"}
File.open(ARGV[0]).each_line do |line|
    result, s = true, []
    line.chomp.each_char {|c|
        if map.has_key?(c)
            s << map[c]
        elsif map.has_value?(c)
            result = false if s.size == 0 || c != s.pop
        end
    }
    puts (result && s.size == 0).to_s.capitalize
end
