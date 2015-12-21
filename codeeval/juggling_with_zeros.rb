File.open(ARGV[0]).each_line do |line|
    puts line.split.each_slice(2).each_with_object([]) { |(a, b), result| 
        result.push((a == "0" ? "0" : "1") * b.size) 
    }.join('').to_i(2)
end
