File.open(ARGV[0]).each_line do |line|
    s, p = line.split(";").map(&:split)
    p = p.map {|i| i.to_i - 1}
    p += [(0...s.length).find {|i| !p.include?(i)}]
    puts (0...s.length).each_with_object(Array.new(s.length)) {|i,r|
          r[p[i]] = s[i]}.join(" ")
end
