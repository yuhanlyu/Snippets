File.open(ARGV[0]).each_line do |line|
    elms = line.split
    m = elms[-1].to_i
    puts elms[-m - 1] if m < elms.size
end
