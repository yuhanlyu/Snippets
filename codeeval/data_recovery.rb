File.open(ARGV[0]).each_line do |line|
    s, p = line.split(";").map(&:split)
    p = p.map {|i| i.to_i - 1}
    p += [(0...s.length).find {|i| !p.include?(i)}]
    puts p.zip(s).sort.map(&:last).join(" ")
end
