cache = Hash.new
File.open(ARGV[0]).each_line.drop(1).map(&:to_i).each do |x|
    puts (0..Math.sqrt(x / 2.0).floor).count {|a|
        cache[a] = a * a if !cache.has_key?(a)
        b = Math.sqrt(x - cache[a]).floor
        cache[b] = b * b if !cache.has_key?(b)
        (a * a + b * b == x) ? true : false
    }
end
