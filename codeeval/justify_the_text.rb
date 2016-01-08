File.open(ARGV[0]).each_line do |line|
    words, result, cur, length = line.chomp.split, [], [], 0
    words.each {|word|
        if length + word.size + cur.size > 80
            if cur.size == 1
                result << "%-80s" % cur[0]
            else
                space, remain = (80 - length).divmod(cur.size - 1)
                result << ([cur[0]] + cur.drop(1).each_with_index.map {|x, i|
                    "%*s" % [space + (i < remain ? 1 : 0) + x.size, x]
                }).join
            end
            length, cur = 0, []
        end
        cur << word
        length += word.size
    }
    result << "%-80s" % cur.join(" ") if cur.size > 0
    result.map(&method(:puts))
end
