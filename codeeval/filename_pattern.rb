File.open(ARGV[0]).each_line do |line|
    p, *fns = line.chomp.split
    p = "^" + p.gsub(/\./, "\\.").gsub(/\*/, ".*").gsub(/\?/, ".") + "$"
    result = fns.each.select {|fn| fn.match(p)}
    puts result.size > 0 ? result.join(" ") : "-"
end
