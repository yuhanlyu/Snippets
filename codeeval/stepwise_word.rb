File.open(ARGV[0]).each_line do |line|
    puts line.split.max_by {|s| s.length}.each_char.with_index.map {|c, i| 
        "*" * i + c}.join(" ")
end
