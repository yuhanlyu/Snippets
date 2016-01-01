File.open(ARGV[0]).each_line do |line|
    puts line.split.reverse.each_slice(2).map(&:first).join(" ")
end
