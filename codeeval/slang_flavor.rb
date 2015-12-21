slang = [", yeah!", ", this is crazy, I tell ya.", ", can U believe this?", 
         ", eh?", ", aw yea.", ", yo.", "? No way!", ". Awesome!"]
index, round = -1, true
File.open(ARGV[0]).each_line do |line|
    puts line.gsub(/[\.\?!]/) { |w| 
        round = !round
        if round
            index = (index + 1) % slang.size; 
            slang[index] 
        else
            w
        end
    }
end
