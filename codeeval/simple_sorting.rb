File.open(ARGV[0]).each_line do |line|
    puts line.chomp.split.map(&:to_f).sort.map {|x| "%.3f" % x}.join(" ")
end
